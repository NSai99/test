inp = input("Are you hungry ? ")
if(inp.lower() == "yes" or inp.lower() == "y"):
	print("Eat Burger")
else:
	print("Drint Soft Drinks")

[print(i) for i in range(len(inp))] 
