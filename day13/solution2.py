# Day 13: Mine Cart Madness
import pandas as pd
directions = ["v", "^", ">", "<"]
intersection = ["left", "straight", "right"]

# Part 2
# The only difference between solution2 and solution1 is that in
# the second solution, crashing minecarts are removed.
#
# Had a lot of issues debugging the code:
# 1. Sometimes the movement of certain carts would be skipped.
#    The issue turned out to be because I was removing the
#    cart from the array "carts" while "carts" was being used
#    in a for loop, resulting in the index being shifted forward
#    by 1 item, effectively skipping the next item.
#    Solution: append all carts to remove in a separate array
#    and only remove carts at the end of each cycle
#
# 2. Kept bumping into "element not in list" or "list index
#    out of range" errors. (basically the cart couldn't be removed)
#    The issue was because the statement checking for the other cart
#    involved in the collision did not check whether the other cart
#    was identical to the current cart, resulting in the current cart
#    being removed twice.
#    Solution: when iterating through carts, look for other carts with
#    the same coordinates which are DIFFERENT from the current cart.
#
# The second test example was also modified slightly from the
# one provided on the AoC website.

data = open("input","r")
tempmap = []
for line in data:
    tempmap.append(list(line)[:-1])

map = pd.DataFrame(tempmap)
map = map.replace([None], [' '], regex=True)
shape = map.shape
carts = []
for rown in range(shape[0]):
    for coln in range(shape[1]):
        if str(map.iat[rown,coln]) in "<>^v":
            # This assumes that carts are not initialized at corners
            # or at intersections
            if (coln != 0) and (coln != shape[1]-1) and (map.iat[rown, coln-1] in "-\/+") and (map.iat[rown, coln+1] in "-\/+"):
                prev = "-"
            if (rown != 0) and (rown != shape[0]-1) and (map.iat[rown-1, coln] in "|\/+") and (map.iat[rown+1, coln] in "|\/+"):
                prev = "|"
            carts.append([map.iat[rown,coln], [map.index[rown], map.columns[coln]], 0, prev])

#print map

toremove = []
while len(carts) != 1:
    # Cart moving and turning logic
    for cart in carts:
        if cart in toremove:
            pass

        elif cart[0] == ">":
            if map.iat[cart[1][0], cart[1][1]+1] in "<>^v":
                map.iat[cart[1][0], cart[1][1]] = cart[3]
                cart[1][1] += 1
                toremove.append(cart)
                for othercart in carts:
                    if (othercart[1] == cart[1]) and (othercart != cart):
                        map.iat[cart[1][0], cart[1][1]] = othercart[3]
                        toremove.append(othercart)
                        break
            else:
                if map.iat[cart[1][0], cart[1][1]+1] == "\\":
                    cart[0] = "v"
                elif map.iat[cart[1][0], cart[1][1]+1] == "/":
                    cart[0] = "^"
                elif map.iat[cart[1][0], cart[1][1]+1] == "+":
                    changedir = intersection[cart[2]]
                    if changedir == "left":
                        cart[0] = "^"
                    elif changedir == "right":
                        cart[0] = "v"

                    cart[2] += 1
                    if cart[2] == 3:
                        cart[2] = 0

                map.iat[cart[1][0], cart[1][1]] = cart[3]
                cart[1][1] += 1
                cart[3] = map.iat[cart[1][0], cart[1][1]]
                map.iat[cart[1][0], cart[1][1]] = cart[0]

        elif cart[0] == "<":
            if map.iat[cart[1][0], cart[1][1]-1] in "<>^v":
                map.iat[cart[1][0], cart[1][1]] = cart[3]
                cart[1][1] -= 1
                toremove.append(cart)
                for othercart in carts:
                    if (othercart[1] == cart[1]) and (othercart != cart):
                        map.iat[cart[1][0], cart[1][1]] = othercart[3]
                        toremove.append(othercart)
                        break
            else:
                if map.iat[cart[1][0], cart[1][1]-1] == "\\":
                    cart[0] = "^"
                elif map.iat[cart[1][0], cart[1][1]-1] == "/":
                    cart[0] = "v"
                elif map.iat[cart[1][0], cart[1][1]-1] == "+":
                    changedir = intersection[cart[2]]
                    if changedir == "left":
                        cart[0] = "v"
                    elif changedir == "right":
                        cart[0] = "^"

                    cart[2] += 1
                    if cart[2] == 3:
                        cart[2] = 0

                map.iat[cart[1][0], cart[1][1]] = cart[3]
                cart[1][1] -= 1
                cart[3] = map.iat[cart[1][0], cart[1][1]]
                map.iat[cart[1][0], cart[1][1]] = cart[0]

        elif cart[0] == "v":
            if map.iat[cart[1][0]+1, cart[1][1]] in "<>^v":
                map.iat[cart[1][0], cart[1][1]] = cart[3]
                cart[1][0] += 1
                toremove.append(cart)
                for othercart in carts:
                    if (othercart[1] == cart[1]) and (othercart != cart):
                        map.iat[cart[1][0], cart[1][1]] = othercart[3]
                        toremove.append(othercart)
                        break
            else:
                if map.iat[cart[1][0]+1, cart[1][1]] == "\\":
                    cart[0] = ">"
                elif map.iat[cart[1][0]+1, cart[1][1]] == "/":
                    cart[0] = "<"
                elif map.iat[cart[1][0]+1, cart[1][1]] == "+":
                    changedir = intersection[cart[2]]
                    if changedir == "left":
                        cart[0] = ">"
                    elif changedir == "right":
                        cart[0] = "<"

                    cart[2] += 1
                    if cart[2] == 3:
                        cart[2] = 0

                map.iat[cart[1][0], cart[1][1]] = cart[3]
                cart[1][0] += 1
                cart[3] = map.iat[cart[1][0], cart[1][1]]
                map.iat[cart[1][0], cart[1][1]] = cart[0]

        elif cart[0] == "^":
            if map.iat[cart[1][0]-1, cart[1][1]] in "<>^v":
                map.iat[cart[1][0], cart[1][1]] = cart[3]
                cart[1][0] -= 1
                toremove.append(cart)
                for othercart in carts:
                    if (othercart[1] == cart[1]) and (othercart != cart):
                        map.iat[cart[1][0], cart[1][1]] = othercart[3]
                        toremove.append(othercart)
                        break
            else:
                if map.iat[cart[1][0]-1, cart[1][1]] == "\\":
                    cart[0] = "<"
                elif map.iat[cart[1][0]-1, cart[1][1]] == "/":
                    cart[0] = ">"
                elif map.iat[cart[1][0]-1, cart[1][1]] == "+":
                    changedir = intersection[cart[2]]
                    if changedir == "left":
                        cart[0] = "<"
                    elif changedir == "right":
                        cart[0] = ">"

                    cart[2] += 1
                    if cart[2] == 3:
                        cart[2] = 0

                map.iat[cart[1][0], cart[1][1]] = cart[3]
                cart[1][0] -= 1
                cart[3] = map.iat[cart[1][0], cart[1][1]]
                map.iat[cart[1][0], cart[1][1]] = cart[0]

    for remcart in toremove:
        carts.remove(remcart)
    toremove = []
    #print map

    carts.sort(key=lambda x: x[1])

print "Solution to part 2:", str(carts[0][1][1])+","+str(carts[0][1][0])
