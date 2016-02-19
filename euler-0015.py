# -*- coding:utf-8 -*-
"""Project Euler problem 15"""

from math import factorial as fact

w = 20
h = 20

print("Answer: " + str(int(fact(w+h)/(fact(w)*fact(h)))))
