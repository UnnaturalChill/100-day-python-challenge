import os, time

pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 

listOfEasy    = ['Cat', 'Dog', 'Hat', 'Run', 'Egg', 'Pen', 'Bat', 'Toy', 'Cup', 'Lip']
listOfNormal  = ['Apple', 'Beach', 'Chair', 'Dance', 'Elephant', 'Flower', 'Guitar', 'Hotel', 'Island', 'Jacket']
listOfHard    = ['Anxious', 'Banquet', 'Courage', 'Disguise', 'Elegant', 'Friction', 'Grateful', 'Hypnosis', 'Furtive', 'Juvenile']
listOfExpert  = ['Insecticide', 'Fecundity', 'Ineffable', 'Abstinence', 'Bureaucracy', 'Complacency', 'Gargantuan', 'Exacerbate', 'Juxtapose', 'Incredulous']
listOfMaster  = ['Gargantuan', 'Antediluvian', 'Bourgeoisie', 'Circumlocution', 'Discombobulate', 'Epistemology', 'Grandiloquence', 'Heliocentric', 'Labyrinthine', 'Discrepancy']

def colorWord(color, word):
  if color == 'red':
    color = 31
  elif color == 'green':
    color = 32
  elif color == 'yellow':
    color = 33
  elif color == 'blue':
    color = 34
  elif color == 'purple':
    color = 35
  elif color == 'cyan':
    color = 36
  return f"\033[{color}m{word}\033[0m"

def waitAndClear(seconds, clear):
  if clear == False:
    return time.sleep(seconds)
  else:
    return time.sleep(seconds), os.system('cls')

print("\033[?25l\033[4mWelcome to the Hangman game!\033[0m\n")
print(f"""You will be prompted with a random word and your task is to guess the word right.\nIf you guess the word {colorWord('green', 'correctly')}, you {colorWord('green', 'win')}!\nIf you guess {colorWord('red', 'incorrectly')} too many times the man hangs himself and you {colorWord('red', 'lose')}!""")
print("Good luck!\n")
input("Press enter to continue")
waitAndClear(0.2, True)

print("First, select a difficulty level of your liking\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
difficulty = input(f"> {colorWord('blue', 'Easy')}\n> {colorWord('green', 'Normal')}\n> {colorWord('yellow', 'Hard')}\n> \033[38;5;{209}mExpert\033[0m\n> {colorWord('red', 'Master')}").capitalize().strip()
print(difficulty)