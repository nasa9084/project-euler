# -*- coding:utf-8 -*-
"""Project Euler problem 46"""

from euler import get_plist, is_primes

mx = 10**6
primes = set(get_plist(mx))
ans = 0
for odd in range(9, mx, 2):
    if odd in primes:
        continue
    flg = True

    for j in [i*i*2 for i in range(int((mx**0.5)/2)+1)]:
        if j>=odd: break

        if is_prime(odd-j,  primes):
            flg = False
            break
    if flg:
        ans = odd
        break
print("Answer: " + str(ans))
