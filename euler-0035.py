# -*- coding:utf-8 -*-
"""Project Euler problem 35"""
from euler import get_plist
primes = get_plist(1000000)
primesset = set(primes)
c = 0
for i in primes:
    for k in range(len(str(i))):
        n = int(str(i)[k:]+str(i)[:k])
        if not n in primesset:
            break
    else:
        c += 1

print("Answer: " + str(c))
