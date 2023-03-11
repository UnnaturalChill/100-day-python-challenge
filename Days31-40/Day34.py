import os, random, time
listOfEmail = []

def prettyPrint():
  os.system("cls") 
  print("\033[?25lList of emails:") 
  for index in range(len(listOfEmail)): 
    print(f"{index}. {listOfEmail[index]}") 
  print()
  time.sleep(1)

def spamList(maxEmails):
  os.system("cls")
  for i in range(0, maxEmails):
    randomEmails = [
    f"\033[?25lHi {listOfEmail[i]},\nAre you free for lunch today? Let's grab a bite together if you're available.\n\nBest,\nJohn", 
    f"\033[?25lHi {listOfEmail[i]},\nJust a friendly reminder that the project deadline is coming up soon. Let's make sure we stay on track to meet it.\n\nThanks,\nKaren",
    f"\033[?25lHi {listOfEmail[i]},\nWishing you a very happy birthday! Hope you have a wonderful day filled with joy and celebration.\n\nBest,\nEmily",
    f"\033[?25lHi {listOfEmail[i]},\nDue to unforeseen circumstances, we'll need to reschedule the meeting originally planned for tomorrow. Please look out for an updated schedule.\n\nThanks,\nMike",
    f"\033[?25lHi {listOfEmail[i]},\nWe're currently hiring for a new position on our team. Please let me know if you're interested or know someone who might be a good fit.\n\nBest,\nAlex",
    f"\033[?25lHi {listOfEmail[i]},\nJust wanted to say congratulations on your recent promotion! Well deserved and I know you'll excel in your new role.\n\nCheers,\nSam",
    f"\033[?25lHi {listOfEmail[i]},\nI'm having some trouble with the new software we're using. Can you give me a hand with it when you have a moment?\n\nThanks,\nMark",
    f"\033[?25lHi {listOfEmail[i]},\nI wanted to thank you for all your help on the project. Your contributions were instrumental in its success.\n\nBest,\nJulie",
    f"\033[?25lHi {listOfEmail[i]},\nDon't forget about the team building event scheduled for next week! Looking forward to seeing you all there.\n\nCheers,\nLaura",
    f"\033[?25lHi {listOfEmail[i]},\nAs you know, we're currently raising funds for our annual charity drive. Please consider making a donation if you haven't already. Every little bit helps!\n\nThanks,\nKim"
    ]
    randomText = random.choice(randomEmails)
    print(f"Email {i + 1}.\n\n{randomText}")
    time.sleep(2)
    os.system("cls")

while True:
  print("\033[?25hSPAMMER Inc.\n")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n5. Exit\n> ")
  if menu == "1":
    time.sleep(.2)
    os.system("cls")
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    time.sleep(.2)
    os.system("cls")
    prettyPrint()
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    spamList(10)
  elif menu == "5":
    os.system("cls")
    break
  else:
    print("Invalid input")
  time.sleep(.5)
  os.system("cls")