print("I'll write a story for you!")
print("Answer the questions and check the story you created!")
print()

placeName = input("Give your world a name: ")
characterName = input("Give your character a name: ")
characterLocation = input("Give your characters location in the world: ")
anotherCharacterLocation = input("Give another location: ")


print(" A long long time ago in a faraway land Called", "\033[32m", placeName, "\033[0m", "there was a fairy called", "\033[36m", characterName, ".", 
    "\033[0m", "They liked to freeze frogs at the", "\033[34m", characterLocation, "\033[0m", "near the", "\033[31m", anotherCharacterLocation, ".")