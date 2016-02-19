# -*- coding: utf-8 -*-
"""Project Euler problem 21"""

from euler import get_flist

s = set()
for i in range(1,10000):
    sfi = sum(get_flist(i)[:-1])
    sfsfi = sum(get_flist(sfi)[:-1])
    if sfi!=i and sfsfi==i:
        s.add(i)
        s.add(sfi)
print("Answer: " + str(sum(s)))
