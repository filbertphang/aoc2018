# Day 4: Repose Record
import pandas as pd
import numpy as np

df = open("input","r")
sorted = []
for line in df:
    sorted.append(line)
sorted.sort()
df.close()

schedule = {}
for entry in sorted:
    time = int(entry[15:17])
    act = entry[19:].split()

    if act[1][0] == "#":
        guard = act[1]
    elif act[0] == "falls":
        start = time
    elif act[0] == "wakes":
        end = time
        if guard not in schedule:
            schedule[guard] = pd.Series([0] * 60)
        schedule[guard][start:end] += 1

# Part 1
curmax = [0,"",0]
for key in schedule:
    sum = schedule[key].sum()
    if sum > curmax[0]:
        curmax[0] = sum
        curmax[1] = key

timemap = schedule[curmax[1]]
curmax[2] = timemap[timemap == timemap.max()].index[0]
print "Solution to part 1:", int(curmax[1][1:])*curmax[2]

# Part 2
schedule_df = pd.DataFrame(schedule)
max_daily = pd.DataFrame([schedule_df.max(axis=1), np.zeros(60)]).T
for x in range(schedule_df.shape[0]):        # rows
    count = 0
    for y in range(schedule_df.shape[1]):    # columns
        if schedule_df.iat[x,y] == max_daily[0][x]:
            count += 1
    max_daily[1][x] = count
tmp  = max_daily[max_daily[1] == 1].max(axis=0)
min = max_daily.where(max_daily == tmp).dropna().index[0]
val = max_daily.iat[min, 0]
id = schedule_df.iloc[min,:].where(schedule_df.iloc[min,:] == val).dropna().index[0]
print "Solution to part 2:", int(id[1:])*min
