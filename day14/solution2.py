# Day 14: Chocolate Charts
import time

input = 157901
Tstart = time.time()

# Part 2
# Original solution was similar but took an exceptionally long time
# to run.
# Optimization made: instead of checking the entire scoreboard for
# the required receipe, only check the last few elements of the list
# so less time is required

scoreboard = [3,7]
str_scoreboard = ''.join(map(str, scoreboard[-7:]))
elf1 = 0
elf2 = 1

while str(input) not in str_scoreboard:
    sum = scoreboard[elf1] + scoreboard[elf2]
    for char in str(sum):
        scoreboard.append(int(char))
    elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
    elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)

    str_scoreboard = ''.join(map(str, scoreboard[-7:]))

str_scoreboard = ''.join(map(str, scoreboard))
print "Solution to part 2:", str_scoreboard.find(str(input))
print "Time elapsed for part 2:", time.time()-Tstart
