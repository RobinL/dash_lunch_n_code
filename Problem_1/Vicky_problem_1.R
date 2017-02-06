
# EXERCISE 1
threes <- seq(3, 999, by=3)
print(threes)

fives <- seq(5, 999, by=5)
print(fives)

all <- c(threes, fives)
uniques <- unique(all)
answer <- sum(uniques)

# Make it into a function

exercise1 = function(n) sum(unique(c(
  seq(3, n-1, by = 3), seq(5, n-1, by = 5))))

exercise1(1000) 
