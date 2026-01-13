import socket

s = socket.socket()
host = socket.gethostname()
port = 60000

s.connect((host, port))

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

s.send(str(result).encode())

with open('received.txt', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        if not data:
            break
        print('Data=>', data.decode())
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')