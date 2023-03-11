import os, time

todoList = []

view = "\033[0;34mview\033[0m"
add = "\033[0;32madd\033[0m"
edit = "\033[0;35medit\033[0m"
remove = "\033[0;33mremove\033[0m"
delete = "\033[0;31mdelete\033[0m"
exitList = "\033[3mexit\033[0m"
invalidInput = "\033[?25l\033[0;31m<Invalid input>\033[0m"

def viewList():
  os.system("cls")
  print("                      \033[?25l\033[0mTo-Do List Manager\n                     ────────────────────\n")
  print("To-Do List\n──────────")
  for item in todoList:
    print(item)
  time.sleep(1.5)
  os.system("cls")

def addItem():
  os.system("cls")
  warningText = "\033[31This item is already in the list!\033[0m"
  while True:
    print("                      \033[0mTo-Do List Manager\n                     ────────────────────\n")
    item = input("Add new todo list item: ")
    if item not in todoList:
      todoList.append(item)
      break
    else:
      print(warningText)
      time.sleep(1.5)
      os.system("cls")
      break

def removeItem():
  os.system("cls")
  while True:
    print("                      \033[?25h\033[0mTo-Do List Manager\n                     ────────────────────")
    print("\033[4mTodo List:\033[0m")
    for item in todoList:
      print(item)
    print()
    itemToRemove = input(f"Which item would you like to {remove}?: ")
    confirmation = input(f"Are you sure you want to {remove} this item?: ")
    if confirmation == "yes":
      if itemToRemove in todoList:
        todoList.remove(itemToRemove)
        print(f"\033[32m{itemToRemove} has been successfully removed\033[0m")
        time.sleep(1)
        os.system("cls")
        break
      else:
        print("\033[31m<Item is not in the list>\033[0m")
        time.sleep(1)
        os.system("cls")
        continue
    elif confirmation == "no":
      print("\033[33m<No items were removed>\033[0m")
      time.sleep(1)
      os.system("cls")
      break
    else:
      print(invalidInput)
      time.sleep(0.7)
      os.system("cls")
      continue

#! Broken
def editItem():
  os.system("cls")
  while True:
    print("                      \033[?25h\033[0mTo-Do List Manager\n                     ────────────────────")
    print("\033[4mTodo List:\033[0m")
    for item in todoList:
      print(item)
    print()
    itemToEdit = input(f"Which item would you like to {edit}?: ")
    if itemToEdit == item in todoList:
      confirmation = input(f"Are you sure you want to {edit} this item?: ")
      if confirmation == "yes":
        editedItem = input(f"What would you like to change {itemToEdit} to?: ")
        for i in range(0, len(todoList)):
          todoList[i] = editedItem
        print(f"\033[32m<{item} has been successfully edited>\033[0m")
        time.sleep(1)
        os.system("cls")
        break
      elif confirmation == "no":
        print("\033[33m<No items were edited>\033[0m")
        time.sleep(1)
        os.system("cls")
        break
      else:
        print(invalidInput)
        time.sleep(0.7)
        os.system("cls")
        continue
    if itemToEdit not in todoList:
      print(f"\033[31m<{itemToEdit} is not in the list>\033[0m")
      time.sleep(1)
      os.system("cls")
      continue

def deleteList():
  os.system("cls")
  print()
  deleteToDoList = input(f"Are you sure you want to {delete} the list?: ")
  if deleteToDoList == "yes":
    todoList.clear()
    print(f"\033[?25lTo-Do list has been successfully deleted")
    time.sleep(1)
    os.system("cls")
    return todoList

while True:
  os.system("cls")
  print("                      \033[?25hTo-Do List Manager\n                     ────────────────────\n")
  choice = input(f"Do you want to {view}, {add}, {edit}, {remove} or {delete} a To-Do list?\nClose by typing {exitList}.\n> ")
  if choice == "view":
    viewList()
  elif choice == "add":
    addItem()
  elif choice == "edit":
    editItem()
  elif choice == "remove":
    removeItem()
  elif choice == "delete":
    deleteList()
  elif choice == "exit":
    print("\033[0;31mExiting...\033[0m")
    time.sleep(0.3)
    os.system("cls")
    break
  else:
    print(f"{invalidInput}")
    time.sleep(.7)
    os.system("cls")