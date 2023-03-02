from getpass import getpass as input

print("Rock, Paper, Scissors game")
print()

print("Select your move (R, P, S)")
print()

player1 = input("Player 1's choice > ")
print()
player2 = input("Player 2's choice > ")
print()

if player1 == "R" and player2 == "R":
  print("It's a tie!")
elif player1 == "P" and player2 == "P":
  print("It's a tie!")
elif player1 == "S" and player2 == "S":
  print("It's a tie!")
elif player1 == "R" and player2 == "P":
  print("Player 2 wins!")
elif player1 == "P" and player2 == "S":
  print("Player 2 wins!")
elif player1 == "S" and player2 == "R":
  print("Player 2 wins!")
elif player1 == "R" and player2 == "S":
  print("Player 1 wins!")
elif player1 == "P" and player2 == "R":
  print("Player 1 wins!")
elif player1 == "S" and player2 == "P":
  print("Player 1 wins!")
elif player2 == "R" and player1 == "P":
  print("Player 1 wins!")
elif player2 == "P" and player1 == "S":
  print("Player 1 wins!")
elif player2 == "S" and player1 == "R":
  print("Player 1 wins!")
elif player2 == "R" and player1 == "S":
  print("Player 2 wins!")
elif player2 == "P" and player1 == "R":
  print("Player 2 wins!")
elif player2 == "S" and player1 == "P":
  print("Player 2 wins!")
else: print("It has to be R, P or S")