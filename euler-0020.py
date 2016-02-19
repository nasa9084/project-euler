# -*- coding: utf-8 -*-
"""Project Euler problem 20"""

from math import factorial as fact
from euler import get_digit_sum

print("Answer: " + str(get_digit_sum(fact(100))))
