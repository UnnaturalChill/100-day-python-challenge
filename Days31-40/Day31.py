def colorChanger(color):
  if color == "red":
    color = 31
  elif color == "white":
    color = 0
  elif color == "blue":
    color = 34
  elif color == "yellow":
    color = 33
  elif color == "green":
    color = 32
  elif color == "purple":
    color = 35
  else:
    color = 0
  return f"\033[{color}m"

title = f"{colorChanger('red')}={colorChanger('white')}={colorChanger('blue')}= {colorChanger('yellow')}Music App {colorChanger('blue')}={colorChanger('white')}={colorChanger('red')}="
prev = "prev"
next = "next"
pause = "pause"

print(f"            {title:^35}\n")
print(f"🔥▶️\t{colorChanger('white')}Radio Gaga")
print(f"\t{colorChanger('yellow')}Queen\n\n")

print(f"{colorChanger('white')}{prev:<15}")
print(f"{colorChanger('green')}{next:^15}")
print(f"{colorChanger('purple')}{pause:>15}")

print("\n\n")
welcomeText = "WELCOME TO"
name = "--  ARMBOOK  --"
text1 = "Definitely not a rip off"
text2 = "a certain other social"
text3 = "networking site"
text4 = "Honest."
username = "Username: "
password = "Password: "
print(f"{colorChanger('white')}{welcomeText:^35}")
print(f"{colorChanger('blue')}{name:^35}")
print(f"{colorChanger('yellow')}{text1:>35}")
print(f"{colorChanger('yellow')}{text2:>35}")
print(f"{colorChanger('yellow')}{text3:>35}")
print(f"{colorChanger('red')}{text4:^35}\n")
username = print(f" {colorChanger('white')}{username:^35}")
username = print(f" {colorChanger('white')}{password:^35}")