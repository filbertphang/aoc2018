# Day 7: The Sum of Its Parts
import pandas as pd
import numpy as np
data = open("input","r")
steps = {}

#steps = {  letter:[[inputs],[outputs]]  }

for line in data:
    finished = line[5]
    requirement = line[36]
    if finished in steps:
        steps[finished][1].append(requirement)
    else:
        steps[finished] = [[],[requirement]]

    if requirement in steps:
        steps[requirement][0].append(finished)
    else:
        steps[requirement] = [[finished],[]]

# Part 1
def get_options(step):
    paths = []
    for key in steps:
        if step == []:
            if step == steps[key][0]:
                paths.append(key)
        elif all(i in step for i in steps[key][0]) and key not in step:
            paths.append(key)
    return paths

path = ''
queue = []
while len(path) != len(steps):
    queue = get_options(path)
    queue.sort()
    path += queue[0]
    queue.pop(0)
print "Solution to part 1:", path

# Part 2
path = []
queue = get_options(path)

avail = [1,2,3,4,5]
working = []
time = -1
while len(path) != len(steps):
    working.sort(key = lambda x: x[2])
    for element in working:
        element[2] -= 1

    while working != []:
        if working[0][2] == 0:
            path.append(working[0][0])
            avail.append(working[0][1])
            working.pop(0)
            queue = get_options(path)
            queue.sort()
            for thing in path:
                if thing in queue:
                    queue.remove(thing)
            for _thing in working:
                if _thing[0] in queue:
                    queue.remove(_thing[0])
        else:
            break

    while (avail != [] and queue != []):
        set = [queue[0], avail[0], ord(queue[0]) - 4]
        working.append(set)
        queue.pop(0)
        avail.pop(0)

    time += 1

print "Solution to part 2:", time
