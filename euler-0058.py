# -*- coding: utf-8 -*-
"""Project Euler problem 58"""
from euler import get_plist
primes = set(get_plist(1000000000))
n = 1
l = [1]
c = 0
while True:
    l = [l[0]+5+8*(n-1)] + l
    l = l + [l[-1]+1+8*(n-1)]
    p = l[-1]+n
    print(str(p)+" ", end="")
    if p in primes:
        c += 1
    p = l[-1]-n
    print(str(p)+" ", end="")
    if p in primes:
        c += 1
    p = l[0]+n
    print(str(p)+" ", end="")
    if p in primes:
        c += 1
    p = l[0]-n
    print(str(p))
    if p in primes:
        c += 1
    if c/(n*4+1)<0.1:
        print("Answer: " + str(n))
        quit()
    n+=1
