# -*- coding:utf-8 -*-
"""Project Euler problem 31"""
def count(tg, coins):
    if len(coins)==0:
        return 1
    else:
        sm = 0
        coin = coins[0]
        q = (tg//coin)+1
        for i in range(q):
            sm += count(tg -coin*i, coins[1:])
        return sm

print("Answer: " + str(count(200, [200,100,50,20,10,5,2])))
