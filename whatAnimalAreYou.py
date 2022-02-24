#!/usr/bin/env python3

land = ["wolf","cheetah"]
water = ["shark","dolphin","alligator"]
air = ["hawk","robin"]

while True:
	print("") # blank line for spacing
	user_input = input("Do you even like animals? Yes or No : ")
	print("") # blank line for spacing
	if user_input.lower() == "yes":
		print("there is hope for you yet.")
		print("Let's find out what animal you are.")

		while True:
			print(land,water,air)
			animal_type = input("Which animal? ")
			if animal_type.lower() == "wolf" or "cheetah":
				print("")#making space
				print("You are a land animal!")
				break
			elif animal_type.lower() == "shark":
				print("") #making space
				print("You are a lone predator!")
				break
			else:
				print("Please select one of the following animals. 'wolf 				or shark'.")



	elif user_input.lower() == "no":
		print("There is no hope for you...begone mortal.")
		break

	else:
		print("Try typing 'yes' or 'no' next time. It's not that hard.")
		break
	print("") #newline
	print("Wow, so you think you are a",animal_type,",could you imagine being such a creature? You are a dangerous creature!")
	break



#user_input = input("


