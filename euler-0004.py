# -*- coding:utf-8 -*-
"""Project Euler problem 4"""

a = 999
b = 999

palindromes = {}

while a!=99:
    x = str(a * b)
    boo=1
    for i in range(len(x)//2):
        if x[i]!=x[-1-i]:
            boo=0
            break
    if boo==1:
        palindromes[int(x)] = str(a)+"*"+str(b)
    if b>=100:
        b -= 1
    elif b==99:
        b = a
        a -=1
print("Answer: " + str(max(palindromes.values())) + "=" + str(max(palindromes)))
