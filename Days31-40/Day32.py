import random

greetingsInDifferentLanguages = ["Hei!", "Hola!", "Bonjour!", "Salut!", "Hallo!", "Konnichiwa!", "Guten Tag!"]

# The easier way
randomItemChoice = random.choice(greetingsInDifferentLanguages)
print(randomItemChoice)

# The random number way
randomItemNumber = random.randint(0, 6)
print(greetingsInDifferentLanguages[randomItemNumber])