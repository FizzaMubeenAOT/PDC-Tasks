from mpi4py import MPI
import numpy as np

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0,0,0,0]

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    grid_row = int(np.floor(np.sqrt(comm.size)))
    grid_column = comm.size // grid_row

    if grid_row*grid_column > size:
        grid_column -= 1
    if grid_row*grid_column > size:
        grid_row -= 1

    if (rank == 0):
        print("Building a %d x %d grid topology:" % (grid_row, grid_column))

    cartesian_communicator = comm.Create_cart(
        (grid_row, grid_column), 
        periods=(True, True), reorder=True)
    
    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)

    neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)

    # --- Matrix Multiplication Logic ---
    # Each process starts with its own local 2x2 matrices
    # We use the rank and coordinates to make the data unique
    matrix_a = [[rank, rank + 1], [rank + 2, rank + 3]]
    matrix_b = [[1, 0], [0, 1]] # Using identity for easy checking
    result = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    print ("Process = %s row = %s column = %s" % (rank, my_mpi_row, my_mpi_col))
    print ("Multiplication Result at this node: %s" % result)
    print ("----> neighbour_processes[UP] = %s, DOWN = %s, LEFT = %s, RIGHT = %s\n" 
           % (neighbour_processes[UP], neighbour_processes[DOWN], 
              neighbour_processes[LEFT], neighbour_processes[RIGHT]))