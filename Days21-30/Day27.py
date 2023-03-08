import random, os, time

def diceRoll(sides):
  return random.randint(1, sides)

def characterHealth():
  health = (diceRoll(7) * diceRoll(13) / 2) + 10
  return f"Health: {health}"

def characterStrength():
  strength = (diceRoll(7) * diceRoll(13) / 2) + 12
  return f"Strength: {strength}"

while True:
  print("Character Builder")
  print()
  name = input("Name your character: ")
  characterType = input("Character type (Human, Fairy, Devil, Kappa): ")
  print()
  print(name)
  time.sleep(.3)
  print(characterHealth())
  time.sleep(.3)
  print(characterStrength())
  print()
  print("May your name go down in legend...")
  print()
  retry = input("Again?: ")
  if retry != "yes":
    os.system("clear")
    break
  else:
    os.system("clear")
    continue