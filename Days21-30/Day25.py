import random

def diceRoll(numberOfSides):
  return random.randint(1, numberOfSides)

def characterHpGenerator():
  characterHp = random.randint(1, 7) * random.randint(1, 9)
  return characterHp

print("CHARACTER STAT GENERATOR")
print()

continueLoop = "yes"
while continueLoop == "yes":
  characterHp = characterHpGenerator()
  input("Name your warrior: ")
  print(f"Their health is {characterHp}")
  print()
  continueLoop = input("Would you like to create another character? (yes/no): ")
  print()