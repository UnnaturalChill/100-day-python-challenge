from getpass import getpass as input

input("Rock, Paper, Scissors game")
print()

print("Firstly select your player names!")
player1name = input("Player 1's name > ")
player2name = input("Player 2's name > ")

player1Wins = 0
player2Wins = 0

while True:
  print()
  if player1Wins > 0 or player2Wins > 0:
    print(player1name, "wins:", player1Wins)
    print(player2name, "wins:", player2Wins)
  if player1Wins == 3:
    print()
    print(player1name, "wins! Congratulations!")
    break
  if player2Wins == 3:
    print()
    print(player2name, "wins! Congratulations!")
    break
  
  print()
  print("Select your move (R, P, S)")
  player1 = input(player1name + "'s choice > ")
  player2 = input(player2name + "'s choice > ")
  print()
  
  if player1 == "R":
    if player2 == "R":
      print("You both picked Rock, it's a draw!")
      continue
    elif player2 == "S":
      print(player1name, "smashed", player2name + "'s Scissors into dust with their Rock!")
      player1Wins += 1
      continue
    elif player2 == "P":
      print(player1name, "'s Rock is smothered by", player2name + "'s Paper!")
      player2Wins += 1
      continue
    else:
      print("Invalid Move", player2name + "!")
      continue
  elif player1 == "P":
    if player2 == "R":
      print(player2name + "'s Rock is smothered by", player1name + "'s Paper!")
      player1Wins += 1
      continue
    elif player2 == "S":
      print(player1name + "'s Paper is cut into tiny pieces by ", player2name + "'s Scissors!")
      player2Wins += 1
      continue
    elif player2 == "P":
      print("Two bits of paper flap at each other. Disappointing. it's a draw!")
      continue
    else:
      print("Invalid Move", player2name + "!")
      continue
  elif player1 == "S":
    if player2 == "R":
      print(player2name + "'s Rock makes metal-dust out of", player1name + "'s Scissors")
      player2Wins += 1
      continue
    elif player2 == "S":
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! it's a draw!")
      continue
    elif player2 == "P":
      print(player1name + "'s Scissors make confetti out of", player2name + "'s paper!")
      player1Wins += 1
      continue
    else:
      print("Invalid Move", player2name + "!")
      continue
  else:
    print("Invalid Move", player1name + "!")
    continue
input("Press Enter to exit...")