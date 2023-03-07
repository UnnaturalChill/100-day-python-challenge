import random

print("Guess the number game")

retries = 0
rndNumber = random.randint(1, 1000)
guess = 0

while True:
  if guess < 0:
    print()
    print("You have to guess a positive number but fine.")
    exit()
  
  print()
  guess = int(input("Guess a number between 1 and 1000 > "))
  print()
  if guess == rndNumber:
    print("Congratulations! You guessed the number!")
    break
  elif guess < rndNumber:
    print("Your guess was too low.")
    retries += 1
    continue
  elif guess > rndNumber:
    print("Your guess was too high.")
    retries += 1
    continue
  else:
    print("You have to guess a number between 1 and 1000.")

input(f"It took you {retries} retries to get it correct.")