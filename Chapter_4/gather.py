from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Each process creates one row of Matrix A
# For simplicity, we assume 2 processes and 2x2 matrices
row_a = [rank + 1, rank + 2]

# Root gathers all rows to form Matrix A
data = comm.gather(row_a, root=0)

if rank == 0:
    print("rank = %s ...receiving data to other process" % rank)
    
    # Matrix A is now the gathered list of rows
    matrix_a = data 
    # Define a simple constant Matrix B to multiply with
    matrix_b = [[1, 2], [3, 4]]
    # Initialize result matrix with zeros
    result = [[0, 0], [0, 0]]

    # Perform matrix multiplication (matrix_a * matrix_b)
    # i: rows of A, j: columns of B, k: common dimension
    for i in range(len(matrix_a)):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    for i in range(1, size):
        value = data[i]
        print(" process %s receiving %s from process %s" % (rank, value, i))
    
    print("Final Multiplied Matrix:")
    for row in result:
        print(row)