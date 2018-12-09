# Day 8: Memory Maneuver
def get_metadata(data, children):
    nchild = int(data[0])
    nmetadata = int(data[1])
    data.pop(0)
    data.pop(0)
    for child in range(nchild):
        children.append(get_metadata(data, []))

    for datum in range(nmetadata):
        children.append(data[0])
        data.pop(0)

    return children

def sumall(arr, sum):
    for element in arr:
        if type(element) == list:
            sum = sumall(element, sum)
        else:
            sum += int(element)
    return sum

def get_value(data, value):
    nchild = 0
    for item in data:
        if type(item) == list:
            nchild += 1
    if nchild == 0:
        value += sum(map(int, data))
    else:
        children = []
        for child in range(nchild):
            children.append(get_value(data[child],0))
        for meta in data[nchild:]:
            if int(meta) <= nchild:
                value += children[int(meta)-1]

    return value

# Part 1
input = open("input","r")
for line in input:
    data = line.split()
input.close()
print "Solution to part 1:", sumall(get_metadata(data,[]),0)

# Part 2
input = open("input","r")
for line in input:
    data = line.split()
input.close()

print "Solution to part 2:", get_value(get_metadata(data, []), 0)
