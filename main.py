legendaryChance = float(input("What is your legendary chance?"))
boxesOpened = int(input("How many boxes did you open?"))

chance = 1 - ((1 - legendaryChance)**boxesOpened)
print(chance, "%")