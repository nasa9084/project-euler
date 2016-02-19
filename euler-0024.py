# -*- coding: utf-8 -*-
"""Project Euler problem 24"""

from itertools import permutations as P

print("Answer: " + str(list(sorted(["".join(l) for l in P("0123456789")]))[1000000-1]))
