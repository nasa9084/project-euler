# -*- coding:utf-8 -*-
"""Project Euler problem 57"""
from fractions import Fraction as frac

def expandSqrt2(n):
    ls = [frac(3,2)]
    for i in range(1, n):
        ls.append(1+frac(1,1+ls[i-1]))
    return ls

target = 1000
ls = expandSqrt2(target)
c = 0
for i in range(1000):
    sqrt2 = ls[i]
    if len(str(sqrt2.numerator))>len(str(sqrt2.denominator)):
        c += 1
print("Answer: " + str(c))
