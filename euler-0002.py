# -*- coding:utf-8 -*-
"""Project Euler problem 2"""

def fib(a, b):
    return a+b

a = 1
b = 2

sm = 2

while True:
    tmp = fib(a, b)
    sm += tmp if tmp%2==0 else 0
    a = b
    b = tmp
    if tmp>4000000:
        break

print("Answer: " + str(sm))
