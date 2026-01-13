from celery import Celery

app = Celery('addTask', broker='amqp://guest@localhost//')

@app.task
def multiply_matrices(matrix_a, matrix_b):
    result = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
                
    return result