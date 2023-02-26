print("Generation Identifier")
print()

print("Which year were you born?")
birthYear = int(input("> "))
print()

if birthYear < 1883 or birthYear > 2024:
    print("You're either long dead or not even born at all!")

if birthYear >= 1883 and birthYear <= 1900:
    print("You are part of the Lost Generation!")

if birthYear >= 1901 and birthYear <= 1927:
    print("You are part of the Greatest Generation!")

if birthYear >= 1928 and birthYear <= 1945:
    print("You are part of the Silent Generation!")
    
if birthYear >= 1946 and birthYear <= 1964:
    print("You are part of the Baby Boomers!")

if birthYear >= 1965 and birthYear <= 1980:
    print("You are part of the Generation X!")

if birthYear >= 1981 and birthYear <= 1996:
    print("You are part of the Millennials!")

if birthYear >= 1997 and birthYear <= 2012:
    print("You are part of the Generation Z!")
    
if birthYear >= 2013 and birthYear <= 2023:
    print("You are part of the Generation Alpha!")