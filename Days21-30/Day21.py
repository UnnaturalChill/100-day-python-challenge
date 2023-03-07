print("Math Game")
print()

multiples = int(input("Name your multiples: "))

for i in range(1, 11):
  Q1 = int(input(f"{i} x {multiples} = "))
  if Q1 % multiples == 0:
    print(f"{i} x {multiples} = {Q1}")