import random, os, time

# Define a function to generate a random number between 1 and user-defined
def diceRoll(sides):
  return random.randint(1, sides)

# Define a function to generate character's health
def characterHealth():
  health = ((diceRoll(7) * diceRoll(13)) / 2) + 20
  return health

# Define a function to generate character's attack
def characterAttack():
  attack = ((diceRoll(7) * diceRoll(13)) / 2) + 10
  return attack

# Define a function to generate character's defense
#! WIP
def characterDefense():
  defense = ((diceRoll(7) * diceRoll(13)) / 2) + 15
  return defense

print("⚔️ Fighting game ⚔️\n")
time.sleep(.5)
print("Create your characters")
print()
time.sleep(.7)

# Create character 1
character1Name = input("Name your character: ")
character1Health = characterHealth()
character1Attack = characterAttack()
character1Defense = characterDefense()
print()
time.sleep(.5)
# Character stats
print(f"""Name:     😶  \033[33m{character1Name}\033[0m""") # Yellow
time.sleep(.3)
print(f"""Health:   ❤️  \033[31m{character1Health}\033[0m""") # Red
time.sleep(.3)
print(f"""Attack:   🗡️ \033[37m{character1Attack}\033[0m""") # Gray
time.sleep(.3)
print(f"""Defense:  🛡️ \033[36m{character1Defense}\033[0m""") #! WIP

time.sleep(1)
print()
print("Who are they battling against?")
print()
time.sleep(1)

# Create character 2
character2Name = input("Name your character: ")
character2Health = characterHealth()
character2Attack = characterAttack()
character2Defense = characterDefense()
print()
time.sleep(.5)
# Character stats
print(f"""Name:     😶  \033[33m{character2Name}\033[0m""") # Yellow
time.sleep(.3)
print(f"""Health:   ❤️  \033[31m{character2Health}\033[0m""") # Red
time.sleep(.3)
print(f"""Attack:   🗡️ \033[37m{character2Attack}\033[0m""") # Gray
time.sleep(.3)
print(f"""Defense:  🛡️ \033[36m{character2Defense}\033[0m""") #! WIP

print()
print(f"Battle between {character1Name} and {character2Name} is starting!")
time.sleep(3)
os.system("cls")

roundCounter = 1
while True:
  print("⚔️ BATTLE TIME ⚔️\n")
  time.sleep(.5)
  print("The battle begins!\n")
  time.sleep(.7)
  character1Roll = diceRoll(10)
  character2Roll = diceRoll(10)
  difference = abs(character1Attack - character2Attack) + 1
  if difference < 5:
    difference += 5

  if character1Roll > character2Roll:
    print(f"{character1Name} wins the first blow!")
    time.sleep(.5)
    print(f"{character2Name} takes \033[1m{difference}\033[0m damage!\n")
    time.sleep(.5)
    character2Health -= difference
    print("--------------------")
    print(f""" Name:     😶  \033[33m{character1Name}\033[0m""") # Yellow
    time.sleep(.2)
    print(f""" Health:   ❤️  \033[31m{character1Health}\033[0m\n""") # Red
    time.sleep(.5)
    print(f""" Name:     😶  \033[33m{character2Name}\033[0m""") # Yellow
    time.sleep(.2)
    print(f""" Health:   ❤️  \033[31m{character2Health}\033[0m""") # Red
    print("--------------------\n")
    roundCounter += 1
    time.sleep(1)
    input("Press enter to continue to the next round...")
    os.system("cls")
    break
  elif character1Roll < character2Roll:
    print(f"{character2Name} wins the first blow!")
    time.sleep(.5)
    print(f"{character1Name} takes \033[1m{difference}\033[0m damage!\n")
    time.sleep(.5)
    character1Health -= difference
    print("--------------------")
    print(f""" Name:     😶  \033[33m{character1Name}\033[0m""") # Yellow
    time.sleep(.2)
    print(f""" Health:   ❤️  \033[31m{character1Health}\033[0m\n""") # Red
    time.sleep(.5)
    print(f""" Name:     😶  \033[33m{character2Name}\033[0m""") # Yellow
    time.sleep(.2)
    print(f""" Health:   ❤️  \033[31m{character2Health}\033[0m""") # Red
    print("--------------------\n")
    roundCounter += 1
    time.sleep(1)
    input("Press enter to continue to the next round...")
    os.system("cls")
    break
  else:
    print("It's a draw!")
    time.sleep(.5)
    print("Continuing to the next round...")
    time.sleep(1)
    os.system("cls")
    break
  
