def count_primes(n):
    if n < 2:
        return 0

    # Create a boolean array to mark prime numbers
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Use the Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Count the number of prime numbers
    prime_count = sum(is_prime)
    return prime_count

# Example usage
n = 75
print(f"The number of prime numbers up to {n} is: {count_primes(n)}")
