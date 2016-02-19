# -*- coding:utf-8 -*-
"""Project Euler problem 10"""
from euler import get_plist

sm = 0
primes = get_plist(2000000)

for i in primes:
	sm += i

print("Answer: " + str(sm))
