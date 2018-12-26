# Day 12: Subterranean Sustainability
#
# The pattern does indeed repeat after around 97 iterations.
# However, the patterns keeps shifting to the right. Since it shifts
# by a constant number of pots, the difference in sum can be computed
# and extrapolated to 50 million generations.

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

# Initializing relevant variables
firstpot = 0
prevsum = 0
diffcounter = 0
diff = 0
potarray = "...." + state + "...."
print " 0:", potarray, "first pot:", firstpot

def prune(arr, pos):
    ind = arr.find("#")
    rind = arr.rfind("#")
    arr = "...." + arr[ind:rind+1] + "...."
    pos += (ind - 4)
    return arr, pos

for generation in range(1,300):
    toreplace = deque()
    indices = deque()

    for indi in range(len(potarray) - 4):
        sample = potarray[indi:indi+5]

        for key in patterns:
            if sample == key:
                toreplace.append(key)
                indices.append(indi)

    for cnt in range(len(toreplace)):
        replacer = toreplace.popleft()
        indexer = indices.popleft()
        potarray = potarray[:indexer+2] + patterns[replacer] + potarray[indexer+3:]

    potarray, firstpot = prune(potarray, firstpot)

    sum = 0
    for countr in range(len(potarray)):
        if potarray[countr] == "#":
           sum += countr + firstpot - 4

    newdiff = sum - prevsum
    prevsum = sum

    # Print the result of each generation for debugging
    if generation < 10:
        print " " + str(generation) + ":", potarray
    else:
        print str(generation) + ":", potarray
    print "sum:", sum, "diff:", diff

    # Part 1
    if generation == 20:
        sum20 = sum

    # Part 2
    if (newdiff - diff) == 0:
        diffcounter += 1
    else:
        diffcounter = 0
    diff = newdiff

    if diffcounter == 5:
        sum5m = sum + ((50000000000 - generation)*diff)
        break


print "\nSolution to part 1:", sum20
print "Solution to part 2:", sum5m
