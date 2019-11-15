from random import randint
from gameVariables import variables, mod

def winorlose(status):
	print ("\n\n\n\n\n\n\n\n\n\n             You", status, "! Would you like to play again?")
	choice = input("                            Y / N\n\n\n\n\n\n\n\n\n\n \n                             ")

	if (choice is "N") or (choice is "n"): 
		print("\n\n\n\n                Thanks for playing! Goodbye!\n\n\n")
		exit()
	elif (choice is "Y" or choice is "y"):
		print ("\n\n\n\n")

		# having these global variables didn't seem to do 
		# anything for me, so i've kept them just as comments

		#global player
		#global computer
		#global choices

		variables.player_lives = mod.player_lives
		variables.computer_lives = mod.computer_lives
		# resetting the changed lives variables to the original value
		# I don't know why this is the only thing that works
		# but it took me a long time to get it working
		# so I won't touch it for now!!

		player = False
		
	else: 
		print("\n\n\n\n          Make a valid choice. Y(es) or N(o)\n\n\n")
		winorlose(status)

