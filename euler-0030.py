# -*- coding:utf-8 -*-
"""Project Euler problem 30"""
ls = []
for i in range(2,999999):
    s = str(i)
    sm = sum([int(p)**5 for p in s])
    if i==sm:
        ls.append(i)
print("Answer: " + str(sum(ls)))
