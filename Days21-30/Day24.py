import random
print("Infinity Dice")

numberOfSides = int(input("How many sides?: "))
rollAgain = "yes"

def diceRoll(numberOfSides):
  print(f"You rolled {random.randint(1, numberOfSides)}")
  print()
while rollAgain == "yes":
  diceRoll(numberOfSides)
  rollAgain = input("Do you want to roll again?: ")