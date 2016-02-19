# -*- coding:utf-8 -*-
"""Project Euler problem 44"""

def getPentanums(n):
    pnums = []
    for i in range(1, n+1):
        pnums.append(i*(3*i-1)//2)
    return pnums

rg = 10000
pnums = getPentanums(rg)
pnumsset = set(pnums)
for i in range(rg):
    for j in range(i+1, rg):
        s = pnums[i] + pnums[j]
        d = pnums[j] - pnums[i]
        if s in pnumsset and d in pnumsset:
            print("Answer: " + str(d))
            quit()
