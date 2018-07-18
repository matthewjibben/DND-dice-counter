import tkinter as tk
import matplotlib.pyplot as plt
import dictStats as ds


def diceValueCounter(sideCount, diceCount, modifier):
    # working with given variables, create list of possible sides for each die
    rolls = list(range(1, sideCount + 1))
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
        val = modifier
        for j in range(len(totalSides)):
            # get the correct value for the current die
            val += totalSides[j][int(i / (sideCount ** j)) % sideCount]
        # add the total value of the roll into totalValues, our counter dictionary
        totalValues[val] = totalValues.get(val, 0) + 1

    return totalValues


def getProbs(totalValues):
    aggregate = sum(totalValues.values())
    probs = []
    for i in totalValues:
        probs.append(totalValues[i]/aggregate*100)
    return probs


def makeTextWindow(text):
    texty = tk.Tk()
    # set the width to be the maximum line length or at least 60 and the height to be up to 20
    T = tk.Text(texty, height=min(20, text.count("\n")+1), width=max(len(max(text.split("\n"), key=len)), 60))
    T.pack()
    T.insert(tk.END, text)


def showVals(sideCount, diceCount, modifier):
    vals = diceValueCounter(sideCount, diceCount, modifier)
    # set up bar graph
    plt.figure(0)
    plt.bar(range(len(vals)), vals.values(), align='center')
    plt.xticks(range(len(vals)), list(vals.keys()))
    # make labels and enable grid
    plt.xlabel("Roll value")
    plt.ylabel("Combination amount")
    plt.grid(True)

    # get data for pie chart
    sizes = getProbs(vals)
    labels = tuple(vals.keys())
    # now set up the pie chart
    plt.figure(1)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
    plt.axis('equal')
    # plt.show()

    # making text window to display average value, min, max, and percentages
    message = f"""The average roll is {ds.dmean(vals)}
The lowest roll is {min(vals)} and the highest is {max(vals)}
=========================================="""
    # loop through each roll value and add its statistics to the message
    for key, val in sorted(vals.items(), key=lambda i: i[1], reverse=True):
        message += "\n{"+f"Roll: {key} Chance: {round(val/ds.totalRolls(vals)*100, 2)}% Combinations: {val}"+"}"
    makeTextWindow(message)

    # show the matplotlib charts
    # this must happen after displaying the second tkinter window, not before
    plt.show()


# setup tkinter window, size, and title
inputWindow = tk.Tk()
inputWindow.title("Dice counter")
# inputWindow.minsize(width=400, height=100)

# making labels for the inputs
tk.Label(inputWindow, text="Sides", width=15, height=2).grid(row=0)
tk.Label(inputWindow, text="Dice", width=15, height=2).grid(row=1)
tk.Label(inputWindow, text="Modifier", width=15, height=2).grid(row=2)

# making the actual entries
sides = tk.Entry(inputWindow)
dice = tk.Entry(inputWindow)
modi = tk.Entry(inputWindow)
# setting their positions
sides.grid(row=0, column=1)
dice.grid(row=1, column=1)
modi.grid(row=2, column=1)
# setting the entry's default value
sides.insert(0, 6)
dice.insert(0, 2)
modi.insert(0, 0)

# making buttons
tk.Button(inputWindow, text="Calculate",
          command=lambda: showVals(int(sides.get()), int(dice.get()), int(modi.get())),
          width=15, height=2).grid(row=3, column=0)
tk.Button(inputWindow, text="exit", command=inputWindow.destroy, width=16, height=2).grid(row=3, column=1)

tk.mainloop()

#print(diceValueCounter(6, 2, 0))
