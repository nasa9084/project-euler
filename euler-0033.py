# -*- coding:utf-8 -*-
"""Project Euler problem 33"""
from fractions import Fraction as frac

denom = 1
molec = 1

for i in range(10,100):
    for j in range(10,100):
        if i>j or i%10==0: continue
        else:
            if str(i)[0] in str(j):
                p = str(i)[1]
                q = str(j).replace(str(i)[0], "")
            elif str(i)[1] in str(j):
                p = str(i)[0]
                q = str(j).replace(str(i)[1], "")
            else: continue
            if p=="" or q=="" or p=="0" or q=="0" or p==q or int(p)>int(q): continue
            if frac(i,j)==frac(int(p), int(q)):
                denom *= int(q)
                molec *= int(p)
print("Answer: " + str(frac(molec, denom)))
