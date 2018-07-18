# added this file to help with doing statistics on dictionaries
# assuming that the key is the value, and the value is the number of occurrences


def sumkeys(dict):
    return sum([key for key in dict])


def sumvals(dict):
    return sum([val for key,val in dict.items()])


def dmean(dict):
    totalVal = 0
    numItems = 0
    for key, val in dict.items():
        totalVal += key*val
        numItems += val
    return totalVal/numItems


def totalRolls(dict):
    return sum([val for key, val in dict.items()])


if __name__ == '__main__':
    d = {1: 2, 2: 2, 3: 4, 4: 0}
    print(max(d))
