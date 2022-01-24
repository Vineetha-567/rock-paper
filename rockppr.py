a=input("enter any name")
b=input("enter any name")
if a==b:
	print("both get tie")
elif a=="rock" and b=="scissor":
	print("rock smashes scissor,a win")
elif a=="rock" and b=="paper":
	print("paper covers rock,b win")
elif a=="paper" and b=="scissor":
	print("scissor cuts paper,b win")
elif a=="paper" and b=="rock":
	print("paper covers rock,a win")
elif a=="scissor" and b=="rock":
	print("rock smashes scissor,b win")
elif a=="scissor" and b=="paper":
	print("scissor cuts paper,a win")