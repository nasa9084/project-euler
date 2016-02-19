# -*- coding:utf-8 -*-
"""Project Euler problem 39"""
mxc = 0
mxp = 0
target = 1000
ratri = []
add = ratri.append
for a in range(1, target):
    for b in range(1,target):
        c = (a**2 + b**2)**0.5
        if c<target:
            add((a,b,c))
ratri = set(ratri)
for p in range(1001):
    c = 0
    l = []
    for a in range(p//2):
        for b in range(p//2):
            if (a,b,p-a-b) in ratri:
                c += 1
                l.append((a,b,p-a-b))
    if c>mxc:
        mxp = p
        mxc = c
print("Answer: " + str(mxp))
