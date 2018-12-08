# Day 6: Chronal Coordinates
# Part 1
import pandas as pd
import numpy as np
coords = pd.read_table("input", header=None, sep=',',names=["x","y"])

def get_shortest_dist(positions, point):
    # coordinates are given in [x,y]
    # where x = dist from left
    # and y = dist from top
    distances = pd.Series(np.zeros(coords.shape[0]))

    for coordinate in positions.iterrows():
        distances[coordinate[0]] = abs(coordinate[1][0]-point[0])+abs(coordinate[1][1]-point[1])

    if distances[distances == distances.min()].shape[0] != 1:
        return "."
    else:
        return distances[distances == distances.min()].index[0]+1

# This block of code took a very long time to run for me so I decided to store
# it in a .csv file to save time when solving the problem
#map = pd.DataFrame(np.zeros((360,360))).astype(str)
#for row in range(map.shape[0]):
#    print "currently on row:", row
#    for column in range(map.shape[1]):
#        map.iat[row,column] = get_shortest_dist(coords, [column,row])
#map.to_csv("map.csv")

map = pd.read_csv("map.csv", index_col=0)
map = map.replace(".","0").astype(int)

finite_areas = range(coords.shape[0])
for a in range(360):
    if int(map.iat[a,0])-1 in finite_areas: finite_areas.remove(int(map.iat[a,0])-1)
    if int(map.iat[a,359])-1 in finite_areas: finite_areas.remove(int(map.iat[a,359])-1)
    if int(map.iat[0,a])-1 in finite_areas: finite_areas.remove(int(map.iat[0,a])-1)
    if int(map.iat[359,a])-1 in finite_areas: finite_areas.remove(int(map.iat[359,a])-1)

areas = []
for item in finite_areas:
    areas.append((map[map == item+1].sum().sum())/(item+1))

print "Solution to part 1:", max(areas)
