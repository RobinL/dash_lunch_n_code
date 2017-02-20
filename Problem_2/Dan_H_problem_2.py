from functools import reduce

def fibonacci (max_value):
    i,j = 1,2
    fib = []
    while (i < max_value):
        fib.extend([i,j])
        i += j
        j += i
    return fib

fib_even = [x for x in fibonacci(4000000) if x % 2 == 0]
sum_even = reduce((lambda x, y: x + y), fib_even)

print(sum_even)