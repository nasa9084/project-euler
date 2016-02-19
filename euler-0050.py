# -*- coding:utf-8 -*-
"""Project Euler problem 50"""
from euler import get_plist

target = 10**6
primes = get_plist(target)
primesset = set(primes)

mx, ans =  0, 0
for l in range(len(primes)):
    for r in range(l+1,len(primes)):
        sm = sum(primes[l:r+1])
        if sm>target: break
        length = (r+1)-l
        if sm in primesset and mx<length:
            ans = sm
            mx = length

print("Answer: " + str(ans))
