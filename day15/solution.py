# Day 15: Beverage Bandits
#import pandas as pd
#import numpy as np
dim = [7,7]
gamemap = [[" " for i in range(dim[0])] for j in range(dim[1])]

# Define relevant functions for convenience
class unit:
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type
        self.power = 3
        self.hp = 200

    def up(self):
        return [self.pos[0] - 1, self.pos[1]]

    def down(self):
        return [self.pos[0] + 1, self.pos[1]]

    def left(self):
        return [self.pos[0], self.pos[1] - 1]

    def right(self):
        return [self.pos[0], self.pos[1] + 1]

def get_pos(pos, board = gamemap):
    return board[pos[0]][pos[1]]

def assign_pos(pos, val, board = gamemap):
    board[pos[0]][pos[1]] = val

def print_map(board = gamemap):
    for lone in board:
        print ''.join(lone)
    print ""

def get_range(targets):
    inrange = []
    for target in targets:
        if get_pos(target.up()) == ".":
            inrange.append(target.up())
        if get_pos(target.down()) == ".":
            inrange.append(target.down())
        if get_pos(target.left()) == ".":
            inrange.append(target.left())
        if get_pos(target.right()) == ".":
            inrange.append(target.right())

    return inrange

def get_reachable_tiles(character, charmap):
    searcher = unit(character.pos, "G")
    search_queue = [searcher.pos]
    assign_pos(searcher.pos, "0", charmap)

    while len(search_queue) != 0:
        searcher.pos = search_queue[0]
        dist = int(get_pos(searcher.pos, charmap)) + 1

        if (get_pos(searcher.up()) == ".") and (get_pos(searcher.up(), charmap) == " "):
            search_queue.append(searcher.up())
            assign_pos(searcher.up(), str(dist), charmap)
        if (get_pos(searcher.down()) == ".") and (get_pos(searcher.down(), charmap) == " "):
            search_queue.append(searcher.down())
            assign_pos(searcher.down(), str(dist), charmap)
        if (get_pos(searcher.left()) == ".") and (get_pos(searcher.left(), charmap) == " "):
            search_queue.append(searcher.left())
            assign_pos(searcher.left(), str(dist), charmap)
        if (get_pos(searcher.right()) == ".") and (get_pos(searcher.right(), charmap) == " "):
            search_queue.append(searcher.right())
            assign_pos(searcher.right(), str(dist), charmap)
        search_queue.pop(0)

    return charmap

def get_unit_from_pos(pos, units):
    for Unit in units:
        if Unit.pos == pos:
            return Unit

def attack(thing, opptype, to_remove):
    if get_pos(thing.up()) == opptype or get_pos(thing.down()) == opptype or get_pos(thing.left()) == opptype or get_pos(thing.right()) == opptype:
        # Get the current unit's attack target
        healths = []
        adj_units = []
        pos_units = []
        for tile in [thing.up(), thing.down(), thing.left(), thing.right()]:
            if get_pos(tile) == "E" and get_pos(tile) == opptype:
                adjunit = get_unit_from_pos(tile, elves)
                healths.append(adjunit.hp)
                adj_units.append(adjunit)
            elif get_pos(tile) == "G" and get_pos(tile) == opptype  :
                adjunit = get_unit_from_pos(tile, goblins)
                healths.append(adjunit.hp)
                adj_units.append(adjunit)
        healths = min(healths)
        for Unit in adj_units:
            if (Unit.hp == healths) and (Unit not in to_remove):
                    # check if to_remove is not empty
                pos_units.append(Unit)
        pos_units.sort(key = lambda x: x.pos)
        target_unit = pos_units[0]
        #print "unit", thing.type, "at", thing.pos, "with target", target_unit.type, "at", target_unit.pos

        # Register the attack
        target_unit.hp -= thing.power
        if target_unit.hp <= 0:
            assign_pos(target_unit.pos, ".")
            to_remove.append(target_unit)

    return to_remove

# Set up the game board
data = open("test4","r")
row, col = 0, 0
units = []

for line in data:
    for char in line:
        if char != "\n":
            if char == "G" or char == "E":
                units.append(unit([row,col], char))
            #else:
            gamemap[row][col] = char
        col += 1
    row += 1
    col = 0

# Game logic
flag = True
tmp = 0

print ""
print "round 0"
print_map()

while flag:
    units.sort(key = lambda x: x.pos)

    # Split current units into goblins and elves
    elves = []
    goblins = []
    to_remove = []
    for thing in units:
        if thing.type == "E":
            elves.append(thing)
        elif thing.type == "G":
            goblins.append(thing)

    for thing in units:
        #print "unit", thing.type, "at", thing.pos
        # Get the list of tiles in range
        if thing.type == "E":
            in_range = get_range(goblins)
            opptype = "G"
            enemies = goblins
        elif thing.type == "G":
            in_range = get_range(elves)
            opptype = "E"
            enemies = elves

        if get_pos(thing.up()) == opptype or get_pos(thing.down()) == opptype or get_pos(thing.left()) == opptype or get_pos(thing.right()) == opptype:
            #print to_remove, "top"
            to_remove = attack(thing, opptype, to_remove)

        else:
            # Determine which tile (in range) to walk towards
            paths = []
            shortest_len = 999999
            grt = get_reachable_tiles(thing, [[" " for i in range(dim[0])] for j in range(dim[1])])
            for tile in in_range:
                if get_pos(tile, grt) != " ":
                    shortest_len = min(shortest_len, int(get_pos(tile,grt)))
            for tile in in_range:
                if get_pos(tile, grt) == str(shortest_len):
                    paths.append(tile)
            if len(paths) == 0:
                pass

            else:
                paths.sort()
                chosen_tile = paths[0]

                # Determine how to walk towards the chosen square
                cmp = get_reachable_tiles(unit(chosen_tile, "E"), [[" " for i in range(dim[0])] for j in range(dim[1])])
                paths = []
                dists = []

                for tile in [thing.up(), thing.down(), thing.left(), thing.right()]:
                    if get_pos(tile, cmp) != " ":
                        dists.append(get_pos(tile, cmp))
                dists = min(dists)
                for tile in [thing.up(), thing.down(), thing.left(), thing.right()]:
                    if get_pos(tile, cmp) == dists:
                        paths.append(tile)
                paths.sort()
                next_move = paths[0]

                # Actually move
                assign_pos(thing.pos, ".")
                thing.pos = next_move
                assign_pos(thing.pos, thing.type)
                to_remove = attack(thing, opptype, to_remove)

    tmp += 1
    print "round", tmp
    print_map()

    # check if to_remove is not empty
    for element in to_remove:
        units.remove(element)

    units.sort(key = lambda x: x.pos)
    for Unit in units:
        pass
        #print "unit", Unit.type, "at", Unit.pos, "with", Unit.hp
    print ""

    # debug: figure out why the pathing is wrong (step 24-25 of example)
    if tmp == 1:
        flag = False
