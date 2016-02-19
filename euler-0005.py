# -*- coding:utf-8 -*-
"""Project Euler problem 5"""

x = a = 2*3*5*7*11*13
while True:
    boo = 1
    for i in range(3, 20):
        if x%(i+1)!=0:
            boo = 0
            break
    if boo==1:
        break
    else:
        x += a
print("Answer: " + str(x))
