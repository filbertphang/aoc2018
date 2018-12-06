# Day 5: Alchemical Reduction
import string
data = open("input","r")
for line in data:
    initpolymer = line
data.close()
initpolymer = initpolymer[:-1]

def react(polymer):
    unchanged = True
    for n in range(len(polymer)-1):
        if n+1 > len(polymer):
            pass
        elif ((polymer[n].islower()) and (polymer[n+1] == polymer[n].upper())) or ((polymer[n].isupper()) and (polymer[n+1] == polymer[n].lower())):
            polymer = polymer[:n] + polymer[n+2:]
            unchanged = False
            break
    return polymer, unchanged

def fullyreact(polymer):
    while True:
        polymer, unchanged = react(polymer)
        if unchanged:
            break
    return len(polymer)

# Part 1
polymer = initpolymer
print "Solution to part 1:", fullyreact(polymer)


# Part 2
# code is stupidly unoptimized
# took 15+ minutes to run but at least it got the right answer
polymer_list = []
for letter in string.ascii_lowercase:
    polymer = initpolymer.translate(None, letter).translate(None, letter.upper())
    polymer_list.append(fullyreact(polymer))
print "Solution to part 2:", min(polymer_list)
