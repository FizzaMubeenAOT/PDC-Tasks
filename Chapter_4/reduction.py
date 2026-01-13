import numpy
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
size = comm.size 
rank = comm.rank

# We use 4 elements to represent a 2x2 matrix
array_size = 4
recvdata = numpy.zeros(array_size, dtype=int)
senddata = (rank + 1) * numpy.arange(array_size, dtype=int)

print(" process %s sending %s " % (rank, senddata))

# Sum all matrices from all processes into recvdata on rank 0
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)

if rank == 0:
    matrix_a = recvdata.reshape(2, 2)   
    matrix_b = numpy.array([[1, 2], [3, 4]]) 
    result = numpy.zeros((2, 2), dtype=int) 
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    print('on task', rank, 'after Reduce and Multiplication: \n', result)
else:
    print('on task', rank, 'after Reduce: data = ', recvdata)