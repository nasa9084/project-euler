# -*- coding:utf-8 -*-
"""Project Euler problem 12"""

i = 1
tri = 0
while True:
    tri += i
    i += 1
    div = []
    for j in range(1, int(tri**0.5)+1):
        if tri%j==0:
            div.append(j)
            div.append(tri//j)
    if len(div)>500:
        print("Answer: " + str(tri))
        quit()
