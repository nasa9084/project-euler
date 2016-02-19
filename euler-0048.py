# -*- coding:utf-8 -*-
"""Project Euler problem 48"""

sm = 0
target = 10**3
for i in range(1,target+1):
    sm += i**i
print("Answer: " + str(sm)[-10:])
