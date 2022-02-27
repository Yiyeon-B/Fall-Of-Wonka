


import sys
import time

x = 4
z = 2
a = 1.0
b = 0.7
c = 0.04
d = 0.02

s = "The oompa loompas encircle you, trapping you in Wonka's factory. "
print()
print()
for char in s:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(d)
time.sleep(b)
t = "Their intentions are unknown."
for char in t:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(d)
print()
print()

time.sleep(a)
answer = input("CONQUER or FLEE? ")

if answer.lower().strip() == "conquer":
print()
s = "You have dethroned Wonka. You now own the means of production."
for char in s:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(d)
time.sleep(a)
print()
print()
s = "The oompa loompas reverently place in front of you a throne of candy canes, licorice, and burned dolls."
for char in s:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(d)
time.sleep(a)
print()
print()
s = "Before taking a seat, you glance over your shoulder at your glorious candy kingdom. "
for char in s:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(d)
time.sleep(a)
s = "Then you look back at the throne."
for char in s:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(d)
time.sleep(z)
s = "A sense of unease settles over you."
print()
print()
for char in s:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(d)
time.sleep(z)
print()
print()
answer = input("SIT or FLEE? ")

if answer.lower().strip() == "sit":
  print()
  s = "You place your hands on the armrests and slowly lower yourself upon your throne. "
  for char in s:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(d)
  time.sleep(b)
  s = "The soft, sticky candy and melted plastic gives to your weight."
  for char in s:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(d)
  time.sleep(a)
  print()
  print()
  s = "And continues to give."
  for char in s:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(d)
    time.sleep(b)
  print()
  print()
  s = "You keep sinking."
  for char in s:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(d)
  time.sleep(b)
  print()
  print()
  s = "Candy oozes through the spaces between your fingers. "
  for char in s:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(d)
  time.sleep(b)
  s = "A single plastic eyeball falls into your lap."
  for char in s:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(d)
  time.sleep(b)
  s =" It stares up at you accusingly."
  for char in s:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(d)
  time.sleep(z)
  print()
  print()
  answer = input("Continue to SIT or FLEE? ")
  
  if answer.lower().strip() == "sit":
    print()
    s = "You continue to sink. "
    for char in s:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(d)
    time.sleep(b)
    s = "The last thing you see is the chocolate waterfall, slowly churning, before you become the throne. "
      for char in s:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(d)
    time.sleep(b)
    s = "Such is the price of power."
    for char in s:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(d)
    time.sleep(b)
    
  else:
    print()
    s = "You try to push yourself up but your only leverage is the throne itself. Your attempt to escape only sinks you deeper into it. The oompa loompas watch you struggle dispassionately. "
    for char in s:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(d)
    time.sleep(b)
    print()
    print()
    s = "The last thing you witness is the oompa loompas fanning out into a circle, with you at the very center, as they begin composing a song about your downfall..."
    for char in s:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(d)
    time.sleep(b)
 
  elif answer.lower().strip() == "flee":
    print()
    s = "Was this choice born of cowardice or wisdom?"
    for char in s:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(d)
    time.sleep(b)
    print()
    print()
    s = "Only time will tell as you escape into the depths of the Chocolate Factory..."
    for char in s:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(d)
    time.sleep(b)

  else:
    print(" ")
    print("Eliminated.")

elif answer.lower().strip() == "flee":
  print()
  s = "Was this an act of cowardice? Or wisdom?"
  for char in s:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(d)
  time.sleep(b)
  print()
  print()
  s = "Only time will tell as you escape into the depths of the Chocolate Factory..."
  for char in s:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(d)
  time.sleep(b)

else:
  print(" ")
  print("Eliminated.")
