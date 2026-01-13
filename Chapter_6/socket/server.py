import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)

while True: 
    clientsocket, addr = serversocket.accept()
    print("Connected with %s" % str(addr))
    
    data = clientsocket.recv(1024).decode('ascii')
    print("Received matrix from client: %s" % data)

    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    result = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    response = "Server Matrix Result: " + str(result) + " | Time: " + time.ctime(time.time())
    clientsocket.send(response.encode('ascii'))
    clientsocket.close()