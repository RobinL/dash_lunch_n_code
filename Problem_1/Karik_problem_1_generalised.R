# Generalised Problem 1

N <- 999
myNumbers <- c(3,5)

allNumbers <- 1:N


allNumbersLong <- rep(allNumbers, length(myNumbers))
tests <- allNumbersLong %% rep(myNumbers, each = length(allNumbers)) == 0

sum(unique(allNumbersLong[tests]))

