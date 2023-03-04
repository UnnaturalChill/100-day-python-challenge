print("-MY LOGIN SYSTEM-")
print("~~~~~~~~~~~~~~~~~")
print()

username = input("Username >\033[32m ")
password = input("\033[0mPassword >\033[32m ")
print("\033[0m")

if username == "Cirno" and password == "strongest":
    print("Welcome back the strongest fairy!")
    print()
    print("You're looking awfully cool today!")

elif username == "Reimu" and password == "shrineMaiden":
    print("Welcome back graceful Shrine maiden!")
    print()
    print("Thank you for your service once again. Hope you got some donations!")
    
elif username == "Marisa" and password == "lastSpark":
    print("Welcome back wise witch!")
    print()
    print("Hope you have a great day borrowing stuff (stealing)!")
    
else:
    print("Get lost youkai! This is no place for someone like you!")