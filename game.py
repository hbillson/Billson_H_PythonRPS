from random import randint

choices=["rock", "paper", "scissors"]

#computer=choices[randint(0,2)]

player = False

while player is False:

	player=input("choose rock, paper or scissors: \n")
	computer=choices[randint(0,2)]
	print("computer: ", computer, "player: ", player)
	if player == computer: 
		print("tie, no one wins. try again") 
	elif player == "quit": 
		print("you chose to quit, quitter.")
		exit()
	else: 
		print("NOT a tie. now we can check other conditions")
		if player == "rock":
			print("check and see what the computer is, and win or lose")

	player = False
	computer=choices[randint(0,2)]