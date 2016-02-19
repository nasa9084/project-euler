# -*- coding: utf-8 -*-
"""Project Euler problem 243"""

from fractions import Fraction as frac
from itertools import count
from euler import get_plist

def R(d):
    return phi(d)/(d-1)

primes = get_plist(100)
target = frac(15499, 94744)
d = 1
phi = 1
for idx,p in enumerate(primes):
    d *= p
    phi *= p-1
    if frac(phi,d) < target: break
for i in count(1):
    if frac(phi*i, d*i-1)<target:
        break
print("Answer: " + str(d*i))
