#Dice Rolling Game
import random
while True:

  ask1 = input('Roll the Dice?(y/n): ').lower()
  if ask1== "y":
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print(dice1 ,dice2 )

  elif ask1== "n":
    print("Thank you for playing")
    break
  else:
    print("Sorry, you have to roll again")
















