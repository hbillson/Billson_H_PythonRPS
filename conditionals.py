# check a temperature and output a result

temperature = int(input("input a number between 0 and 100"))

if temperature <= 4:
	print("water is a solid. cuz it's frozen")

elif temperature < 100: 
	print("water is a liquid") 

else: 
	print("water is a gas. cuz it's boiling")

