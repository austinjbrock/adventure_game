#import time module to control flow
import time
#start intro and welcome message
land = 'Witwarrth'
print('Welcome to the game')
name = input('What is your name? ')
age = int(input("What is your age? "))
health = 100

print('Hello ', name ,' you are ', age, ' years old')

if(age >= 18):
  print('You are old enough to play')
  wants_to_play = input('Do you want to play? ').lower()
  if(wants_to_play == "yes"):
    print('Here we go...')
  time.sleep(2)
  print("You are transported to an ethereal, mystical land, named " + land)
  time.sleep(1)
  print('Here in ' + land, 'your fate is determined by your choice of direction... choose wisely.')


    #player chooses left path...
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


  #player chooses the right path
  else:
    answer = input("You decided to wander down the right path, and you arrive at a lagoon. Do you swim across, or walk around?(swim/walk around)")
    if answer == "swim":
      print('While swimming across, you were attacked by a creature with long fangs, but you escaped...')
      print('Health after the attack is ' + str(health))
      time.sleep(1)
      print('A wizard appears out of thin air to award your bravery. You have recieved a protien snack to restore your health')
      print('Your health is now ' + str(health))
    
    answer = input('You have reached the base of a mountain... you can climb over, costing you 20 health points, or you can walk left, and head through the enchanted forest.')
    if answer == "walk":
      print('You have walked around the lagoon, but with all of that cardio, your health has been dropped down by 10')
      time.sleep(1)
    elif answer == 'climb':
      print('You have sucessfully climbed the mountain and reached the summit. You are greeted by many wizards who will provide you will essentials and food to continue your journey.')
      print('Health is now at ' + str(health) + ' after the food and essentials')
  #works until this point. will continue the journey...
  
  
    # if answer == 'climb':
    #   health == health -20
    # # else: answer == 'walk'
    # # print('You have decided to venture through the enchanted forest. You made it through with ease, and will be rewared for your courage.')

else:
  print('You are not old enough to play')
