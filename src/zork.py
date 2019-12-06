import items

def Play_Zork():
        loop = 4
        print("---------------------------------------------------------")
        print("Welcome to Zork - The Unofficial Python Version.")
        return loop

def exit_function(exit_inp):
        if exit_inp.lower() == 'dead':
                exit()

def room4(second, itemList):

        if second.lower() == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
                living_status = 'Alive'
        elif second.lower() == ("open mailbox"):
                print("---------------------------------------------------------")
                print("Opening the small mailbox reveals a leaflet.")
                living_status = 'Alive'
        elif second.lower() == ("go north"):
                loop = 1
                living_status = 'Alive'
        elif second.lower() == ("open door"):
                print("---------------------------------------------------------")
                print("The door cannot be opened.")
                living_status = 'Alive'
        elif second.lower() == ("take boards"):
                print("---------------------------------------------------------")
                print("The boards are securely fastened.")
                living_status = 'Alive'
        elif second.lower() == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
                living_status = 'Alive'
        elif second.lower() == ("go southwest"):
                loop = 8
                living_status = 'Alive'
        elif second.lower() == ("read leaflet"):
                print("---------------------------------------------------------")
                print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
                living_status = 'Alive'
        elif second.lower() == ("going east"):
                loop = 12
                living_status == 'Alive'
        elif second.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                living_status = 'Dead'
                dead_inp = living_status
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")

        return [loop, living_status]

def room1(north_house_inp, itemList):

        if north_house_inp.lower() == ("go south"):
                loop = 4
                living_status = 'Alive'
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
                living_status = 'Alive'
        elif north_house_inp.lower() == ("fish"):
                print("---------------------------------------------------------")
                print("You spend some time fishing but nothing seems to bite.")
                living_status = 'Alive'
        elif north_house_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                living_status = 'Dead'
                dead_inp = living_status
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                
        return [loop, living_status]

def room8(forest_inp, itemList):

        if forest_inp.lower() == ("go west"):
                print("---------------------------------------------------------")
                print("You would need a machete to go further west.")
                living_status = 'Alive'
        elif forest_inp.lower() == ("go north"):
                print("---------------------------------------------------------")
                print("The forest becomes impenetrable to the North.")
                living_status = 'Alive'
        elif forest_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("Storm-tossed trees block your way.")
                living_status = 'Alive'
        elif forest_inp.lower() == ("go east"):
                loop = 9
        elif forest_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                living_status = 'Dead'
                dead_inp = living_status
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
        return [loop, living_status]

def room9(grating_inp, itemList):

        if grating_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("You see a large ogre and turn around.")
                living_status = 'Alive'
        elif grating_inp.lower() == ("descend grating"):
                loop = 10
                living_status = 'Alive'
        elif grating_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                living_status = 'Dead'
                dead_inp = living_status
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")

        return [loop, living_status]

def room10(cave_inp, itemList):

        if cave_inp.lower() == ("descend staircase"):
                loop = 11
                living_status = 'Alive'
        elif cave_inp.lower() == ("take skeleton"):
                print("---------------------------------------------------------")
                print("Why would you do that? Are you some sort of sicko?")
                living_status = 'Alive'
        elif cave_inp.lower() == ("smash skeleton"):
                print("---------------------------------------------------------")
                print("Sick person. Have some respect mate.")
                living_status = 'Alive'
        elif cave_inp.lower() == ("light up room"):
                print("---------------------------------------------------------")
                print("You would need a torch or lamp to do that.")
                living_status = 'Alive'
        elif cave_inp.lower() == ("break skeleton"):
                print("---------------------------------------------------------")
                print("I have two questions: Why and With What?")
                living_status = 'Alive'
        elif cave_inp.lower() == ("go down staircase"):
                loop = 11
                living_status = 'Alive'
        elif cave_inp.lower() == ("scale staircase"):
                loop = 11
                living_status = 'Alive'
        elif cave_inp.lower() == ("going south"):
                loop = 15
                living_status = 'Alive'
        elif cave_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                living_status = 'Dead'
                dead_inp = living_status
                exit_function(dead_inp)
        elif cave_inp.lower() == ("scale staircase"):
                loop = 11
        else:
                print("---------------------------------------------------------")

        return [loop, living_status]

def room11(last_inp, itemList):

        if last_inp.lower() == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest!")
        elif last.inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                dead_inp = input("Do you want to continue? Y/N ")
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")

        return [loop, living_status]

def room12(user_input, itemList):
                
        if user_input.lower() == ("going south"):
                loop = 4
                living_status = 'Alive'
        elif user_input.lower() == ("going west"):
                print("Opening a rickety window you climb into the house.")
        elif user_input.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                living_status = 'Dead'
                dead_inp = living_status
                exit_function(dead_inp)
        else:
              print("---------------------------------------------------------")
        return [loop, living_status]

def room13(user_input, itemList):

        if user_input.lower() == ("going up"):
                loop = 14
                living_status = 'Alive'
        elif user_input.lower() == ("going east"):
                loop = 12
                living_status = 'Alive'
        elif user_input.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                living_status = 'Dead'
                dead_inp = living_status
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                
        return [loop, living_status] 

def room14(user_input, itemList):
        if user_input.lower() == ("going down"):
                loop = 13
                living_status = 'Alive'
        elif user_input.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                living_status = 'Dead'
                dead_inp = living_status
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                
        return [loop, living_status] 

def room15(user_input, itemList):
        if user_input.lower() == ("going north"):
                loop = 10
                living_status = 'Alive'
        elif user_input.lower() == ("going south"):
                loop = 16
                living_status = 'Alive'
        elif user_input.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                living_status = 'Dead'
                dead_inp = living_status
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                
        return [loop, living_status]

def room16(user_input, itemList):
        if user_input.lower() == ("going north"):
                loop = 15
                living_status = 'Alive'
        else:
                print("---------------------------------------------------------")
                print("You die.")
                print("You have been eaten by the grue."
                print("---------------------------------------------------------")
                living_status = 'Dead'
                dead_inp = living_status
                exit_function(dead_inp)

def PrintOutput(s):
    print("OUTPUT", s)



