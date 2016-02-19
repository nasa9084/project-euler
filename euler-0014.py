# -*- coding:utf-8 -*-
"""Project Euler problem 14"""
mxlen = 0
mx = 0
target = 10**6
for i in range(1, target):
    ls = []
    t = i
    while t!=1:
        ls.append(t)
        t = t/2 if t%2==0 else 3*t+1
    if mxlen<len(ls):
        mx = i
        mxlen = len(ls)
print("Answer: " + str(mx))
