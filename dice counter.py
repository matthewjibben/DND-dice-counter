import numpy
import matplotlib.pyplot as plt
import math
import tkinter


def addToCount(dict, val):
    if val in dict:
        dict[val] += 1
    else:
        dict[val] = 1
# get user input for these variables
sideCount = 6
diceCount = 2
modifier = 0

# working with variables
rolls = list(range(1, sideCount+1))
totalSides = [rolls] * diceCount

# this is our counter dictionary, used to count how many times each roll value is possible
totalValues = {}

# The variable 'val' gets the correct side, by getting (i div sides^dieNum) mod 6
# for example with 3d6, this will give 0...5 every 6 iterations for die number 1,
# then for die number 2 it will return 0 for iterations 0...5, and 1 for iterations 6...11,
# and 2 for iterations 12...17, and so on
# for die 3, it will return 0 for iterations 0...35, return 1 for iterations 36...71, and so on.
# the vals for all die (a single roll) are all added together, then placed in totalValues

for i in range(sideCount ** diceCount):
    val = 0
    for j in range(len(totalSides)):
        # get the correct value for the current die
        val += totalSides[j][int(i/(sideCount ** j)) % sideCount]
    # add the total value of the roll into totalValues, our counter dictionary
    totalValues[val] = totalValues.get(val, 0) + 1

print(totalValues)
