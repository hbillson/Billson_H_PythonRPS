from random import randint

choices=["rock", "paper", "scissors"]

player = False

while player is False:

	player=input("choose rock, paper or scissors: \n")
	computer=choices[randint(0,2)]
	print("computer: ", computer, "player: ", player)
	if player == computer: 
		print("tie, no one wins. try again \n") 
	elif player == "quit": 
		print("you chose to quit, quitter.")
		exit()
	elif player == "rock":
		if computer == "paper":
			print ("You lose!", computer, "covers", player,"\n")
		else:
			print("You won!", player, "smashes", computer, "\n")

	elif player == "paper":
		if computer == "scissors":
			print ("You lose!", computer, "cuts", player,"\n")
		else:
			print("You won!", player, "covers", computer, "\n")

	elif player == "scissors":
		if computer == "rock":
			print ("You lose!", computer, "smashes", player,"\n")
		else:
			print("You won!", player, "cuts", computer, "\n")

	player = False
	computer=choices[randint(0,2)]