# -*- coding:utf-8 -*-
"""Project Euler problem 23"""
def getAbundantList(n):
    ls = []
    ladd = ls.append
    for i in range(2,n):
        divisors = []
        dadd = divisors.append
        for j in range(1,i):
            if i%j==0:
                dadd(j)
        if sum(divisors)>i:
            ladd(i)
    return ls

abu = set(getAbundantList(28123))
abusum = set([x+y for x in abu for y in abu])
sum = 0
for i in range(28123):
    if not i in abusum:
        sum += i
print("Answer: " + str(sum))
