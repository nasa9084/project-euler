# -*- coding:utf-8 -*-
"""Project Euler problem 9"""

for a in range(1, 1000):
    for b in range(1, 1000-a):
        c = 1000-a-b
        if a**2+b**2==c**2:
            print("Answer: " + str(a*b*c))
            quit()
