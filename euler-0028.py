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

import sys
argv = sys.argv
argc = len(argv)
if argc>3:
    print("Usage: python {} [rev|size] <int>\n".format(argv[0]))
    quit()
elif argc==2:
    rev = int(argv[1])
elif argc==3:
    if argv[1]=="rev":
        rev = int(argv[1])
    elif argv[1]=="size":
        size = int(argv[2])
        rev = (size+1)/2
    else:
        print("Usage: python {} [rev|size] <int>\n".format(argv[0]))
        quit()
print("Answer: " + str(spiral(rev)))
