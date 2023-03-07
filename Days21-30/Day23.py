def replitLogin():
  while True:
    username = input("Username: ")
    password = input("Password: ")
    print()
    if username == "admin" and password == "admin":
      print("REPLIT LOGIN SUCCESSFUL")
      break
    else:
      print("REPLIT LOGIN FAILED")
      continue

print("REPLIT LOGIN SYSTEM")
print()
replitLogin()