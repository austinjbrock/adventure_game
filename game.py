#import time module to control flow
import time
#start intro and welcome message
land = 'Witwarrth'
print('Welcome to the game')
name = input('What is your name? ')
age = int(input("What is your age? "))
health = 80

print('Hello ', name ,' you are ', age, ' years old')

if(age >= 18):
  print('You are old enough to play')
  wants_to_play = input('Do you want to play? ').lower()
  if(wants_to_play == "yes"):
    print('Here we go...')

  left_or_right = input('First path choice... Left or Right (left/right)? ')
  if left_or_right == "left":
    answer = input("You follow the left path and stumble upon a sunny meadow... Do you continue walking or stop to rest? (walk/rest)")
    
    if answer == "walk":
      health == health - 10
      print('your health has been reduced by 10.')
      print('your health is now :' + str(health))
    elif answer == "rest":
      health == health + 20
      print('You regained your health to 100%')

  else:
    answer = input("You decided to wander down the right path, and you arrive at a lagoon. Do you swim across, or walk around?(swim/walk around)")

  time.sleep(2)
  print("You are transported to an ethereal, mystical land, named " + land)
  time.sleep(2)
  print('Here in ' + land, 'your fate is determined by your choice of direction... choose wisely.')

else:
  print('You are not old enough to play')
