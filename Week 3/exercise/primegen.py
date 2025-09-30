def prime_generator():
    """Yield prime numbers indefinitely."""
    primes = []
    num = 2
    while True:
        if all(num % p != 0 for p in primes):
            primes.append(num)
            yield num
        num += 1

# Example usage
gen = prime_generator()
for _ in range(10):
    print(next(gen), end=" ")
