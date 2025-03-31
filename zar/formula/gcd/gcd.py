def gcd(m, n):
    for _ in range(min(m, n)):  
        if n == 0:
            break
        m, n = n, m % n
    print(f"Greatest Common Divisor is {m}")