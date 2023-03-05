print("Loan calculator")
print()
print("1000€ over 10 years at 5% APR")
print()

loan = 1000
apr = 0.05

for i in range(1, 11):
  loan += (loan * apr)
  print(f"Year {i} is {round(loan, 2)}")

print(f"You paid", round(loan - 1000, 2))