# -*- coding:utf-8 -*-
"""Project Euler problem 41"""
from euler import get_plist
from itertools import permutations


primes = set(get_plist(7654321))

for pat in reversed(sorted([int("".join(l)) for l in list(permutations([x for x in "1234567"]))])):
    if pat in primes:
        print("Answer: " + str(pat))
        break
else:
    for pat in reversed(sorted([int("".join(l)) for l in list(permutations([x for x in "1234"]))])):
        if pat in primes:
            print("Answer: " + str(pat))
            break
