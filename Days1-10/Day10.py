print("Tip calculator")
print()

print("How much did you spend?")
moneySpend = float(input("> "))
print()

print("""How much do you want to tip (1 - 3)?
1. 5%
2. 10%
3. 15%
4. No tip""")
tip = input("> ")

if tip == "1":
    tip = 0.5
elif tip == "2":
    tip = 0.10
elif tip == "3":
    tip = 0.15
elif tip == "4":
    tip = 0
else:
    print("You didn't select one of the options. Try again.")
    tip = 0
print()

print("How many people in your group?")
group = int(input("> "))
print()

total = (moneySpend + moneySpend * tip) / group
print("You each own €", round(total, 2))