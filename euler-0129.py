# -*- coding:utf-8 -*-
"""Project Euler problem 129"""

from euler import gcd

def R(k):
    return int("1"*k)

def A(n):
    k=len(str(n))
    mod = R(k)%n
    while mod!=0:
        mod = (10*mod+1)%n
        k+=1
    return k

n = 1000000
while True:
    if gcd(n, 10)==1:
        if A(n)>1000000:
            break
    n += 1
print("Answer: " + str(n))
