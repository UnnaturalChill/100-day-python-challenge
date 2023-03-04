exit = ""

while exit != "yes":
  print("What animal sound do you want to hear?")
  print("Options: Cat, Dog, Horse, Sheep, Cow.")
  answer = input("> ")

  if answer == "cat" or answer == "Cat":
    print("Meow!")
  elif answer == "dog" or answer == "Dog":
    print("Woof!")
  elif answer == "horse" or answer == "Horse":
    print("Neigh!")
  elif answer == "sheep" or answer == "Sheep":
    print("Baa!")
  elif answer == "cow" or answer == "Cow":
    print("Moo!")
  else: print("You didn't enter a valid answer.")

  exit = input("Would you like to exit? (yes/no): ")