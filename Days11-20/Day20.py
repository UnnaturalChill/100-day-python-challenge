print("List generator")
print()

startingValue = int(input("Start at: "))
valueToEndBefore = int(input("End before: "))
increment = int(input("Increment between: "))

for i in range(startingValue, valueToEndBefore, increment):
  print(i)