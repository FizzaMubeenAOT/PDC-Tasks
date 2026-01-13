# Asynchronous Programming (Asyncio) - Python Examples

## Overview
This task explores **Asynchronous I/O**, a method of concurrent programming that allows a single thread to handle multiple tasks by "waiting" for I/O operations without blocking the entire execution.

Asyncio makes programs more efficient by enabling tasks to run concurrently, especially for I/O-heavy operations such as network requests or timers.

---

## How It Works
- Uses an **Event Loop** to manage "coroutines."  
- When a task is waiting (e.g., for a network response), the event loop pauses it and starts another task.  
- This allows a single thread to handle multiple tasks efficiently without blocking the program.  
- Async functions are defined using `async def` and are executed with `await` or scheduled as tasks.

---

## File Overview

- `asyncio_event_loop.py`  
  Demonstrates how to create, run, and close the central event loop that manages all tasks.

- `asyncio_coroutine.py`  
  Shows the basic syntax of `async def` and `await` to create non-blocking functions.

- `asyncio_task_manipulation.py`  
  Focuses on scheduling multiple tasks simultaneously and managing their execution states.

- `asyncio_and_futures.py`  
  Explains "Futures," which are objects representing results that haven't happened yet.

- `concurrent_futures_pooling.py`  
  Shows how to run CPU-bound tasks in a separate pool while keeping the main async loop running.

---

## Observations
- Unlike multiprocessing, Asyncio does **not use multiple CPU cores**, but is extremely efficient for tasks involving waiting (e.g., web scraping, database queries).  
- Code is cleaner and avoids the complexity of manual thread management.  
- Ideal for I/O-bound applications where tasks spend time waiting for external resources.

---

## Dependencies
- **Python 3.7+**  
- Asyncio is part of the **Python standard library**, so no external installation is required.

---

## Usage
Run any script directly using Python:

```bash
python asyncio_event_loop.py
