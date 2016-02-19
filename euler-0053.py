# -*- coding:utf-8 -*-
"""Project Euler problem 53"""
from math import factorial as fact
target = 10**6
count = 0
res = []
re = 1
for i in range(1, 101):
    re *= i
    res.append(re)
ne = 1
for n in range(1, 101):
    print(n)
    ne *= n
    for r in range(1, n):
        c = ne/(res[r-1]*fact(n-r))
        if c>=target: count += 1
print("Answer: " + str(count))
