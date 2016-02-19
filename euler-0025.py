# -*- coding: utf-8 -*-
"""Project Euler problem 25"""

fiblist = []
add = fiblist.append
i = 0
while True:
    if i==0:
        add(1)
    elif i==1:
        add(1)
    else:
        fib = fiblist[i-1] + fiblist[i-2]
        if len(str(fib))==1000:
            break
        add(fib)
    i+=1

print("Answer: " + str(i+1))
