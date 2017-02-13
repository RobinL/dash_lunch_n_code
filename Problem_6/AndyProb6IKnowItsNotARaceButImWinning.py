def sumSq(x):
	return int(x*(x+1)*(2*x+1)/6);
	

def sqSum(x):
	return int((x*(x+1)/2)**2);

print(sqSum(100)-sumSq(100))