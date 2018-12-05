# Day 1: Chronal Calibration #
import numpy as np
import pandas as pd
df = pd.read_table("input1.txt", header=None)

# Part 1
print(df.sum(axis=0))

# Part 2
dict = {}
sum = 0
flag = False
while True:
    for index, row in df.iterrows():
        sum += row[0]
        if sum not in dict:
            dict[sum] = 1
        else:
            print(sum)
            flag = True
            break
    if flag: break
