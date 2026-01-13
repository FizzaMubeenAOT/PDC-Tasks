import concurrent.futures
import time

number_list = list(range(1, 11))

def matrix_multiply_task(scalar):
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    result = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                # Multiply the result by the scalar to simulate unique work
                result[i][j] += (matrix_a[i][k] * matrix_b[k][j]) * scalar
    return result

def evaluate(item):
    result_item = matrix_multiply_task(item)
    print('Item %s, Matrix Result: %s' % (item, result_item))

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.perf_counter()
    for item in number_list:
        evaluate(item)
    print('Sequential Execution in %s seconds' % (time.perf_counter() - start_time))
    
    # Thread Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Thread Pool Execution in %s seconds' % (time.perf_counter() - start_time))

    # Process Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Process Pool Execution in %s seconds' % (time.perf_counter() - start_time))