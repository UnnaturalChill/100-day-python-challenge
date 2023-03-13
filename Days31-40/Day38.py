def colorize(color):
  if color == 'b':
    print("\033[34m", end="")
  elif color == 'g':
    print("\033[32m", end="")
  elif color == 'p':
    print("\033[35m", end="")
  elif color == 'y':
    print("\033[33m", end="")
  elif color == 'r':
    print("\033[31m", end="")
  elif color == ' ':
    print("\033[0m", end="")

sentence = input("What sentence do you want rainbow-ising?: ")
for letter in sentence:
  colorize(letter.lower())
  print(letter, end="")
print()