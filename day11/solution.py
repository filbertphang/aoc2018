# Day 11: Chronal Charge
import pandas as pd
import numpy as np
import time

Tstart = time.time()
# This was my puzzle input
serial = 7672

powers = pd.DataFrame(np.zeros((300,300))).astype(int)
for y in range(powers.shape[0]):
    for x in range(powers.shape[1]):
        id = x + 11
        pow = ((id * (y + 1)) + serial) * id
        if pow > 99:
            pow = int(str(pow)[-3])
        else:
            pow = 0
        pow -= 5
        powers.iat[y,x] = pow

# Part 1
# Naive implementation used because I first solved this part
# without knowing about Kadane's Algorithm
# Solution takes around 45 seconds to run
sums = pd.DataFrame(np.zeros((298,298))).astype(int)
for y in range(powers.shape[0] - 2):
    for x in range(powers.shape[1] - 2):
        sums.iat[y,x] = powers.iloc[y:y+3, x:x+3].sum().sum()

pmax = sums[sums == sums.max().max()].dropna(axis=0, how="all").dropna(axis=1, how="all")
print "Solution to part 1:", str(pmax.columns[0]+1) + "," + str(pmax.index[0]+1)

Tend1 = time.time()
print "Time elapsed for part 1:", (Tend1 - Tstart)

# Part 2
# Unfortunately had to brute force / use naive implementation to solve
# because I couldn't understand how 2D Kadane's Algorithm worked
# Solution to this part took 4922 seconds, or roughly 82 mins to run
curmax = -99999
curindex = [0,0]
cursize = 0
for size in range(1, 300):
    sums = sums = pd.DataFrame(np.zeros((300-size,300-size))).astype(int)
    for y in range(powers.shape[0] - size):
        for x in range(powers.shape[1] - size):
            sums.iat[y,x] = powers.iloc[y:y+size+1, x:x+size+1].sum().sum()

    pmax = sums[sums == sums.max().max()].dropna(axis=0, how="all").dropna(axis=1, how="all")
    if (pmax.shape == (1,1)) and max(curmax, pmax.iat[0,0]) != curmax:
        curmax = pmax.iat[0,0]
        curindex = [pmax.columns[0]+1, pmax.index[0]+1]
        cursize = size + 1

    print "Done with size", size

print "Solution to part 2:", str(curindex[0]) + "," + str(curindex[1]) + ","+str(cursize)
Tend2 = time.time()
print "Time elapsed for part 2:", (Tend2-Tstart)
