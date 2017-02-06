threes = []
for i in range(334):
	threes.append(3*i)

fives = []
for i in range(200):
	if i%3!=0:
		fives.append(5*i)

t = sum(threes)
f=sum(fives)


print (t+f)