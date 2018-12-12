# Day 10: The Stars Align
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = open("input","r")
velocity = []
positions = pd.DataFrame(columns=["x","y"])
velocity = pd.DataFrame(columns=["x","y"])

for line in data:
    splitted = line.split("=")
    tmppos = map(int, splitted[1].split(">")[0].split("<")[1].split(","))
    positions = positions.append({"x":tmppos[0], "y":tmppos[1]}, ignore_index=True)
    tmpvel = map(int,splitted[2].split("<")[1].split(">")[0].split(","))
    velocity = velocity.append({"x":tmpvel[0], "y":tmpvel[1]}, ignore_index=True)

# Note: the number 10101 was NOT arbitrarily chosen!
#
# I initially ran a loop to see the positons of the stars in 250-second intervals
# After around 40*250 seconds, a message started to appear
# However, since the message lasts for only 1 second, when approaching the
# 10,000-second mark, positions must be changed in smaller intervals, like
# in 1 or 10-second intervals.
#
# Eventually, I managed to pinpoint the second (10101) where the stars looked
# particularly aligned. I saved the image as message.png and noted down
# the exact number of seconds required to achieve that outcome.
# The image seen needs to be rotated 180 degrees and flipped horizontally
# to see the message.

positions = positions.add(velocity*10101)
plt.scatter(positions.x, positions.y, s = 75)
plt.axis('equal')
plt.show()
