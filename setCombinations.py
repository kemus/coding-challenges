testLists = [
         ['apple', 'banana', 'pear'],
         ['car','truck'],
         ['zambia', 'malawi', 'kenya'],
    ]

def setCombinations(lists):
    # how many items are in each list
    listLengths = [len(l)-1 for l in lists]
    combination = [0 for i in lists]

    def getNextCombination(combination, listLengths, digit):
        # Did we loop through all the combinations?
        if digit >= len(combination):
            return False

        # Can we add one to this place?
        if combination[digit] < listLengths[digit]:
            combination[digit]+=1
            return combination

        # Carry the one...
        else:
            combination[digit] = 0
            return getNextCombination(combination, listLengths, digit+1)

    while combination:
        print [lists[i][combination[i]] for i in range(len(lists))]
        combination = getNextCombination(combination, listLengths, 0)

if __name__ == "__main__":
    setCombinations(testLists)
