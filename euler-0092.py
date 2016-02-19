# -*- coding: utf-8 -*-
"""Project Euler problem 92"""
def sumSq(n):
    if n<10:
        return n**2
    else:
        return sum([int(c)**2 for c in str(n)])

c = 0
for i in range(1, 10000000):
    print(i)
    while True:
        i = sumSq(i)
        if i==89:
            c += 1
            break
        elif i==1:
            break
print("Answer: " + str(c))
