from prime import isPrime

numPrimes = int(input("How many primes do you want?"))

primes = [] 
n = 2
while len(primes) < numPrimes:
    if isPrime(n):
        primes.append(n)
    n += 1

with open("primes.txt","w") as f:
    for p in primes:
        f.write(str(p) + "\n")
