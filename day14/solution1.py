# Day 14: Chocolate Charts
import time

input = 157901
Tstart = time.time()

# Part 1
scoreboard = [3,7]
elf1 = 0
elf2 = 1

while len(scoreboard) < (input+10):
    sum = scoreboard[elf1] + scoreboard[elf2]
    for char in str(sum):
        scoreboard.append(int(char))
    elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
    elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)

ans1 = ''.join(map(str, scoreboard[input:input+10]))
T1 = time.time()

print "Solution to part 1:", ans1
print "Time elapsed for part 1:", T1-Tstart
