# -*- coding:utf-8 -*-
"""Project Euler problem 3"""

target = 600851475143

x = target
i = 2
prime_factors = []

while x>1:
    if x%i==0:
        prime_factors.append(i)
        x /= i
    else:
        i += 1

print("Answer: " + str(max(prime_factors)))
