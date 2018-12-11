# Day 9: Marble Mania
# This was my initial solution for day 9
# After realising that Part 2 would take an obscenely long time
# to finish (even longer than my day 5 part 2 implementation),
# I decided to look up hints on /r/adventofcode
data = open("input","r")
for line in data:
    players = int(line.split()[0])
    lastmarble = int(line.split()[-2])

def clockwise(arr, pos):
    n = 1
    while n != 0:
        n -= 1
        pos += 1
        if pos == len(arr):
            pos = 0
    return pos+1

def anticlockwise(arr, pos):
    n = 7
    while n != 0:
        n -= 1
        pos -= 1
        if pos == -1:
            pos = len(arr)-1
    return pos

# Part 1
stack = [0]
curmarble = 1
curpos = 0
curplayer = 0
curscore = 0
scores = [0]*players
while curmarble != lastmarble+1:
    if curmarble % 23 == 0:
        remove = anticlockwise(stack,curpos)
        curscore = curmarble + stack[remove]
        stack.pop(remove)
        curpos = remove
        if remove == len(stack):
            curpos = 0
        scores[curplayer] += curscore
    else:
        curpos = clockwise(stack,curpos)
        stack.insert(curpos, curmarble)
    curmarble += 1
    curplayer += 1
    if curplayer == players:
        curplayer = 0

print "Solution to part 1", max(scores)
