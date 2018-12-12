# Day 11: Chronal Charge
import pandas as pd
import numpy as np

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
sums = pd.DataFrame(np.zeros((298,298))).astype(int)
for y in range(powers.shape[0] - 2):
    for x in range(powers.shape[1] - 2):
        pass
        sums.iat[y,x] = powers.iloc[y:y+3, x:x+3].sum().sum()

pmax = sums[sums == sums.max().max()].dropna(axis=0, how="all").dropna(axis=1, how="all")
print "Solution to part 1:", pmax.columns[0]+1, ",", pmax.index[0]+1

# Part 2
