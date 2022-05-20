# returns whether b evenly divides into a
def isDivisible(a,b):
    if b == 0:
        return False
    return a % b == 0

# returns whether n is prime or not.
def isPrime(n):
    if n != 2 and n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True