# Message Passing Interface (MPI) - Python Examples

## Overview
This folder contains Python scripts demonstrating **Distributed Memory Parallelism** using the `mpi4py` library. It showcases how multiple processes communicate by passing messages in a distributed system environment.

MPI (Message Passing Interface) enables independent processes to coordinate by sending and receiving data. Scripts are executed using an MPI runner (like `mpiexec`), which spawns multiple instances of the script that communicate via a common communicator (`COMM_WORLD`).

---

## How It Works
- Each process runs independently but can communicate with others through message passing.
- Processes are identified by a **rank** (ID) and can send/receive data from specific ranks.
- MPI supports collective operations like broadcasting, scattering, gathering, and reduction.
- Proper synchronization is essential to avoid deadlocks when processes wait on each other.

---

## File Overview

- `helloworld_MPI.py`  
  A basic script to verify the MPI environment by printing the rank (ID) of each process.

- `pointToPointCommunication.py`  
  Demonstrates direct data transfer between two specific processes (Rank 0 → Rank 1).

- `broadcast.py`  
  Shows how a single process (root) sends the same data to every other process in the group.

- `scatter.py`  
  Illustrates dividing a dataset into chunks and distributing them across all available processes.

- `gather.py`  
  Collects data chunks from all processes and combines them into one array at the root.

- `reduction.py`  
  Performs mathematical operations (like Sum or Max) across data from all processes and returns a single result.

- `alltoall.py`  
  A complex operation where every process sends and receives distinct data from every other process.

- `deadLockProblems.py`  
  An educational script showing scenarios where processes wait indefinitely, causing the program to freeze.

- `virtualTopology.py`  
  Demonstrates organizing processes into logical shapes (like a 2D grid) for specific algorithmic needs.

---

## Observations
- **Performance** improves when tasks are distributed across multiple processes, but communication overhead can slow down very small tasks.
- **Deadlocks** can occur in point-to-point communication if proper synchronization is not ensured.
- Collective operations (broadcast, scatter, gather, reduction, all-to-all) simplify communication but require all processes to participate.

---

## Dependencies
- **Python 3.x**
- **mpi4py** library
- **MPI Distribution**:  
  - Windows: MS-MPI  
  - Linux/Mac: OpenMPI

---

## Usage
To run any of the scripts, use the `mpiexec` command with the desired number of processes. For example:

```bash
mpiexec -n 4 python helloworld_MPI.py
