def prime_list(num):
    primes = [True] * (num + 1)
    primes[0] = primes[1] = False  

    for p in range(2, int(num**0.5) + 1):
        if primes[p]:
            for i in range(p * p, num + 1, p):
                primes[i] = False

    prime_numbers = [i for i, is_prime in enumerate(primes) if is_prime]
    print(f"Prime numbers up to {num}: {prime_numbers}")