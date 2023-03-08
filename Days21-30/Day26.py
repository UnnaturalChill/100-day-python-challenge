import os, time

# Code only works on Replit
def play():
  source = audio.play_file('audio.wav')
  source.paused = False
  while True:
    stopAudio = int(input("Press 2 to go back > "))
    if stopAudio == 2:
      source.paused = True
      return
    else:
      continue


while True:
  os.system("clear")
  print("MyPOD Music Player")
  print()
  
  time.sleep(1)
  print("Press 1 to Play")
  print("Press 2 to Exit")
  time.sleep(1)
  
  print()
  print("Press anything else to see the menu again")
  print()
  
  userInput = input("")
  if userInput == "1":
    play()
  elif userInput == "2":
    break
  else:
    continue