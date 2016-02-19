# -*- coding:utf-8 -*-
"""Project Euler problem 34"""
from math import factorial as fact

ans = 0
ansset = set()
for i in range(3, fact(9)*7):
    ans += i if i==sum([fact(int(x)) for x in str(i)]) else 0

print("Answer: "+ str(ans))
