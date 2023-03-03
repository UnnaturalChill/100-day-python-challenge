print("Fill-in the blank lyrics game!")
print("""You will be presented with 3 different lyrics. 
Try to guess the missing parts!""")
print()
counter1 = 1
counter2 = 1
counter3 = 1
next1 = 0
next2 = 0

while True:
  print("\033[32mLevel 1\033[0m")
  print("As the ____ swings the great pendulum")
  lyrics1 = input(">\033[32m ")
  print()
  if lyrics1 != "time":
    print("\033[0mWrong! Try again!")
    counter1 += 1
  else:
    print("\033[0mWell done! You guessed it right!")
    next1 = 1
    break

while next1 == 1:
  print()
  print("\033[33mLevel 2\033[0m")
  print("Born without a ____ on the darkest day")
  lyrics2 = input(">\033[33m ")
  print()
  if lyrics2 != "name":
    print("\033[0mWrong! Try again!")
    counter2 += 1
  else:
    print("\033[0mWell done! You guessed it right!")
    next2 = 1
    break

while next2 == 1:
    print()
    print("\033[31mLevel 3\033[0m")
    print("Diving in, I'm reaching for the ____ of a nuclear reactor")
    lyrics3 = input(">\033[31m ")
    print()
    if lyrics3 != "core":
      print("\033[0mWrong! Try again!")
      counter3 += 1
    else:
      print("\033[0mWell done! You guessed it right!")
      break

total = counter1 + counter2 + counter3

print("It took you\033[32m", counter1, "\033[0mtries to guess the first missing part!")
print("It took you\033[33m", counter2, "\033[0mtries to guess the second missing part!")
print("It took you\033[31m", counter3, "\033[0mtries to guess the third missing part!")
print("It took you a total of\033[34m", total, "\033[0mattempts to guess all the missing parts!")