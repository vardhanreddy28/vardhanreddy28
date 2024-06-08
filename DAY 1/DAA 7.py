def isprime(n, divisor=None):
    if n<=1:
        return False
    if divisor is None:
        divisor=n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return isprime(n,divisor-1)
def generateprimes(n,current=2,primes=None):
    if primes is None:
        primes=[]
    if current>n:
        return primes
    if isprime(current):
        primes.append(current)
    return generateprimes(n,current+1,primes)
limit = 30
primes = generateprimes(limit)
print(f"Prime numbers up to {limit}:",primes)