while True:
  if character1Health <= 0:
    print(f"{character1Name} lost!")
    time.sleep(.5)
    print("--------------------")
    print(f""" Name:     😶  \033[33m{character1Name}\033[0m""") # Yellow
    time.sleep(.2)
    print(f""" Health:   ❤️  \033[31m{character1Health}\033[0m""") # Red
    print("--------------------\n")
    time.sleep(.5)
    input(f"The battle has ended! {character2Name} has won in {roundCounter} rounds!")
    os.system("cls")
    break
  elif character2Health <= 0:
    time.sleep(.5)
    print(f"{character2Name} lost!")
    print("--------------------")
    print(f""" Name:     😶  \033[33m{character2Name}\033[0m""") # Yellow
    time.sleep(.2)
    print(f""" Health:   ❤️  \033[31m{character2Health}\033[0m""") # Red
    print("--------------------\n")
    time.sleep(.5)
    input(f"The battle has ended! {character1Name} has won in {roundCounter} rounds!")
    os.system("cls")
    break
  else:
    print("⚔️ BATTLE TIME ⚔️\n")
    time.sleep(.5)
    print(f"⚔️ Battle continues! ⚔️")
    print(f"""        Round {roundCounter}\n""")
    time.sleep(.7)
    character1Roll = diceRoll(7)
    character2Roll = diceRoll(7)
    if character1Roll > character2Roll:
      print(f"{character1Name} wins the first blow!")
      time.sleep(.5)
      print(f"{character2Name} takes \033[1m{difference}\033[0m damage!\n")
      time.sleep(.5)
      character2Health -= difference
      print("--------------------")
      print(f""" Name:     😶  \033[33m{character1Name}\033[0m""") # Yellow
      time.sleep(.2)
      print(f""" Health:   ❤️  \033[31m{character1Health}\033[0m\n""") # Red
      time.sleep(.5)
      print(f""" Name:     😶  \033[33m{character2Name}\033[0m""") # Yellow
      time.sleep(.2)
      print(f""" Health:   ❤️  \033[31m{character2Health}\033[0m""") # Red
      print("--------------------\n")
      roundCounter += 1
      time.sleep(1)
      input("Press enter to continue to the next round...")
      os.system("cls")
      continue
    elif character1Roll < character2Roll:
      print(f"{character2Name} wins the first blow!")
      time.sleep(.5)
      print(f"{character1Name} takes \033[1m{difference}\033[0m damage!\n")
      time.sleep(.5)
      character1Health -= difference 
      print("--------------------")
      print(f""" Name:     😶  \033[33m{character1Name}\033[0m""") # Yellow
      time.sleep(.2)
      print(f""" Health:   ❤️  \033[31m{character1Health}\033[0m\n""") # Red
      time.sleep(.5)
      print(f""" Name:     😶  \033[33m{character2Name}\033[0m""") # Yellow
      time.sleep(.2)
      print(f""" Health:   ❤️  \033[31m{character2Health}\033[0m""") # Red
      print("--------------------\n")
      roundCounter += 1
      time.sleep(1)
      input("Press enter to continue to the next round...")
      os.system("cls")
      continue
    else:
      print("It's a draw!\n")
      time.sleep(.5)
      print("Continuing to the next round...\n")
      time.sleep(1)
      os.system("cls")
      continue
