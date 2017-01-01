import fractions

# Euler's totient function
# Counts the positive integers 
#up to a given integer n 
# that are relatively prime to n
def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount