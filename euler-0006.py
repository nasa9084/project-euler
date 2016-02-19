# -*- coding:utf-8 -*-
"""Project Euler problem 6"""

sum_of_squares = squares_of_sum = 0

for i in range(100):
    sum_of_squares += (i+1)**2
    squares_of_sum += (i+1)

print("Answer: " + str(squares_of_sum **2 - sum_of_squares))
