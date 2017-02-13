#test post please ignore
import numpy as np
def isPal(x):
	return str(x)==str(x)[::-1];

thou = np.arange(100,1000)
pals = []
for i in thou:
	for j in np.arange(i+1,1000):
		if(isPal(i*j)):
			pals.append(i*j)

print(max(pals))