def gcd2(m, n):
    while n:
        m, n = n, m % n
    print(f"Greatest Common Divisor is {m}")