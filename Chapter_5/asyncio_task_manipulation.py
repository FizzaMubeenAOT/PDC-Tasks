import asyncio
async def matrix_mul_part1():
    # Matrix A * Matrix B
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    res = [0, 0] # First row result
    
    print('Asyncio.Task: Computing Matrix Row 1')
    for j in range(2):
        for k in range(2):
            res[j] += A[0][k] * B[k][j]
            await asyncio.sleep(1) # Simulated delay
    print('Asyncio.Task - Row 1 Result = %s' % res)

async def matrix_mul_part2():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    res = [0, 0] # Second row result
    
    print('Asyncio.Task: Computing Matrix Row 2')
    for j in range(2):
        for k in range(2):
            res[j] += A[1][k] * B[k][j]
            await asyncio.sleep(1)
    print('Asyncio.Task - Row 2 Result = %s' % res)

async def matrix_scalar_mul(scalar):
    # Scalar multiplication task
    mat = [[1, 2], [3, 4]]
    print('Asyncio.Task: Computing Scalar Multiplication')
    for i in range(2):
        for j in range(2):
            mat[i][j] *= scalar
            await asyncio.sleep(1)
    print('Asyncio.Task - Scalar Matrix Result = %s' % mat)

if __name__ == '__main__':
    async def main():
        task_list = [
            asyncio.create_task(matrix_mul_part1()),
            asyncio.create_task(matrix_mul_part2()),
            asyncio.create_task(matrix_scalar_mul(10))
        ]
        await asyncio.wait(task_list)

    print('Starting Parallel Matrix Tasks...')
    asyncio.run(main())