# Day 2: Inventory Management System
import numpy as np
import pandas as pd
df = pd.read_table("input", header=None)

# Part 1
twos = 0
threes = 0
for index, row in df.iterrows():
    dict = {}
    istwo = False
    isthree = False
    for char in row[0]:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for key in dict:
        if dict[key] == 2:
            istwo = True
        elif dict[key] == 3:
            isthree = True
    if istwo:
        twos += 1
    if isthree:
        threes += 1
checksum = twos*threes
print(checksum)

# Part 2
def numdiff(str1,str2):
    diff = 0
    diffletter = []
    for n in range(len(str1)):
        if str1[n] != str2[n]:
            diff += 1
            diffletter.append(str2[n])
    return diff, diffletter

flag = False
for x in range(df.size):
    if ((249-x) == -1) or flag:
        break
    for y in range(249-x):
        diff, diffletter = numdiff(df.iloc[x,0], df.iloc[y,0])
        if diff == 1:
            reqletters = ""
            for letter in df.iloc[y,0]:
                if letter != diffletter[0]:
                    reqletters += letter
            flag = True
            break
print(reqletters)
