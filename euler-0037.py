# -*- coding:utf-8 -*-
"""Project Euler problem 37"""

from euler import get_plist

primes = get_plist(1000000)
primesset = set(primes)
sm = 0
for p in primes:
    if p<10: continue
    for i in range(len(str(p))):
        if not int(str(p)[i:]) in primesset:
            break
    else:
        for i in range(len(str(p))-1):
            if not int(str(p)[:-i-1]) in primesset:
                       break
        else:
            sm += p
print("Answer: " + str(sm))
