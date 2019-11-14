from random import randint
from gameFunctions import winlose, compare
from gameVariables import variables, mod

choices = ["rock", "paper", "scissors"]

# naming these variables in the variables file was the only
# way I could get my game to work! 

variables.computer = choices[randint(0,2)]
variables.player = False

while variables.player is False:
	# added a border and spaces to make it prettier

	print("  =================================================")
	print("  =                                               =")
	print("  =                 - COMPUTER -                  =")
	print("  =                    ", variables.computer_lives, "/ 5                     =")
	print("  =                  - PLAYER -                   =")
	print("  =                    ", variables.player_lives, "/ 5                     =")
	print("  =                                               =")
	print("  =         First player to 0 lives loses!        =")
	print("  =                                               =")
	print("  =================================================\n")

	# asking the player for their choice
	# added space and line breaks in the input line to make it prettier 

	variables.player = input("\n \n                  Choose your weapon!              \n\n               (rock, paper or scissors)          \n \n \n                  Type your choice: \n \n                         ")
	print("\n\n\n")

	# calling compare function 
	compare.comparing("playing")

	# making space to make it look better
	print("\n\n\n\n\n\n")

	# calling winlose function

	if variables.player_lives is 0: 
		winlose.winorlose("lost")

	elif variables.computer_lives is 0: 
		winlose.winorlose("win")

	# resetting
	variables.player = False
	variables.computer = choices[randint(0,2)]