from random import randint
from gameFunctions import winlose
from gameVariables import variables, mod


def comparing(status):
	if variables.player == "quit":
		print("\n             Thank you for playing. Goodbye! \n\n\n\n")
		exit()

	# the crazy line breaks and spaces makes it look like
	# the points / player choice / results are on
	# separate pages, making the game easier to read

	elif variables.computer == variables.player: 
		print("\n \n \n \n \n \n \n \n \n                  Computer chose:", variables.computer, "\n")
		print("        It's a tie! No one loses life. Try again. \n") 

	elif variables.player == "rock":
		if variables.computer == "paper":
			print("\n \n \n \n \n \n \n \n \n                 Computer chose:", variables.computer, "\n")
			print("              You lost!", variables.computer, "covers", variables.player,"\n")
			print("                    You lost a life. \n")
			variables.player_lives = variables.player_lives -1
		else:
			print("\n \n \n \n \n \n \n \n \n                Computer chose:", variables.computer, "\n")
			print("            You won!", variables.player, "smashes", variables.computer, "\n")
			print ("                 Computer lost a life.\n")
			variables.computer_lives = variables.computer_lives -1

	elif variables.player == "paper":
		if variables.computer == "scissors":
			print("\n \n \n \n \n \n \n \n \n                Computer chose:", variables.computer, "\n")
			print("             You lost!", variables.computer, "cuts", variables.player,"\n")
			print("                    You lost a life.\n")
			variables.player_lives = variables.player_lives -1
		else:
			print("\n \n \n \n \n \n \n \n \n                  Computer chose:", variables.computer, "\n")
			print("               You won!", variables.player, "covers", variables.computer, "\n")
			print("                  Computer lost a life.\n")
			variables.computer_lives = variables.computer_lives -1

	elif variables.player == "scissors":
		if variables.computer == "rock":
			print("\n \n \n \n \n \n \n \n \n                  Computer chose:", computer, "\n")
			print("             You lost!", computer, "smashes", player,"\n")
			print("                   You lost a life.\n")
			variables.player_lives = variables.player_lives -1
		else:
			print("\n \n \n \n \n \n \n \n \n                 Computer chose:", variables.computer, "\n")
			print("              You won!", variables.player, "cuts", variables.computer, "\n")
			print("                  Computer lost a life.\n")
			variables.computer_lives = variables.computer_lives -1
	else:
		print("        That's not a valid choice, try again. \n")

	# asks the player to acknowledge the result by having to 
	# input ENTER/RETURN to continue

	input("                 Press ENTER to continue. \n \n \n \n \n \n \n \n \n \n")
