#Treasure Island game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
option = input("You're at a crossroad, choose which way to go. Left or Right\n")
if option =="Left":
	option2 = input("You've come to a lake with an island in the middle, choose Swim  across or Wait for a boat\n")
	if option2=="Wait for a boat":
		option3=input("You arrive at the island, there's three doors. choose Red, Blue, Yellow\n")
		if option3=="Red":
			print("You entered a room full of beasts. Game Over")
		elif option3=="Yellow":
			print("You found the treasure. You win")
		elif option3=="Blue":
			print("You entered a room stacked with swords. Game Over")
		else:
			print("Door does not exist. Game Over")
	else:
		print("You are eaten by sharks. Game Over")
else:
	print("You entered an ogre's cave. Game Over")
			

#Python chatbox
print("Hello, welcome to the python chatbox!!")
query1= input("Are you excited to interact with the program? Enter yes or no\n")
if query1=='yes':
	query2 = int(input("How old are you?\n"))
	if query2 <=17:
		print("Sorry this is not appropriate for you")
	else:
		query3=input("How are you feeling today?? enter good,nice, elated,okay,happy,angry,sad,lonely,pressured,frustrated\n")
		if query3=="good" or query3=="okay" or query3=="happy" or query3=="elated":
			print("Shine on you got this!!")
		elif query3=="angry" or query3=="frustrated" or query3=="agitated" or query3=="on edge":
			print("Take a deep breath everything is going to be okay")
			query4= input("Would you like to speak to our counsellor? Type yes or no\n")
			if query4=="yes":
			 category=input("Please state category: Family, work, personal\n")
			if category=="Family":
				print("Call 555")
			elif category=="work":
				print("Call 777")
			elif category=="personal":
				print("Call 888")
			else:
				print("Call 999")
		elif query3=="sad" or query3=="lonely" or query3=="blue":
			print("Hugs and cuddles. You are not alone")
		else:
			print("The power is within you.Smile!!")
			
else:
	print("Maybe try again later")
		
		