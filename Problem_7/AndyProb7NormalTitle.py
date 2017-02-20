import numpy as np, math as m

#number of primes < N is about log N, so 10,001st prime should be around 100,000- 150,000 to be safe
sieve  = np.arange(3,150000,2)
primes = np.arange(10001)
p=0
for i in np.arange(11):
	sieve = [j for j in sieve if (j%sieve[i]>0 or j == sieve[i])]
	

	
	

print(sieve[0])

def steelyDan(x):
	prim = [True]*x
	prim[0]=False
	prim[1]=False
	root = int(m.sqrt(x))
	for i in np.arange(root):
		if prim[i]:
			j = i*2
			while j < x:
				prim[j]=False
				j=j+i
	f = np.where(prim)[0]
	return [len(f),f]
	#return [k for n in prim if prim[k]]

print(steelyDan(150000)[1][10000])

