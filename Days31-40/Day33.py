import os, time

todoList = []

def addTodo():
  print()
  item = input("Enter todo item: ")
  todoList.append(item)
  print()

def deleteTodo():
  print()
  print("\033[4mTodo List:\033[0m")
  for item in todoList:
    print(item)
  print()
  item = input("Enter todo item to delete: ")
  todoList.remove(item)
  print()

def viewTodo():
  print()
  print("\033[?25l\033[4mTodo List:\033[0m")
  for item in todoList:
    print(item)
  print()

while True:
  print("\033[?25h\033[4mToDo List Manager\033[0m")
  print()
  print("1. Add Todo")
  print("2. Delete Todo")
  print("3. View Todo")
  print("4. Exit")
  print()
  choice = int(input("Enter choice: "))
  os.system("cls")
  if choice == 1:
    addTodo()
    os.system("cls")
  elif choice == 2:
    deleteTodo()
    os.system("cls")
  elif choice == 3:
    viewTodo()
    time.sleep(2)
    os.system("cls")
  elif choice == 4:
    break
  else:
    print("Invalid choice")