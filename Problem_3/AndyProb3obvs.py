import numpy as np, math as m
x=600851475143
#x=102053
#largest possible factor would be sqrt(x)
y=int(m.floor(m.sqrt(x)))
# A general solution would have p=y, which is about 700,000, but I know the answer so there.
# Also this is super inefficient apparently.
p = 7000
sieve = np.arange(p)


for z in np.arange(2,p):
	#We build a prime sieve as we go (ish, if we put & sieve > z in the update bit we'd get a sieve)
	# - skip to next z if we've checked factors of z already
	if sieve[z] == 0:
		continue
	#If we've found a divisor, factor it out as much as we can
	while x % z == 0:
		x = x/z

	if z >= x:
		print z
		break
	# Update sieve
	sieve[(sieve % z == 0)] = 0
# If that hasn't worked, then the remains of x is greater than p, and prime, assuming p=y (proof is left to the reader)
if x>p:
	print x

	
