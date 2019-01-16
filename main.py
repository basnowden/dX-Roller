import random

def getInput():
    sides = input("How many sides on the desired die?\n")
    quantity = input("How many dice to roll?\n")
    if sides == "":
        sides = 2
    if quantity == "":
        quantity = 1
    return sides,quantity

def roll(sides):
    result = random.randint(1,sides)
    return result

sides,quantity = getInput()
results = []
for currRoll in range(int(quantity)):
    result = roll(int(sides))
    results.append(result)
    #print("Result of d",sides," roll ",currRoll,": ",result,sep="")
print(*results,sep=", ")
