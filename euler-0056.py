# -*- coding:utf-8 -*-
"""Project Euler problem 56"""
from euler import get_digit_sum

mx = 0
for a in range(1, 100):
    t = 1
    for b in range(1, 100):
        t *= a
        if get_digit_sum(t)>mx:
            mx = get_digit_sum(t)
print("Answer: " + str(mx))
