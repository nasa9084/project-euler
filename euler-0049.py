# -*- coding:utf-8 -*-
"""Project Euler problem 49"""

from itertools import permutations as p
from euler import get_plist


primes = set(get_plist(10000))
for i in range(1000, 10000):
    if i==1487: continue
    fst = i
    snd = fst + 3330
    thd = snd + 3330
    if not fst in primes or not snd in primes or not thd in primes:
        continue
    pat = set(["".join(ls) for ls in p(str(fst))])
    if str(snd) in pat and str(thd) in pat:
        break
print("Answer: " + str(fst) + str(snd) + str(thd))
