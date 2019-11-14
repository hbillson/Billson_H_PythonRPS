from gameVariables import variables
variables.player_lives = 5
variables.computer_lives = 5

# I have to set local variables within mod.py for 
# the lives, in order to use them as the default values
# in winorlose

player_lives = variables.player_lives
computer_lives = variables.computer_lives