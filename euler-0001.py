# -*- coding:utf-8 -*-
"""Project Euler problem 1"""

sum = 0
for i in range(1000):
    if i%3==0 or i%5==0:
        sum += i
print("Answer: " + str(sum))
