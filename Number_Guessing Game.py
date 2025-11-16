# Number Guessiong Game

import random
guessed_number = random.randint(1,100)
while True:
 try:
  inp = int(input('Guess the number from 1 to 100: '))
  if inp ==guessed_number:
     print('You guessed the number')
     break
  elif inp < guessed_number:
     print('Too low')
  elif inp > guessed_number:
     print('Too high')
 except ValueError:
  print('Enter a valid number')