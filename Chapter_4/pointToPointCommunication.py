from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print("my rank is : ", rank)

if rank == 0:
    # Sending a 2x2 matrix instead of a single number
    data = [[1, 1], [2, 2]]
    destination_process = 4
    comm.send(data, dest=destination_process)
    print("sending data %s to process %d" % (data, destination_process))

if rank == 1:
    # Sending a different 2x2 matrix instead of a string
    data = [[5, 6], [7, 8]]
    destination_process = 8
    comm.send(data, dest=destination_process)
    print("sending data %s to process %d" % (data, destination_process))

if rank == 4:
    received_matrix = comm.recv(source=0)
    print("data received is = %s" % received_matrix)
    
    local_mat = [[1, 2], [3, 4]]
    result = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += received_matrix[i][k] * local_mat[k][j]
    print("Process 4 multiplication result: %s" % result)

if rank == 8:
    received_matrix = comm.recv(source=1)
    print("data1 received is = %s" % received_matrix)
    
    local_mat = [[1, 0], [0, 1]] 
    result = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += received_matrix[i][k] * local_mat[k][j]
    print("Process 8 multiplication result: %s" % result)