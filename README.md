Python Concurrency Demo
Explore how to use multithreading and multiprocessing in Python, complete with performance comparisons for I/O-bound vs CPU-bound tasks.

🧩 What's Inside
🔹 Multithreading

Uses ThreadPoolExecutor from concurrent.futures to run lightweight threads within a single process

Ideal for I/O-bound operations like file reads or web requests

Threads share memory but are limited by Python’s Global Interpreter Lock (GIL), meaning only one thread runs bytecode at any moment 
reddit.com
+5
medium.com
+5
stackoverflow.com
+5
geeksforgeeks.org
+4
docs.python.org
+4
stackoverflow.com
+4
digitalocean.com
+1
geeksforgeeks.org
+1
stackoverflow.com

⚙️ Multiprocessing

Leveraging multiprocessing.Pool, this module spawns separate processes, each with its own Python interpreter and memory space

Enables true parallel execution across multiple CPU cores—perfect for compute-heavy tasks 
geeksforgeeks.org
+3
medium.com
+3
reddit.com
+3

📊 Included in This Repo
Runnable examples using ThreadPoolExecutor and multiprocessing.Pool

Benchmark scripts comparing threading vs processing across I/O-heavy and CPU-heavy workloads

Guidelines on when to choose threads (I/O tasks) vs processes (CPU tasks)

🚀 How to Use
bash
Copy
Edit
git clone https://github.com/yourusername/your-repo
cd your-repo

# Install dependencies
pip install -r requirements.txt

# Run I/O-bound example
python io_thread_example.py

# Run CPU-bound benchmark
python cpu_process_benchmark.py
✅ Key Takeaways
Scenario	Best Approach	Why
I/O-bound tasks	Multithreading	Overlaps waiting time, plus thread pooling reduces overhead 
youtube.com
+9
digitalocean.com
+9
geeksforgeeks.org
+9
turing.com
+10
medium.com
+10
geeksforgeeks.org
+10
CPU-bound tasks	Multiprocessing	Bypasses GIL and utilizes multiple cores for real parallelism

📚 Learn More
[StackOverflow discussion on threading vs multiprocessing in Python]
stackoverflow.com
+12
stackoverflow.com
+12
discuss.python.org
+12

[GeeksforGeeks comparison guide]
en.wikipedia.org
+3
geeksforgeeks.org
+3
geeksforgeeks.org
+3

Official docs: [concurrent.futures.ThreadPoolExecutor, multiprocessing.Pool]
