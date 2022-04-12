# My Lottery Program
  # Work in progress 3/8/22
# Todo
  # Add options (done)
  # Add ui (done)
  # Add gui (half done)
  # Loop to Q1 

import turtle
# adds turtle graphics

screen=turtle.Screen()
# idk why I need this :)

screen.setup(372, 429)
# screen size based on jpg pixels

screen.bgpic("lottery.jpg")

from random import shuffle
# adds shuffle function to python

lottery_mega = list(range(1,70))
numbers_mega = []

for i in range (5):
	shuffle (lottery_mega)
	# shuffles the array
	x = lottery_mega.pop ()
	# removes and returns last vale from array/list
	numbers_mega.append(x)
	# adds item to the end of the list (ie the results)

numbers_mega.sort()
# sorts in ascending order ".sort(reverse=True)" for descending

lottery_power = list(range(1,69))
numbers_power = []

for i in range (5):
	shuffle (lottery_power)
	# shuffles the array
	x = lottery_power.pop ()
	# removes and returns last vale from array/list
	numbers_power.append(x)
	# adds item to the end of the list (ie the results)

numbers_power.sort()
# sorts in ascending order ".sort(reverse=True)" for descending

lottery_keno = list(range(1,80))
numbers_keno = []

for i in range (20):
	shuffle (lottery_keno)
	# shuffles the array
	x = lottery_keno.pop ()
	# removes and returns last vale from array/list
	numbers_keno.append(x)
	# adds item to the end of the list (ie the results)

numbers_keno.sort()
# sorts in ascending order ".sort(reverse=True)" for descending
def Q1():
  Q1
Q1=input("Do you want A) Mega Millions Numbers B) Powerball Numbers C) Keno Numbers [A/B/C]?")
#Q1 is question 1 and the input shows up in the prompt
if Q1 == "A" or Q1 == "a":print ("Your Mega Millions Numbers Are", numbers_mega)
elif Q1 == "B" or Q1 == "b":print ("Your Powerball Numbers Are", numbers_power)
elif Q1 == "C" or Q1 == "c":print ("Your Keno Numbers Are", numbers_keno)