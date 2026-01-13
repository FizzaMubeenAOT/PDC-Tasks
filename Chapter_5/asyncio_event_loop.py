import asyncio
import time
import random

def do_matrix_mul(task_name):
    # Two small 2x2 matrices
    A = [[random.randint(1, 5), 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    
    print("%s performed matrix multiplication: %s" % (task_name, result))

def task_A(end_time, loop):
    print("\ntask_A called")
    do_matrix_mul("Task A") # Perform multiplication
    time.sleep(random.randint(0, 2)) # Reduced sleep for faster testing
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_B, end_time, loop)
    else:
        loop.stop()

def task_B(end_time, loop):
    print("\ntask_B called")
    do_matrix_mul("Task B") # Perform multiplication
    time.sleep(random.randint(0, 2))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_C, end_time, loop)
    else:
        loop.stop()

def task_C(end_time, loop):
    print("\ntask_C called")
    do_matrix_mul("Task C") # Perform multiplication
    time.sleep(random.randint(0, 2))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_A, end_time, loop)
    else:
        loop.stop()

# Main logic
loop = asyncio.new_event_loop() # Use new_event_loop for better compatibility
asyncio.set_event_loop(loop)

end_loop = loop.time() + 10 # Set to 10 seconds for a quicker demonstration
loop.call_soon(task_A, end_loop, loop)

try:
    loop.run_forever()
finally:
    loop.close()