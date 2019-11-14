from random import randint
from gameFunctions import winlose
from gameFunctions import config
from gameFunctions import mod

global player_lives
global computer_lives

player_lives = config.player_lives
computer_lives = config.computer_lives

choices = ["rock", "paper", "scissors"]

computer = choices[randint(0,2)]

player = False

while player is False:
	print("  =================================================")
	print("  =                                               =")
	print("  =                 - COMPUTER -                  =")
	print("  =                    ", computer_lives, "/ 5                     =")
	print("  =                  - PLAYER -                   =")
	print("  =                    ", player_lives, "/ 5                     =")
	print("  =                                               =")
	print("  =         First player to 0 lives loses!        =")
	print("  =                                               =")
	print("  =================================================\n")

	#print("\n       If you are done playing, type 'quit'.\n")
	player = input("\n \n                  Choose your weapon!              \n\n               (rock, paper or scissors)          \n \n \n                  Type your choice: \n \n                         ")
	player = player.lower()

	if player.lower() == "quit":
		print("\n             Thank you for playing. Goodbye!")
		exit()

	elif computer == player: 
		print("\n \n \n \n \n \n \n \n \n                  Computer chose:", computer, "\n")
		print("        It's a tie! No one loses life. Try again. \n") 

	elif player.lower() == "rock":
		if computer == "paper":
			print("\n \n \n \n \n \n \n \n \n                 Computer chose:", computer, "\n")
			print("              You lost!", computer, "covers", player,"\n")
			print("                    You lost a life. \n")
			player_lives = player_lives -1
		else:
			print("\n \n \n \n \n \n \n \n \n                Computer chose:", computer, "\n")
			print("            You won!", player, "smashes", computer, "\n")
			print ("                 Computer lost a life.\n")
			computer_lives = computer_lives -1

	elif player.lower() == "paper":
		if computer == "scissors":
			print("\n \n \n \n \n \n \n \n \n                Computer chose:", computer, "\n")
			print("             You lost!", computer, "cuts", player,"\n")
			print("                    You lost a life.\n")
			player_lives = player_lives -1
		else:
			print("\n \n \n \n \n \n \n \n \n                  Computer chose:", computer, "\n")
			print("               You won!", player, "covers", computer, "\n")
			print("                  Computer lost a life.\n")
			computer_lives = computer_lives -1

	elif player.lower() == "scissors":
		if computer == "rock":
			print("\n \n \n \n \n \n \n \n \n                  Computer chose:", computer, "\n")
			print("             You lost!", computer, "smashes", player,"\n")
			print("                   You lost a life.\n")
			player_lives = player_lives -1
		else:
			print("\n \n \n \n \n \n \n \n \n                 Computer chose:", computer, "\n")
			print("              You won!", player, "cuts", computer, "\n")
			print("                  Computer lost a life.\n")
			computer_lives = computer_lives -1
	
	else:
		print("        That's not a valid choice, try again")

	input("               Press any key to continue. \n \n \n \n \n \n \n \n \n \n")

	if player_lives is 0: 
		# the only way I could get the lives to reset properly
		# was to reset the lives here, before calling the winlose function
		player_lives = config.player_lives
		computer_lives = config.computer_lives
		winlose.winorlose("lost")

	elif computer_lives is 0: 
		player_lives = config.player_lives
		computer_lives = config.computer_lives
		winlose.winorlose("win")

	player = False
	computer = choices[randint(0,2)]