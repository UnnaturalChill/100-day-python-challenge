print("Math Game")
print()

scoreCounter = 0
multiples = int(input("Name your multiples: "))
print()

for i in range(1, 11):
  question = int(input(f"{i} x {multiples} = "))
  if question == i * multiples:
    print("You got it right. Great work!")
    print()
    scoreCounter += 1
  else: 
    print(f"You got it wrong. Right answer is {i * multiples}")
    print()
print(f"You scored {scoreCounter} out of 10")