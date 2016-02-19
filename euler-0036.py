# -*- coding:utf-8 -*-
"""Project Euler problem 36"""
from euler import is_palindrome

sm = 0
for i in range(1000000):
    if is_palindrome(str(i)) and is_palindrome(str(bin(i))[2:]):
        sm += i
print("Answer: " + str(sm))
