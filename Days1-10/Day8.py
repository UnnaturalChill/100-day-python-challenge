print("Wholesome positivity machine")
print()

name = input("What's your name? >\033[35m ")        # Name is purple 35
print()

achievements = input("\033[0mWhat do you want to achieve? >\033[34m ")      # Achievement is blue
print()

happinessScale = input("\033[0mOn a scale of 1-10 how are you feeling today,\033[35m " + name + "\033[0m? >\033[32m ")      # Scale is green
print()

if achievements == "Learn to code" and happinessScale == "10":
    print("\033[0mHey\033[35m " + name + "\033[0m. Good to hear feeling good today and wanting to learn to code. You can totally do it! You are amazing!")
else: print("\033[0mVery cool!")