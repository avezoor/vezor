def gcd4(m, n):
    def __prime_factors(x):
        factors = []
        d = 2
        while d * d <= x:
            while x % d == 0:
                factors.append(d)
                x //= d
            d += 1
        if x > 1:
            factors.append(x)
        return factors

    factors_m = __prime_factors(m)
    factors_n = __prime_factors(n)
    
    common_factors = set(factors_m) & set(factors_n)
    gcd = 1
    
    for factor in common_factors:
        gcd *= factor ** min(factors_m.count(factor), factors_n.count(factor))
    
    print(f"Greatest Common Divisor is {gcd}")