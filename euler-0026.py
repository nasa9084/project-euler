# -*- coding:utf-8 -*-
"""Project Euler problem 26"""
mx = 0
mxd = 0
for d in range(2, 1000+1):
    tmp = d
    while d%2 == 0:
        d //= 2
    while d%5 == 0:
        d //= 5
    if d==1:
        continue
    c = 1
    while 10**c % d != 1:
        c += 1
    if c>mx:
        mxd = tmp
        mx = c
print("Answer: " + str(mxd))
