year = 365
leapYear = 366
hours = 24
minutes = 60
seconds = 60

print("How many days are in this year?")
thisYear = int(input("> "))

secondsInAYear = year * hours * minutes * seconds

secondsInALeapyear = leapYear * hours * minutes * seconds

if thisYear == 365:
    print("There are", secondsInAYear, "seconds in a year.")
elif thisYear == 366:
    print("There are", secondsInALeapyear, "seconds in a leapyear.")
else:
    print("That's not how many years there are in a year!")