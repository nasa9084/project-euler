# -*- coding: utf-8 -*-
"""Project Euler problem 65"""

from fractions import Fraction as frac
from euler import get_digit_sum

def cfrac(l):
    if len(l)==1:
        return l[0]
    else:
        return l[0] + frac(1, cfrac(l[1:]))

e = [2]
k = 1
while len(e)!=100:
    e = e + [1, 2*k, 1]
    k += 1
print("Answer: " + str(get_digit_sum(cfrac(e).numerator)))
