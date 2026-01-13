# Distributed Systems (Celery, Pyro4, Sockets) - Python Examples

## Overview
This folder covers **Distributed Computing Architecture**, demonstrating how different machines or processes can work together using **Task Queues (Celery)**, **Remote Objects (Pyro4)**, and **Direct Networking (Sockets)**.

It provides hands-on examples of the **Client-Server model**, where a server hosts a resource or service and one or more clients connect to it over a network to perform tasks or retrieve data.

---

## How It Works
- The **Client-Server model** allows clients to request services and servers to process requests concurrently.  
- **Celery** is used for asynchronous task execution in the background via a task queue.  
- **Pyro4** allows Python objects to be accessed remotely, making remote method calls appear local.  
- **Sockets** implement direct networking using TCP/IP, giving full control over data transfer but requiring manual handling.

---

## File Overview

### Celery Folder
- `addTask.py`  
  Defines a background task to be executed asynchronously.  

- `addTask_main.py`  
  Sends the task to a worker queue for execution.

### Pyro4 Folder (Python Remote Objects)
- `pyro_server.py`  
  Makes a Python object accessible over the network.  

- `pyro_client.py`  
  Calls methods on the remote object as if it were local.  

- `chainTopology.py`  
  Demonstrates a "Chain" topology where one server calls another to complete a request.

### Socket Folder
- `server.py` & `client.py`  
  Implements basic TCP/IP networking to send strings or files between programs.  

- `addTask.py` (Socket)  
  Implements logic (e.g., addition) over a raw network connection.

---

## Observations
- **Celery** is ideal for heavy background jobs and asynchronous processing.  
- **Pyro4** provides an easy way to make Python applications communicate across the network.  
- **Sockets** offer the most control but require manual data handling and networking knowledge.

---

## Dependencies
- Python 3.x  
- **Celery**: `pip install celery`  
- **Pyro4**: `pip install Pyro4`  
- A **broker** (e.g., Redis or RabbitMQ) is required for Celery task queues.

---

## Usage
- **Celery Tasks**: Start a Celery worker and run the main script:
```bash
celery -A addTask worker --loglevel=info
python addTask_main.py


Pyro4 Remote Objects: Run the server, then the client:
python pyro_server.py
python pyro_client.py

Socket Programs: Run the server first, then the client:
python server.py
python client.py
