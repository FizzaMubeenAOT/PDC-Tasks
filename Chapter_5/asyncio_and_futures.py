import asyncio
import sys

async def first_coroutine(future, num):
    # Matrix A * Matrix B
    A = [[num, 1], [1, 1]]
    B = [[1, 2], [3, 4]]
    result = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
                
    await asyncio.sleep(4)
    future.set_result('First coroutine (Matrix Mult) result = %s' % result)

async def second_coroutine(future, num):
    # Matrix C * Matrix D
    C = [[num, num], [num, num]]
    D = [[1, 0], [0, 1]] 
    result = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += C[i][k] * D[k][j]
                
    await asyncio.sleep(4)
    future.set_result('Second coroutine (Matrix Mult) result = %s' % result)

def got_result(future):
    print(future.result())

async def main():
    # Get numbers from command line
    num1 = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    num2 = int(sys.argv[2]) if len(sys.argv) > 2 else 2

    # Create Futures
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    # Add callbacks
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    # Wrap coroutines in Tasks (Fixes the TypeError)
    task1 = asyncio.create_task(first_coroutine(future1, num1))
    task2 = asyncio.create_task(second_coroutine(future2, num2))

    # Wait for the tasks to complete
    await asyncio.wait([task1, task2])

if __name__ == '__main__':
    # asyncio.run() handles the event loop automatically
    asyncio.run(main())