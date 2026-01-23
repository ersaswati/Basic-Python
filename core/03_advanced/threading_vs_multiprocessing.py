"""
File: threading_vs_multiprocessing.py
Purpose:
    Demonstrate visible computation inside threading and multiprocessing
Author: Saswati Barik
Level: Advanced Python (AI Engineer)
"""

import threading
import multiprocessing
import time
import os


# ==================================================
# 🔹 Class 1: I/O-Bound Task Runner (Threading)
# ==================================================
class IOBoundTaskRunner:
    """
    Demonstrates I/O-bound tasks using threading.
    Each thread performs multiple steps to simulate
    real-world operations (API calls, file writes).
    """

    def io_task(self, task_id):
        print(f"🧵 Thread-{task_id} started")

        for step in range(1, 4):
            print(f"🧵 Thread-{task_id} | Step {step}: Waiting for I/O...")
            time.sleep(0.5)  # Simulates blocking I/O

        print(f"🧵 Thread-{task_id} completed\n")

    def run(self, num_threads=3):
        start_time = time.time()

        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=self.io_task, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("⏱️ Total I/O Threading Time:", time.time() - start_time)


# ==================================================
# 🔹 Class 2: CPU-Bound Task Runner (Multiprocessing)
# ==================================================
class CPUBoundTaskRunner:
    """
    Demonstrates CPU-intensive computation using multiprocessing.
    Each process performs heavy math inside a loop.
    """

    def cpu_task(self, process_id, n):
        print(f"⚙️ Process-{process_id} started")

        total = 0
        for i in range(1, n + 1):

            # Heavy computation
            total += i * i

            # Show progress every 25,000 iterations
            if i % 25_000 == 0:
                print(
                    f"⚙️ Process-{process_id} | "
                    f"Processed {i} iterations | "
                    f"Current Sum: {total}"
                )

        print(f"⚙️ Process-{process_id} completed\n")
        return total

    def run(self, iterations=1_00_000):
        start_time = time.time()

        cpu_cores = os.cpu_count()
        process_count = max(1, cpu_cores - 2)

        print("🧠 CPU Cores:", cpu_cores)
        print("⚙️ Processes Used:", process_count)

        with multiprocessing.Pool(processes=process_count) as pool:
            results = pool.starmap(
                self.cpu_task,
                [(i, iterations) for i in range(process_count)]
            )

        print("⏱️ Total CPU Multiprocessing Time:", time.time() - start_time)


# ==================================================
# 🔹 Main Execution
# ==================================================
if __name__ == "__main__":

    print("\n🚀 Running I/O-Bound Task (Threading)\n")
    io_runner = IOBoundTaskRunner()
    io_runner.run(num_threads=3)

    print("\n🚀 Running CPU-Bound Task (Multiprocessing)\n")
    cpu_runner = CPUBoundTaskRunner()
    cpu_runner.run(iterations=1_00_000)
