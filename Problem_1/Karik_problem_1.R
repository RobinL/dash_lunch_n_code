# problem 1

N <- 999;

allNumbers <- 1:N
sum(allNumbers[allNumbers%%3 == 0 | allNumbers%%5 == 0])