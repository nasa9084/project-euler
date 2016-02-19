# -*- coding:utf-8 -*-
"""Project Euler problem 47"""

from euler import get_plist
def getPrimeFactor(x, primes):
    pf = []
    mx = x/2+1
    for i in primes:
        if mx<i:
            break
        if x!=1:
            if x%i==0:
                x/=i
                pf.append(i)
    return pf

mx = 10**6
primes = get_plist(mx)
chk = 4
fst = 0
cnt = 0
print(getPrimeFactor(14, primes))
for i in range(mx):
    pf = set(getPrimeFactor(i, primes))
    if len(pf)==chk:
        if cnt==0:
            fst = i
        cnt += 1
        print(" "*cnt, i, cnt, list(sorted(list(pf)))) if cnt!=0 else ""
        if cnt==chk:
            break
    else:
        cnt = 0
print("Answer: " + str(fst))
