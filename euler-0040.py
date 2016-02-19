# -*- coding:utf-8 -*-
"""Project Euler problem 40"""

s = ""
l = 0
i = 0
while l<1000000:
    t = str(i)
    s += t
    l += len(t)
    i += 1
ans = 1
for i in range(6):
    ans *= int(s[10**i])
print("Answer: " + str(ans))
