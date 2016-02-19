# -*- coding:utf-8 -*-
"""Project Euler problem 28"""

def spiral(n):
    if n==1:
        return 1
    else:
        cornersum = 0
        here = (2*(n-1)-1)**2
        for i in range(4):
            here = here + (2*n-2)
            cornersum += here
        return spiral(n-1) + cornersum


size = 1001
rev = (size+1)//2
print("Answer: " + str(spiral(rev)))
