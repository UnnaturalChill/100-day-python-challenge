def colorChanger(color, text):
  if color == "red":
    color = 31
  elif color == "green":
    color = 32
  elif color == "yellow":
    color = 33
  elif color == "blue":
    color = 34
  elif color == "magenta":
    color = 35
  else:
    color = 0
  coloredText = print(f"\033[{color}m", f"{text}", "\033[0m", sep="", end="",)
  return coloredText

print("Super Subroutine\n")
print("With my ", end="")
colorChanger("red", "super cool subroutine, ")
colorChanger("green", "i can change the color ")
colorChanger("yellow", "of any text I want. ")
colorChanger("blue", "How cool is that? ")
colorChanger("resetColor", "I can even change it back to normal!")