import random


choices = ('r','p','s')

while True:
  user = input('Rock, Paper or Scissor ? (r/p/s): ')
  if user not in choices :
    print('Invalid Choice')
    continue

  computer = random.choice(choices)
  print(f'You chose {user}')
  print(f'Computer chose {computer}')

  if(user == computer):
    print('Tie')
  elif(user == 'r' and computer == 's' or
     user == 'p' and computer == 'r' or
     user == 's' and computer == 'p'):
    print('You Win')
  else:
    print('You lose')

  should_continue = input('Continue ? (y/n): ').lower()
  if(should_continue == 'n'):
    break