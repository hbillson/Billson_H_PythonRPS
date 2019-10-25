from random import randint

choices=["rock", "paper", "scissors"]

# comparing computer and player worked in both versions of my game when:
#    - both values are ints (player input is 0-2)
#    - i changed both values to '(input("choose rock, paper or scissors")'
#    - when i moved the computer=choices value to inside the loop
#      instead of at the top


player = False

while player is False:

	player=(input("choose rock, paper or scissors for player \n"))
	if player == "quit": 
		print("goodbye")
		exit()

	computer=choices[randint(0,2)]

	print("computer:", computer, "player:", player)

	if computer == player: 
		print("tie. no one wins, play again \n")
	else:
		print("not a tie. check result and determine who wins \n")

	player = False 
