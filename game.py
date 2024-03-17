#import time module to control flow
import time
#start intro and welcome message
land = 'Witwarrth'
print('Welcome to the game, your adventure awaits.')
print('What is your name?')
name = input()
print('Enter your age')
age = int(input())
if(age >= 18):
  print('Lets get started...')
else:
  print('You are not old enough to play')
time.sleep(2)
print("You are transported to an ethereal, mystical land, named " + land)
time.sleep(2)
print('Greetings ' + name + '. ' + 'Here on ' + land + ', ' + 'you have the power to control your fate.')
