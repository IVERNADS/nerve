# This program is a timer that is customized for the 'Nerve of Steel' game

import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("times-up.jpeg")

print(Welcome to Nerve of Steel game! The last player to sit wins!")

s = str(input("Please enter 's' when you are ready to begin."))

if s==s: 
print("Players stand!")
# a random number is generated by the computer between 5 and 25
set_time = random.randint(5,25)
time.sleep(set_time)
im.show()
print("Time Up.  Last to sit down wins.")
