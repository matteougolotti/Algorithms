# Returns greatest common divisor of a and b
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a