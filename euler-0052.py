# -*- coding:utf-8 -*-
"""Project Euler problem 52"""
from itertools import permutations as p

for i in range(1, 10**6):
    pat = [int("".join(s)) for s in p(str(i))]
    for j in range(2, 7):
        if not i*j in pat: break
    else:
        print("Answer: " + str(i))
        quit()
