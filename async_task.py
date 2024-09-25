import asyncio


async def async_write_to_file(filename, data, duration):
    """Simulate writing data to a file asynchronously."""
    print(f"Writing to {filename} asynchronously...")
    await asyncio.sleep(duration)
    with open(filename, 'w') as f:
        f.write(data)
    print(f"Finished writing to {filename}")

async def run_async_tasks(primes):
    """Run multiple async file writing tasks for prime numbers."""
    chunk_size = len(primes) // 5
    tasks = []
    
    for i in range(5):
        chunk = primes[i * chunk_size: (i + 1) * chunk_size]
        primes_data = '\n'.join(map(str, chunk))
        tasks.append(async_write_to_file(f"primenumbers{i}.txt", primes_data, 1))
    
    await asyncio.gather(*tasks)
