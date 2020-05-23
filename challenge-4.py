from random import randint

rn = randint(0, 100)
count = 0

while count < 20:
  print("What is your number?")
  wans = input()
  ans = int(wans)
  if ans > rn:
    print("Too high!")
  elif ans < rn:
    print("Too low!")
  elif ans == rn:
    print("You got it!")
  count = count + 1
  
