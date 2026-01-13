import Pyro4

scalar = input("Enter a scalar value to multiply with the matrix: ").strip()

server = Pyro4.Proxy("PYRONAME:server")    

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

s = int(scalar)
final_matrix = [[cell * s for cell in row] for row in result]

print(server.multiply_by_scalar(str(final_matrix)))