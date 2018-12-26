# Day 12: Subterranean Sustainability
#
# Wanted to see if the pattern ended up repeating / approaches a
# constant value. However, I ran out of space on the screen to display
# each generation.
#
# Solution2.py resolves this issue by keeping track of the distance of
# the first plant from the origin (0th pot) and dynamically extending the
# current pot array to display only the relevant sections.

import math
from collections import deque

# Processing data
init = 0
patterns = {}
data = open("input","r")
for line in data:
    if init == 0:
        state = line.split()[2]
    elif init != 1:
        tmp =  line.split()
        patterns[tmp[0]] = tmp[2]
    init += 1

# Part 1
rowlength = 150
potarray = "."*rowlength
potzero = (rowlength - len(state))/2
potarray = potarray[:potzero] + state + potarray[potzero+len(state):]
print " 0:", potarray

#for generation in range(1,21):
for generation in range(1,20): #50000000000):
    toreplace = deque()
    indices = deque()

    for indi in range(rowlength - 4):
        sample = potarray[indi:indi+5]

        for key in patterns:
            if sample == key:
                #print "sample:", sample, "key:", key
                toreplace.append(key)
                indices.append(indi)
                #print "replacing at pos", indi

    for cnt in range(len(toreplace)):
        replacer = toreplace.popleft()
        indexer = indices.popleft()
        potarray = potarray[:indexer+2] + patterns[replacer] + potarray[indexer+3:]
        # abdZZXZZda
        # 0123456789
        # -----56---
    if generation < 10:
        print " " + str(generation) + ":", potarray
    else:
        print str(generation) + ":", potarray
    #if generation % 10000000 == 0:
    #    print "finished generation", generation
sum = 0
for countr in range(len(potarray)):
    if potarray[countr] == "#":
        sum += countr - potzero
print "Solution to part 1:", sum
