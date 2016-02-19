# -*- coding:utf-8 -*-
"""Project Euler problem 29"""

ls = []
add = ls.append

frm = 2
to = 100
for a in range(frm, to+1):
    for b in range(frm, to+1):
        add(a**b)

print("Answer: " + str(len(list(set(ls)))))
