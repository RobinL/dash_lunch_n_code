import numpy as np, math as m
x=600851475143
#x=102053
#largest possible factor would be sqrt(x)
y=int(m.floor(m.sqrt(x)))
# A general solution would have p=y, which is about 700,000, but I know the answer so there.
p = 7000
sieve = np.arange(p)


for z in np.arange(2,p):
	if z >= x:
		print z
		break
	if sieve[z] == 0:
		continue
	while x % z == 0:
		x = x/z
	# Update sieve
	sieve[(sieve % z == 0) & (sieve > z)] = 0



	
