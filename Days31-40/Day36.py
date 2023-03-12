names = []

def printList():
  print()
  for name in names:
    print(name)
  print()

while True:
  firstName = input("What is your name? ").strip().capitalize()
  surname = input("What is your surname? ").strip().capitalize()
  fullName = f"{firstName} {surname}"
  if fullName not in names:
    names.append(fullName)
  else:
    print("Error: Name already exists")
  printList()