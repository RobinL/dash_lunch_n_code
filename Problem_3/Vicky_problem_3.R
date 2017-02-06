install.packages('gmp')

require(gmp)

n <- 600851475143

v <- factorize(n)
print(v)
max(v)
