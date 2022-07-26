# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Dave Dworak
# Creation Date: 7/25/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

# 1) The print call below is enclosed in triple single-quotes. Typically used
# for multi-line comments. Recommend using single or double quote
# 2) The same print call is indented in a manor that makes lines appear odd when running
def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = '' # 3) this is indented with spaces instead of tab, which causes an error
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return caves # 4) caves should be cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3) # 5) The argument should be 2 to match above comment, or change comment to reflect the argument
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!' # 6) This print call is missing the enclosing parentheses

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y': # 7) Both of these conditions need a double "=" as they are strings
	displayIntro()
	caveNumber = choosecave() # 8) The c in choosecave needs to be capitalized (chooseCave)
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no": # 9) This condition requires "no" for the print call. Recommend using the oppositte condition of above like, "if playAgain != 'yes' or playAgain != 'y':"
		print("Thanks for planing") # 10) Typo - "planing" to "playing"

