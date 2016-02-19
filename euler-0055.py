# -*- coding:utf-8 -*-
"""Project Euler problem 55"""
from euler import is_palindrome


c = 0
for i in range(10000):
    p = i
    for j in range(50):
        p = p + int(str(p)[::-1])
        if is_palindrome(p):
            break
    else:
        c += 1
print("Answer: " + str(c))
