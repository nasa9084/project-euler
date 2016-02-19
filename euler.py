# -*- coding: utf-8 -*-
"""Module for Project Euler"""

def is_prime(n, primes=None):
    if primes is None:
        num = [True]*(n+1)
        num[0] = num[1] = False
        for i in range(2,int(n**0.5)+1):
            if num[i]:
                for j in range(i**2, n+1, i):
                    num[j] = False
        return num[n]
    else:
        return n in primes

def get_plist(mx):
    sieve = [True]*(mx//3 + int(mx%6==2))
    for i in range(1, int(mx**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1|1
            for j in range(k*k//3, len(sieve), 2*k):
                sieve[j] = False
            for j in range(k*(k-2*(i&1)+4)//3, len(sieve), 2*k):
                sieve[j] = False
    plist = [(i*3+1)|1 for i,v in enumerate(sieve) if v==True][1:]
    return [2,3] + plist

def gcd(a, b):
    if a<b:
        return gcd(b, a)
    elif b==0:
        return a
    else:
        return gcd(b, a%b)

def get_digit_sum(n):
    return sum([int(c) for c in str(n)])

def is_palindrome(n):
    if str(n)[::-1]==str(n):
        return True
    else:
        return False

def is_tri(x):
    n = ((8*x+1)**0.5+1)/2
    return int(n) == n

def is_penta(x):
    n = ((24*x+1)**0.5+1)/6
    return int(n) == n

def is_hexa(x):
    n = ((8*x+1)**0.5+1)/4
    return int(n) == n

def get_flist(n):
    factors = set()
    for f in range(1, int(n**0.5)+1):
        if n%f==0:
            factors.add(f)
            factors.add(n//f)
    return list(sorted(list(factors)))
