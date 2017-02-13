threes = range(3, 999, 3)
# for i in range(3,999, 3):
# 	threes.append(3*i)

fives = []*200
for i in range(200):
	if i%3!=0:
		fives[i]=5*i

t = sum(threes)
f=sum(fives)


print (t+f)