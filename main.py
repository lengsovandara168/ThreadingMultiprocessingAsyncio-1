import asyncio
import multiprocessing

import async_task
import generate_numbers
import multiprocessing_task
import requests
import threading_task


def main():
    url = r'https://raw.githubusercontent.com/lengsovandara168/ThreadingMultiprocessingAsyncio/refs/heads/main/numbers.txt'
    response = requests.get(url)
    with open('numbers.txt', 'w') as file:
        file.write(response.text)

    # Step 1: Generate numbers file
    print("Generating numbers.txt file...")
    generate_numbers.generate_numbers_file("numbers.txt", 10000, 100000, 1000000)


    # Step 2: Read numbers from file
    with open("numbers.txt", "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    # Step 3: Run multiprocessing task to find primes
    print("Running multiprocessing task...")
    primes = multiprocessing_task.find_primes_in_range(numbers, chunk_size=len(numbers)//multiprocessing.cpu_count())
    print(f"Prime numbers found: {len(primes)}")

    # Step 4: Run threading task to simulate I/O
    print("Running threading I/O tasks...")
    threading_task.run_io_tasks()

    # Step 5: Run async tasks to write prime numbers to files
    print("Writing prime numbers to files asynchronously...")
    asyncio.run(async_task.run_async_tasks(primes))

if __name__ == "__main__":
    main()
