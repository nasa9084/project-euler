# -*- coding:utf-8 -*-
"""Project Euler problem 17"""
def digToStr(n):
    if n>9:
        raise Exception
    if n==1: return "one"
    elif n==2: return "two"
    elif n==3: return "three"
    elif n==4: return "four"
    elif n==5: return "five"
    elif n==6: return "six"
    elif n==7: return "seven"
    elif n==8: return "eight"
    elif n==9: return "nine"
    elif n==0: return ""

def teenToStr(n):
    if n<10 or 20<=n:
        raise Exception
    if n==10: return "ten"
    elif n==11: return "eleven"
    elif n==12: return "twelve"
    elif n==13: return "thirteen"
    elif n==14: return "fourteen"
    elif n==15: return "fifteen"
    elif n==16: return "sixteen"
    elif n==17: return "seventeen"
    elif n==18: return "eighteen"
    elif n==19: return "nineteen"

def tyToStr(n):
    if n<20 or 100<=n or n%10!=0:
        raise Exception
    if n==20: return "twenty"
    elif n==30: return "thirty"
    elif n==40: return "forty"
    elif n==50: return "fifty"
    elif n==60: return "sixty"
    elif n==70: return "seventy"
    elif n==80: return "eighty"
    elif n==90: return "ninety"


def numToStr(n):
    if n<10: return digToStr(n)
    elif 10<=n<20: return teenToStr(n)
    elif 20<=n<100: return tyToStr(n//10*10)+digToStr(n%10)
    elif 100<=n<1000 and n%100==0: return digToStr(n//100)+"hundred"
    elif 100<=n<1000 and n%100!=0: return digToStr(n//100)+"hundredand"+numToStr(n%100)
    elif n==1000: return "onethousand"

tg = 1000
ret= ""
for i in range(1, tg+1):
    s = numToStr(i)
    ret += s
print("Answer: " + str(len(ret)))
