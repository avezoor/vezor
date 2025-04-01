def isPrime(n):
    if not isinstance(n, int) or n <= 0:
        print("Warning: Please enter a positive integer.")
        return False
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
