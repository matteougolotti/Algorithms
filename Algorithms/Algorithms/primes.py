# Implementation of the sieve of Erathostenes for prime numbers
def primes(n):
    numbers = [True for x in range(0, n)]

    for p in range(2, n):
        if numbers[p] == True:
            i = p+p
            while i < n:
                numbers[i] = False
                i = i + p
    res = []
    for i in range(2, n):
        if numbers[i]:
            res.append(i)
    return res