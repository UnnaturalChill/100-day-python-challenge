input("Which character are you from the Touhou Project series?")
input("Answer the following questions to find out!")
input('To answer a question make sure to use either "y" or "n".')
input("Let's begin!")
print()

Reimu = input("You like to use magic balls to defeat your enemies: ")
if Reimu == "y":
    print("You are \033[31m Reimu Hakurei \033[0m!")
else: 
    print("Well, not everyone can be the main character!")
print()

Marisa = input("You like to borrow things (steal): ")
if Marisa == "y":
    print("You are \033[33m Marisa Kirisame \033[0m!")
else: 
    print("Yeah maybe that for the better...")
print()

Cirno = input("You like freezing frogs and hate math: ")
if Cirno == "y":
    print("You are \033[34m Cirno \033[0m!")
else: 
    print("Well, not everyone can be based!")