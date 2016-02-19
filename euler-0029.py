# -*- coding:utf-8 -*-
"""Project Euler problem 29"""

ls = []
add = ls.append
import sys
argv = sys.argv
argc = len(argv)
if not argc==3:
    print("Usage: python {} <int from> <int to>\n".format(argv[0]))
    quit()
else:
    frm = int(argv[1])
    to = int(argv[2])
    for a in range(frm, to+1):
        for b in range(frm, to+1):
            add(a**b)

    print("Answer: " + str(len(list(set(ls)))))
