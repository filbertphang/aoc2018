# Day 6: Chronal Coordinates
# Part 2
import pandas as pd
import numpy as np
coords = pd.read_table("input", header=None, sep=',',names=["x","y"])

def total_manhattan(coordinates, point):
    sum = 0
    for line in coordinates.iterrows():
        sum += abs(line[1][0]-point[0])
        sum += abs(line[1][1]-point[1])
    return sum

distances = pd.DataFrame(np.zeros((360,360))).astype(int)

#for row in range(distances.shape[0]):
#    print "currently on row:", row
#    for column in range(distances.shape[1]):
#        distances.iat[row,column] = total_manhattan(coords, [column,row])
#distances.to_csv("distances.csv")

distances = pd.read_csv("distances.csv", index_col=0)
distances[distances<10000] = 1
print "Solution to part 2:", distances[distances<10000].sum().sum()
