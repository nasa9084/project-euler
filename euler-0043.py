# -*- coding:utf-8 -*-
"""Project Euler problem 43"""

from itertools import permutations as P

pds = ["".join(l) for l in P([c for c in "0123456789"])]
primes = [2,3,5,7,11,13,17]
sm = 0
for pat in pds:
    for i in range(1, len("0123456789")-2):
        if not int(pat[i:i+3])%primes[i-1]==0:
            break
    else:
        sm += int(pat)
print("Answer: " + str(sm))
