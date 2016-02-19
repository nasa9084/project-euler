# -*- coding: utf-8 -*-
"""Project Euler problem 79"""

patterns = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716""".split("\n")
password = []
for pattern in patterns:
    pattern = [int(c) for c in pattern]
    for i in range(3):
        if not pattern[i] in password:
            password.append(pattern[i])
    while True:
        fst = password.index(pattern[0])
        snd = password.index(pattern[1])
        thd = password.index(pattern[2])
        if fst>snd:
            password[fst], password[snd] = password[snd], password[fst]
            continue
        if snd>thd:
            password[snd], password[thd] = password[thd], password[snd]
            continue
        break
print("Answer: " + str("".join([str(i) for i in password])))
