print("Star wars name generator\n")

firstName = input("Enter your first name: ").strip()
lastName = input("Enter your last name: ").strip()
maidenName = input("Enter your mum's maiden name: ").strip()
bornCity = input("Enter your born city: ").strip()

starWarsName = f"{firstName[0:3].capitalize()}{lastName[0:2].lower()} {maidenName[0:2].capitalize()}{bornCity[-3:].lower()}"
print(f"\nYour Star Wars name is: {starWarsName}")