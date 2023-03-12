import os, time

todoList = []

view = "\033[0;34mview\033[0m"
add = "\033[0;32madd\033[0m"
edit = "\033[0;35medit\033[0m"
remove = "\033[0;33mremove\033[0m"
delete = "\033[0;31mdelete\033[0m"
settings = "\033[4msettings\033[0m"
exitList = "\033[3mexit\033[0m"
invalidInput = "\033[?25l\033[0;31m<Invalid input>\033[0m"
warningText = "\033[31m\033[?25lThis item is already in the list!\033[0m"

def viewList():
  os.system("cls")
  print("                      \033[?25l\033[0mTo-Do List Manager\n                     ────────────────────")
  print("\033[4mTo-Do List\033[0m")
  for item in todoList:
    print(item)
  input("\033[?25lPress enter to continue...")
  os.system("cls")

def addItem():
  os.system("cls")
  while True:
    print("                      \033[0mTo-Do List Manager\n                     ────────────────────\n")
    item = input("Add new todo list item: ").title()
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
    itemToRemove = input(f'Which item would you like to {remove}?("exit" to exit): ').title()
    if itemToRemove == "Exit":
      print("\033[31m\033[?25lExiting...\033[0m")
      time.sleep(0.3)
      os.system("cls")
      break
    if itemToRemove not in todoList:
      print(f"\033[31m\033[?25l<{itemToRemove} is not in the list>\033[0m")
      time.sleep(1)
      os.system("cls")
      continue
    confirmation = input(f"Are you sure you want to {remove} this item?: ")
    if confirmation == "no":
      print("\033[33m\033[?25l<No items were removed>\033[0m")
      time.sleep(1)
      os.system("cls")
      continue
    if confirmation != "yes" and confirmation!= "no" :
      print(invalidInput)
      time.sleep(0.7)
      os.system("cls")
      continue
    if itemToRemove in todoList and confirmation == "yes":
      todoList.remove(itemToRemove)
      print(f"\033[32m\033[?25l{itemToRemove} has been successfully removed\033[0m")
      time.sleep(1)
      os.system("cls")
      break

def editItem():
  os.system("cls")
  while True:
    print("                      \033[?25h\033[0mTo-Do List Manager\n                     ────────────────────")
    print("\033[4mTodo List:\033[0m\n")
    for item in todoList:
      print(item)
    print()
    itemToEdit = input(f'Which item would you like to {edit}?("exit" to exit): ').title()
    if itemToEdit == "Exit":
      print("\033[31m\033[?25lExiting...\033[0m")
      time.sleep(0.3)
      os.system("cls")
      break
    if itemToEdit not in todoList:
      print(f"\033[31m\033[?25l<{itemToEdit} is not in the list>\033[0m")
      time.sleep(1)
      os.system("cls")
      continue
    newItem = input(f"What would you like to change {itemToEdit} to?: ").title()
    confirmation = input(f'Are you sure you want to {edit} this item?: ')
    if confirmation == "no":
      print("\033[33m\033[?25l<No items were edited>\033[0m")
      time.sleep(1)
      os.system("cls")
      continue
    if confirmation != "yes" and confirmation!= "no" :
      print(invalidInput)
      time.sleep(0.7)
      os.system("cls")
      continue
    for i in range(0, len(todoList)):
      if todoList[i] == itemToEdit and confirmation == "yes":
        todoList[i] = newItem
        print(f"\033[32m\033[?25l<{item} has been successfully edited>\033[0m")
        time.sleep(1)
        os.system("cls")
        break
    break

def deleteList():
  os.system("cls")
  print()
  deleteToDoList = input(f"Are you sure you want to {delete} the list?: ")
  if deleteToDoList == "yes":
    todoList.clear()
    print(f"\033[31m\033[?25lTo-Do list has been successfully deleted\033[0m")
    time.sleep(1)
    os.system("cls")
  elif deleteToDoList == "no":
    print(f"\033[33m\033[?25l<List deletion terminated>\033[0m")
    time.sleep(1)
    os.system("cls")
  else:
    print(invalidInput)
    time.sleep(0.7)
    os.system("cls")

while True:
  os.system("cls")
  print("                      \033[?25hTo-Do List Manager\n                     ────────────────────\n")
  choice = input(f"Do you want to {view} the list, {add} an item, {edit} an item, {remove} an item or {delete} the list?\nClose by typing {exitList}.\n> ")
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
    print("\033[31m\033[?25lExiting...\033[0m")
    time.sleep(0.3)
    os.system("cls")
    break
  else:
    print(f"{invalidInput}")
    time.sleep(.7)
    os.system("cls")