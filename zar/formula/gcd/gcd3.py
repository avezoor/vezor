def gcd3(m, n):
    d = min(m, n)
    
    for i in range(d, 0, -1):  
        if m % i == 0 and n % i == 0:
            print(f"Greatest Common Divisor is {i}")
            return