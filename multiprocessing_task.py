import multiprocessing


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_chunk(numbers):
    """Check if numbers in a chunk are prime."""
    return [n for n in numbers if is_prime(n)]

def find_primes_in_range(numbers, chunk_size):
    """Split the numbers into chunks and use multiprocessing to check for primes."""
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    with multiprocessing.Pool() as pool:
        prime_chunks = pool.map(check_prime_chunk, chunks)
    return [prime for chunk in prime_chunks for prime in chunk]
