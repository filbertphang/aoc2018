# Day 13: Mine Cart Madness
import pandas as pd
directions = ["v", "^", ">", "<"]
intersection = ["left", "straight", "right"]

# Part 1
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

flag = False
while not flag:
    # Cart moving and turning logic
    for cart in carts:
        if cart[0] == ">":
            if map.iat[cart[1][0], cart[1][1]+1] in "<>^v":
                map.iat[cart[1][0], cart[1][1]] = cart[3]
                cart[1][1] += 1
                map.iat[cart[1][0], cart[1][1]] = "X"
                firstcrash = [cart[1][0], cart[1][1]]
                flag = True
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
                map.iat[cart[1][0], cart[1][1]] = "X"
                firstcrash = [cart[1][0], cart[1][1]]
                flag = True
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
                map.iat[cart[1][0], cart[1][1]] = "X"
                firstcrash = [cart[1][0], cart[1][1]]
                flag = True
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
                map.iat[cart[1][0], cart[1][1]] = "X"
                firstcrash = [cart[1][0], cart[1][1]]
                flag = True
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

    #print map
    carts.sort(key=lambda x: x[1])

print "Solution to part 1:", str(firstcrash[1])+","+str(firstcrash[0])
