# -*- coding:utf-8 -*-
"""Project Euler problem 32"""

from itertools import permutations as p
digits = [str(x) for x in list(range(1,10))]
ls = []
for pat in p(digits):
    for i in range(1,len(digits)-2):
        for j in range(2,len(digits)-1):
            if i==j or i>j: continue
            first = int("".join(pat[:i]))
            second = int("".join(pat[i:j]))
            ans = int("".join(pat[j:]))
            if first * second == ans:
                ls.append(ans)
print("Answer: " + str(sum(list(set(ls)))))
