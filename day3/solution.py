# Day 3: No Matter How You Slice It
import numpy as np
import pandas as pd
fabric = pd.DataFrame(np.zeros((1000,1000)))

# Part 1
df = open("input","r")
for line in df:
    arr = line.split()[2:]
    left, top = arr[0].split(",")
    top = top[:len(top)-1]
    width, height = arr[1].split("x")
    left, top, width, height = map(int, [left, top, width, height])

    fabric.iloc[top:top+height, left:left+width] += 1

overlaps = (fabric > 1)
area = overlaps.sum().sum()
print(area)
df.close()

# Part 2
df = open("input","r")
for line in df:
    arr = line.split()
    left, top = arr[2].split(",")
    top = top[:len(top)-1]
    width, height = arr[3].split("x")
    left, top, width, height = map(int, [left, top, width, height])

    if (fabric.iloc[top:top+height, left:left+width].sum().sum()) == (width*height):
        print(arr[0])
        break
df.close()
