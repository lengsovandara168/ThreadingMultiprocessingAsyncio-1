import threading
import time


def simulate_io_task(file_name, duration):
    """Simulate a file download or I/O operation by sleeping for a duration."""
    print(f"Simulating I/O task for {file_name}")
    time.sleep(duration)
    print(f"Completed I/O task for {file_name}")

def run_io_tasks():
    """Run multiple I/O-bound tasks using threading."""
    threads = []
    for i in range(5):
        thread = threading.Thread(target=simulate_io_task, args=(f"file_{i}.txt", 2))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
