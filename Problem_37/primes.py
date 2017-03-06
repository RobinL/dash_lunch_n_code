#!/usr/bin/env python3

import math


def primes(n, verbose=False):
    '''Return primes to n using Eratosthenes Sieve'''
    sqrtN = math.sqrt(n)
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    i = 1
    while i < sqrtN:
        if primes[i]:
            j = i * 2
            while j < n:
                primes[j] = False
                j = j + i
        i += 1

    if verbose:
        for i in range(len(primes)):
            if primes[i]:
                print("%d, " % i, end="")
                print('')

    return [i for i, x in enumerate(primes) if x]


def circular(n):
    '''return a list of circular numbers of n'''
    s = str(n)
    lst = []
    while s not in lst:
        lst.append(s)
        s = s[-1] + s[:-1]

    return [int(i) for i in lst]

if __name__ == '__main__':
    c_primes = []
    # If you leave some_primes as a list this is a lot slower!
    some_primes = set(primes(1000000))
    for p in some_primes:
        c = circular(p)
        if set(c).issubset(some_primes):
            c_primes.append(p)

    print(c_primes)
    print(len(c_primes))
