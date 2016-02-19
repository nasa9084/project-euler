# -*- coding:utf-8 -*-
"""Project Euler problem 19"""
year = 1900
dayw = 1

c = 0
while year!=2001:
    for month in range(1, 13):
        if dayw==0 and year!=1900:
            c+=1
        if month in [9,4,6,11]:
            daym = 30
        elif month in [1,3,5,7,8,10,12]:
            daym = 31
        elif month==2 and ((year%4==0 and year%400!=0 and year%100==0) or year%4!=0):
            daym = 28
        elif month==2 and year%4==0:
            daym = 29
        else:
            print("?: {}".format(year))
            daym = 28
        dayw = (dayw + daym)%7
    year += 1
print("Answer: " + str(c))
