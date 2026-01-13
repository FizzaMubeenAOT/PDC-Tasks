from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print("my rank is %i" % (rank))

if rank == 1:
    # Matrix A to send
    data_send = [[1, 2], [3, 4]]
    destination_process = 5
    source_process = 5

    # Receive Matrix B from rank 5, then send Matrix A to rank 5
    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)
    
    # Simple matrix multiplication (Result = A * B)
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += data_send[i][k] * data_received[k][j]

    print("sending data %s to process %d" % (data_send, destination_process))
    print("data received is = %s" % data_received)
    print("multiplication result = %s" % result)

if rank == 5:
    # Matrix B to send
    data_send = [[5, 6], [7, 8]]
    destination_process = 1
    source_process = 1

    # Send Matrix B to rank 1, then receive Matrix A from rank 1
    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)
    
    # Simple matrix multiplication (Result = B * A)
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += data_send[i][k] * data_received[k][j]

    print("sending data %s to process %d" % (data_send, destination_process))
    print("data received is = %s" % data_received)
    print("multiplication result = %s" % result)