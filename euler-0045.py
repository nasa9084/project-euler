# -*- coding:utf-8 -*-
"""Project Euler problem 45"""

from euler import is_penta

i = 144
while True:
    Hn = i*(2*i-1)
    if is_penta(Hn):
        print("Answer: " + str(Hn))
        break
    i+=1
