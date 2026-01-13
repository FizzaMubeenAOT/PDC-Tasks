from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Root defines a matrix as a list of rows
    # Each element in this list will be sent to a different process
    array_to_share = [[1, 2], [3, 4]] 
else:
    array_to_share = None

# Scatter the rows: rank 0 gets [1, 2], rank 1 gets [3, 4]
recvbuf = comm.scatter(array_to_share, root=0)

# The row received from scatter
row_a = recvbuf

matrix_b = [[5, 6], [7, 8]]
row_result = [0, 0]

for i in range(2):
    for j in range(2):
        row_result[i] += row_a[j] * matrix_b[j][i]

print("process = %d" % rank + " received row = " + str(recvbuf) + " row result = " + str(row_result))