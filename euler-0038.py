# -*- coding:utf-8 -*-
"""Project Euler problem 38"""
def isPandigital(n):
    if type(n) == int:
        n = str(n)
    return "".join([str(y) for y in list(sorted([int(x) for x in n]))]) == "123456789"

i = 0
mx = 0
while i<10000:
    n = ""
    for j in range(1,10):
        m = i*j
        n += str(m)
        if j==1:
            continue
        elif len(n)==9:
            if isPandigital(n):
                if mx < int(n):
                    mx = int(n)
        elif len(n)>9:
            break
    i += 1
print("Answer: " + str(mx))
