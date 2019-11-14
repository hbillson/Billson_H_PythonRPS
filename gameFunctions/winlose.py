from random import randint
from gameFunctions import config
from gameFunctions import mod

def winorlose(status):
	#print("called win or lose:", status, "\n")
	print ("             You", status, "! Would you like to play again?")
	choice = input("                            Y / N \n                             ")
	print(choice)

	if (choice is "N") or (choice is "n"): 
		print("You chose to quit.")
		exit()
	elif (choice is "Y" or choice is "y"):
		print ("\n\n\n\n")

		global player_lives
		global computer_lives
		global player
		global computer
		global choices
		# I could not for the life of me get the 
		# lives variables to reset using the winorlose
		# function
		player_lives = config.player_lives
		computer_lives = config.computer_lives
		player = False
		computer = choices[randint(0,2)]

	else: 
		print("Make a valid choice. Y(es) or N(o)")

choices=["rock", "paper", "scissors"]