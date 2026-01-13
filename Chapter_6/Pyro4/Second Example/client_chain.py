from __future__ import print_function
import Pyro4

server = Pyro4.core.Proxy("PYRONAME:server")

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

print("Result=%s" % server.multiply_by_scalar(str(result)))