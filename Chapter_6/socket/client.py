import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

s.connect((host, port))

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

data_to_send = str(result)
s.send(data_to_send.encode('ascii'))

tm = s.recv(1024)
s.close()

print("Server response: %s" % tm.decode('ascii'))