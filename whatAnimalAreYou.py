#!/usr/bin/env python3

land = ['wolf','cheetah']
water = ["shark","dolphin"]
air = ["hawk","peacock"]

while True:
	print("") # blank line for spacing
	user_input = input("Do you even like animals? Yes or No : ")
	print("") # blank line for spacing
	if user_input.lower() == "yes":
		print("there is hope for you yet.")
		print("") #spacing
		print("Let's find out which animal you prefer.")

		while True:
			print(land,water,air)
			animal_type = input("Which animal? ")
			if animal_type.lower() == "wolf":        #or "cheetah":
				print("")#making space
				print("You are a pack leader!")
				break
			elif animal_type.lower() == "cheetah":
				print("")
				print("You are ridicously fast!")			
				break

			elif animal_type.lower() == "shark":    # or "dolphin" or "alligator":
				print("") #making space
				print("Sharks can be sneaky sometimes!")
				break
			elif animal_type.lower() == "dolphin":    # or "dolphin" or "alligator":
                                print("") #making space
                                print("You sure love the water don't you?!")
                                break

			elif animal_type.lower() == "hawk":     #or "robin":
				print("") #spacing
				print("You command the skies. Spread your wings and fly!!!")
				break
			elif animal_type.lower() == "peacock":    # or "dolphin" or "alligator":
                                print("") #making space
                                print("You're a peacock. You have wings. You have to spread your wings and fly!")
                                break

			else:
				print("")
				print("Please select one of the following animals provided.")
				#print(land,water,air)

	elif user_input.lower() == "no":
		print("There is no hope for you...begone mortal.")
		break

	else:
		print("Try typing 'yes' or 'no' next time. It's not that hard.")
		break

	print("") #newline
	print("Wow, so you like "+ animal_type +"s? Could you imagine being such a creature? That would be so epic!")
	break



#user_input = input("


