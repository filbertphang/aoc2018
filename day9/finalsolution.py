# Day 9: Marble Mania
# After searching on /r/adventofcode, I learnt that a more efficient
# solution would be to use circular doubly linked lists
# This is my attempt at such an implementation

# Part 2
data = open("input","r")
for line in data:
    players = int(line.split()[0])
    lastmarble = int(line.split()[-2])
lastmarble *= 100

def clockwise(stack, cur):
    return stack[cur][1]

def anticlockwise(stack, cur):
    for i in range(7):
        a = stack[cur][0]
        cur = a
    return cur

stack = [0]*(lastmarble+1)
stack[0] = [1,1]
stack[1] = [0,0]
curmarble = 2
curpos = 1
curplayer = 1
stacksize = 2
scores = [0]*players
while curmarble != lastmarble+1:
    if curmarble % 23 == 0:
        curpos = anticlockwise(stack, curpos)
        scores[curplayer] += curmarble + curpos
        stack[stack[curpos][0]][1] = stack[curpos][1]
        stack[stack[curpos][1]][0] = stack[curpos][0]
        curpos = clockwise(stack, curpos)
        #print curmarble

    else:
        curpos = clockwise(stack, curpos)
        #print "curpos:", curpos, "curmarble:", curmarble
        stack[curmarble] = [curpos, stack[curpos][1]]
        stack[stack[curpos][1]][0] = curmarble
        stack[curpos][1] = curmarble
        stacksize += 1
        curpos = curmarble
        #print stack

    curmarble += 1
    curplayer += 1
    if curplayer == players:
        curplayer = 0

print "Solution to part 2", max(scores)
