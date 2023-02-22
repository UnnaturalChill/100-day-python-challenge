input("Which character are you from the Touhou Project series?")
input("Answer the following questions to find out!")
input('To answer a question make sure to use either "y" or "n".')
input("Let's begin!")
print()

Reimu = input("You like to use magic balls to defeat your enemies: ")
if Reimu == "y":
    print("You are\033[31m Reimu Hakurei\033[0m!")
else: 
    print("Well, not everyone can be the main character!")
print()

Marisa = input("You like to borrow things (steal): ")
if Marisa == "y":
    print("You are\033[33m Marisa Kirisame\033[0m!")
else: 
    print("Yeah maybe that for the better...")
print()

Cirno = input("You like freezing frogs and hate math: ")
if Cirno == "y":
    print("You are\033[34m Cirno\033[0m!")
else: 
    print("Well, not everyone can be based!")

Sakuya = input("You use pads: ")
if Sakuya == "y":
    print("You are\037[0m Sakuya Izayoi\033[0m!")
else: 
    print("I knew they were real!")
    
Clownpiece = input("You like America: ")
if Clownpiece == "y":
    print("You are\035[0m Clownpiece\033[0m!")
else: 
    print("So you are on the Lunarians side after all!? Junko will not like this...")
    
Remilia = input("You live in a big manshion: ")
if Remilia == "y":
    print("You are\033[0m Remilia Scarlet\033[0m!")
else: 
    print("Sipping tea isn't your thing, eh?")

Flandre = input("You live in a basement: ")
if Flandre == "y":
    print("You are\033[0m Flandre Scarlet\033[0m!")
else: 
    print("You would rather socialize and go outside? Shame.")