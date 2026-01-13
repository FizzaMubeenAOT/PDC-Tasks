from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # Defining two 2x2 matrices to share
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    variable_to_share = [matrix_a, matrix_b]
else:
    variable_to_share = None

# Broadcast the matrices to all processes
variable_to_share = comm.bcast(variable_to_share, root=0)

# Unpack the matrices
A = variable_to_share[0]
B = variable_to_share[1]

# Initialize a 2x2 result matrix with zeros
result = [[0, 0], [0, 0]]

# Simple nested loops for matrix multiplication
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]

print("process = %d" %rank + " result matrix = " + str(result))