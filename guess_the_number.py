import random

number = random.randint(1,100) 

while True:
  try:
    guess = int(input('Guess a number between range 1-100: '))
    if guess < number : print('Too low')
    elif guess > number : print('Too High')
    else : 
      print('Congratulations !! Correct guess !!') 
      break
  except ValueError:
    print('Please enter a valid number')