# Task 1: Matrix Multiplication using Multiprocessing and Multithreading 

 ## Description This task compares the performance of matrix multiplication using:

 - **Multiprocessing**
 - **Multithreading**
 
  The goal is to measure execution time for both approaches and analyze the results.

 ## ⚙️ Implementation Details
 - Programming Language: Python
 - Matrix Size: 10,000 × 10,000
 - Environment: VS Code

## 📊 Results
| Number of Processes | Multiprocessing Time (s) | Multithreading Time (s) |
|----------------------|--------------------------|--------------------------|
| 10                   | 2.27                     | 8.44                     |
| 15                   | 3.33                     | 8.95                     |
| 50                   | 3.29                     | 9.04                     |

  
 ## 🧠 Conclusion Multiprocessing performed significantly faster than multithreading for large matrix sizes, due to true parallel execution across CPU cores.