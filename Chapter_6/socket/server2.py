import socket

port = 60000
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(15)

print('Server listening....')

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    
    data = conn.recv(1024)
    print('Server received', repr(data.decode()))

    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    result = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    with open('matrix_result.txt', 'w') as f_result:
        f_result.write("Matrix Multiplication Result:\n")
        f_result.write(str(result))

    filename = 'matrix_result.txt'
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
        print('Sent', repr(l.decode()))
        l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('->Thank you for connecting'.encode())
    conn.close()