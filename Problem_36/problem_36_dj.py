#!/usr/bin/env python3 


def is_palindrome(a):
    '''Returns true if a is palindromic'''
    s = str(a)
    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            return False
    
    return True
        

out = []

i = 0
while i < 1000000:
    if is_palindrome(i):
        b = bin(i)[2:]
        if is_palindrome(b):
            out.append(i)
    i += 1

print(sum(out))
