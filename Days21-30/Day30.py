print("30 Days of Code. How are you feeling?\n")

for i in range(1, 31):
  feelings = input(f"Day {i}: ")
  print()
  text = f"You thought Day {i} was"
  print(f"{text:^35}")
  print(f"{feelings:^35}")
  print()