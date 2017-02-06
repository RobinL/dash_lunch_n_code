
# EXERCISE 2
len <- 100 # I don't like this - not sure on creating new vectors
fibvals <- numeric(len)
fibvals[1] <- 1
fibvals[2] <- 1
for (i in 3:NROW(fibvals)) { 
  fibvals[i] <- fibvals[i-1]+fibvals[i-2]
  currentmax <- max(fibvals)
  if (currentmax >= 4000000) break
} 

# Find the even numbers only
is.even <- function(x) x %% 2 == 0
evens <- fibvals[is.even(fibvals)==TRUE]

# Add them up
sum(evens)
