# Returns the list of prime factors of n (without exponent info)
def prime_factors(n):
    f = dict()
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            if not (d in f):
                f[d] = True
                factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                if not (n in f):
                    f[n] = True
                    factors.append(n)
            break
    return factors
