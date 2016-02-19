# -*- coding:utf-8 -*-
"""Project Euler problem 27"""
from euler import get_plist

class Answer:
    def __init__(self):
        self.a = 0
        self.b = 0
    def setval(self, a,b):
        self.a = a
        self.b = b
    def get(self):
        return self.a*self.b

def quad(n, a, b):
    return n*n + a*n + b

longest = 0
ans = Answer()
primes = set(get_plist(100000))
for a in range(-1000, 1001):
    if a%2==0: continue
    for b in range(-1000, 1001):
        if not abs(b) in primes: continue
        n = 0
        while quad(n, a, b) in primes:
            n += 1
        if n > longest:
            longest = n
            ans.setval(a,b)
print("Answer: " + str(ans.get()))
