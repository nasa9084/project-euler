# -*- coding:utf-8 -*-
"""Project Euler problem 7"""

from euler import get_plist

target = 10000
l = 10**6
while True:
    primes = get_plist(l)
    if len(primes)>=target: break
print("Answer: " + str(primes[target]))
