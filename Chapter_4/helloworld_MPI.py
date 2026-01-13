from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# --- Simple Matrix Multiplication ---
# Defining two 2x2 matrices
# We use the rank to make the values different for each process
A = [[rank, 1], [2, 3]]
B = [[1, 2], [3, 4]]

# Initialize a 2x2 result matrix with zeros
result = [[0, 0], [0, 0]]

# Standard triple nested loop
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]

print("hello world from process ", rank)
print("process %d matrix result: %s" % (rank, result))