from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


senddata = (rank + 1) * numpy.arange(4, dtype=int)
recvdata = numpy.empty(4, dtype=int)
comm.Alltoall(senddata, recvdata)

# We treat recvdata as Matrix A and senddata as Matrix B
result = numpy.zeros((2, 2), dtype=int)

# Reshape the flat arrays into 2x2 matrices for easy indexing
matrix_a = recvdata.reshape(2, 2)
matrix_b = senddata.reshape(2, 2)

# Standard triple nested loop for matrix multiplication
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

print(" process %s sending %s receiving %s" % (rank, senddata, recvdata))
print(" process %s matrix result:\n%s" % (rank, result))