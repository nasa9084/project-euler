# -*- coding:utf-8 -*-
"""Project Euler problem 51"""

from euler import get_plist

primes = get_plist(10**6)
primesset = set(primes)
avail = []
for prime in primes:
    s = [int(d) for d in str(prime)]
    for i in range(10):
        if s.count(i) == 3:
            avail.append((prime, i))
for p in avail:
    c = 0
    for i in range(10):
        t = str(p[0]).replace(str(p[1]), str(i))
        if str(int(t))!=t:
            continue
        if int(t) in primesset:
            c+=1
            if c==8:
                print("Answer: " + str(p[0]))
                quit()
