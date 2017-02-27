import numpy as np
sievemax=500000
sieve=np.ones(sievemax)
primes=[]
i=2

while len(primes) <10001:
    if sieve[i]==1:
        primes.append(i)
        for x in range(i**2,sievemax,i):
            sieve[x]=0
    i=i+1
primes[10000]
