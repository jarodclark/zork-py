import items

def Play_Zork():
	loop = 4
	print("---------------------------------------------------------")
	print("Welcome to Zork - The Unofficial Python Version.")
	return loop

def exit_function(exit_inp):
        if exit_inp.lower() == ("n"):
                exit()
        if exit_inp.lower() == ("y"):
                Play_Zork()

def room4(second, itemList):

        if second.lower() == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
        elif second.lower() == ("open mailbox"):
                print("---------------------------------------------------------")
                print("Opening the small mailbox reveals a leaflet.")
        elif second.lower() == ("go north"):
                loop = 1
        elif second.lower() == ("open door"):
                print("---------------------------------------------------------")
                print("The door cannot be opened.")
        elif second.lower() == ("take boards"):
                print("---------------------------------------------------------")
                print("The boards are securely fastened.")
        elif second.lower() == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
        elif second.lower() == ("go southwest"):
                loop = 8
        elif second.lower() == ("read leaflet"):
                print("---------------------------------------------------------")
                print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
        elif second.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        Play_Zork()
        else:
                print("---------------------------------------------------------")          
        return loop

def room1(north_house_inp, itemList):

        if north_house_inp.lower() == ("go south"):
                loop = 4
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
        elif north_house_inp.lower() == ("fish"):
                print("---------------------------------------------------------")
                print("You spend some time fishing but nothing seems to bite.")
        elif north_house_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        Play_Zork()
        else:
                print("---------------------------------------------------------")
                
        return loop

def room8(user_input, itemList):

        if forest_inp.lower() == ("go west"):
                print("---------------------------------------------------------")
                print("You would need a machete to go further west.")
        elif forest_inp.lower() == ("go north"):
                print("---------------------------------------------------------")
                print("The forest becomes impenetrable to the North.")
        elif forest_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("Storm-tossed trees block your way.")
        elif forest_inp.lower() == ("go east"):
                loop = 9
        elif forest_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        Play_Zork()
        else:
                print("---------------------------------------------------------")
        return loop

def room9(user_input, itemList):

        if grating_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("You see a large ogre and turn around.")
        elif grating_inp.lower() == ("descend grating"):
                loop = 10
        elif grating_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        Play_Zork()
        else:
                print("---------------------------------------------------------")

        return loop

def room10(user_input, itemList):

        if cave_inp.lower() == ("descend staircase"):
                loop = 11
        elif cave_inp.lower() == ("take skeleton"):
                print("---------------------------------------------------------")
                print("Why would you do that? Are you some sort of sicko?")
        elif cave_inp.lower() == ("smash skeleton"):
                print("---------------------------------------------------------")
                print("Sick person. Have some respect mate.")
        elif cave_inp.lower() == ("light up room"):
                print("---------------------------------------------------------")
                print("You would need a torch or lamp to do that.")
        elif cave_inp.lower() == ("break skeleton"):
                print("---------------------------------------------------------")
                print("I have two questions: Why and With What?")
        elif cave_inp.lower() == ("go down staircase"):
                loop = 11
        elif cave_inp.lower() == ("scale staircase"):
                loop = 11
        elif cave_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        Play_Zork()
        elif cave_inp.lower() == ("scale staircase"):
                loop = 11
        else:
                print("---------------------------------------------------------")

        return loop

def room11(user_input, itemList):

        if last_inp.lower() == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest!")
        elif last.inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        Play_Zork()
        else:
                print("---------------------------------------------------------")

        return loop


##	while True:
##		# First Input Loop
##		while loop == 4:
##			room4(user_input, [])
##
##		# North of House
##		while loop == 1:
##			room1(user_input, [])
##
##		# Southwest Loop
##		while loop == 8:
##			room8(user_input, [])
##		
##
##		# East Loop and Grating Input
##		while loop == 9:
##                        room9(user_input, [])
##
##
##		# Grating Loop and Cave Input
##		while loop == 10:
##		
##		# End of game
##		while loop == 11:
##			room11(user_input, [])
##			
##			# Exit loop at the end of game
##			exit_inp = input("Do you want to continue? Y/N ")
##			if exit_inp.lower() == ("n"):
##				exit()
##			if exit_inp.lower() == ("y"):
##				Play_Zork()
