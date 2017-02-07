import math as m
def fib(x):
	if x < 3:
		return x;
	else:
		return fib(x-1)+fib(x-2);
n = 4000000
# fib(n) tends to 1.618**n ish, so we won't need to calculate more than max
max = int(m.ceil(m.log(n,1.6)))

x = [0]*max

for i in range(max):
	if i%3==2:
		x[i]=fib(i)

print sum(x)


