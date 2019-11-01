from random import randint

def winorlose(status):
	print("called win or lose:", status, "\n")
	print ("You", status, "! Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer

		player_lives = 1
		computer_lives = 1 
		player = False
		computer = choices[randint(0,2)]
	elif choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
	else: 
		print("Make a valid choice. Y(es) or N(o)")

choices=["rock", "paper", "scissors"]

player_lives = 1
computer_lives = 1

player = False

while player is False:
	print("==========================================\n")
	print("Computer Lives:", computer_lives, "/5\n")
	print("Player Lives:", player_lives, "/5\n" )
	print("==========================================\n")

	player=input("choose rock, paper or scissors: \n")
	computer=choices[randint(0,2)]

	if player == computer: 
		print("tie, no one wins. try again \n") 

	elif player == "quit": 
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if computer == "paper":
			print ("You lose!", computer, "covers", player,"\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "paper":
		if computer == "scissors":
			print ("You lose!", computer, "cuts", player,"\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "covers", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "scissors":
		if computer == "rock":
			print ("You lose!", computer, "smashes", player,"\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "cuts", computer, "\n")
			computer_lives = computer_lives -1

	if player_lives == 0: 
		winorlose("lost")
		# print("You lost! Loser. Would you like to play again?")
		# choice = input("Y / N?")

		# if choice == "Y" or choice == "y":
		# 	player_lives = 5 
		# 	computer_lives = 5 
		# 	player = False
		# 	computer = choices[randint(0,2)]
		# elif choice == "N" or choice == "n":
		# 	print("You chose to quit. Better luck next time!")
		# 	exit()
		# else: 
		# 	print("Make a valid choice.")

	elif computer_lives == 0: 
		winorlose("win")
		# print("You won! Would you like to play again?")
		# choice = input("Y / N? ")

		# if choice == "Y" or choice == "y":
		# 	player_lives = 5 
		# 	computer_lives = 5 
		# 	player = False
		# 	computer = choices[randint(0,2)]
		# elif choice == "N" or choice == "n":
		# 	print("You chose to quit. Good job!")
		# 	exit()
		# else: 
		# 	print("Make a valid choice.")

	player = False
	computer=choices[randint(0,2)]