print("Exam Grade Calculator")
print()

input("What is the name of the exam? > ")
print()
maxPossibleScore = int(input("What is the maximum possible score? > "))
print()
yourScore = int(input("What is your score? > "))
print()

percentage = (yourScore / maxPossibleScore) * 100
letterGrade = ""

if percentage >= 90:
  letterGrade = "A+"
elif percentage >= 80 or percentage <= 89:
  letterGrade = "A"
elif percentage >= 70 or percentage <= 79:
  letterGrade = "B"
elif percentage >= 60 or percentage <= 69:
  letterGrade = "C"
elif percentage >= 50 or percentage <= 59:
  letterGrade = "D"
elif percentage < 50:
  letterGrade = "U"
else:
  print("You have entered an invalid score.")
print()

print("You got", round(percentage, 2), "% which is a(n)", letterGrade)