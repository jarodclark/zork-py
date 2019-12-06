# Main game file

import zork

def PrintOutput(s):
    print("OUTPUT", s)

loop = zork.Play_Zork()

while True:
    while loop == 4:
        print("---------------------------------------------------------")
        print("You are standing in an open field west of a white house, with a boarded front door.")
        print("You can see a small lake to the north.")
        print("(A secret path leads southwest into the forest.)")
        print("There is a Small Mailbox.")
        second = input("What do you do? ")
        room_status = zork.room4(second, [])
        loop = room_status[0]
    while loop == 1:
        print("---------------------------------------------------------")
        print("You find yourself at the edge of a beautiful lake aside rolling hills.")
        print("A small pier juts out into the lake.")
        print("A fishing rod rests on the pier.")
        print("(You can see a white house in the distance to the south.)")
        north_house_inp = input("What do you do? ")
        room_status = zork.room1(north_house_inp, [])
        loop = room_status[0]
    while loop == 8:
        print("---------------------------------------------------------")
        print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
        forest_inp = input("What do you do? ")
        room_status = zork.room8(forest_inp, [])
        loop = room_status[0]
    while loop == 9:
        print("---------------------------------------------------------")
        print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
        print("There is an open grating, descending into darkness.")
        grating_inp = input("What do you do? ")  
        room_status = zork.room9(grating_inp, [])
        loop = room_status[0]
    while loop == 10:
        print("---------------------------------------------------------")
        print("You are in a tiny cave with a dark, forbidding staircase leading down.")
        print("There is a skeleton of a human male in one corner.")
        cave_inp = input("What do you do? ")
        room_status = zork.room10(cave_inp, [])
        loop = room_status[0]
    while loop == 11:
        print("---------------------------------------------------------")
        print("You have entered a mud-floored room.")
        print("Lying half buried in the mud is an old trunk, bulging with jewels.")
        last_inp = input("What do you do? ")
        room_status = zork.room11(last_inp, [])
        loop = room_status[0]
    while loop == 12:
        print("---------------------------------------------------------")
        print("You are at the back of the house. paths lead south and west.")
        print("You are being chased by a monster.")
        room12_input = input("What do you do? ")
        room_status = zork.room12(room12_input, [])
        loop = room_status[0]
    while loop == 13:
        print("---------------------------------------------------------")
        print("You find yourself in a dimly lit kitchen with dust covering the floor.")
        print("A lantern rests on the kitchen island.")
        print("A set of stairs leads up to another room.")
        room13_input = input("What do you do? ")
        room_status = zork.room13(room13_input, [])
        loop = room_status[0]
    while loop == 14:
        print("---------------------------------------------------------")
        print("You find yourself in a lit attic with cob webs everywhere.")
        print("The set of stairs will take you back down.")
        room14_input = input("What do you do? ")
        room_status = zork.room14(room14_input, [])
        loop = room_status[0]
    while loop == 15:
        print("---------------------------------------------------------")
        print("You are now in a maze.")
        print("You can either go north or south to find a way out.")
        room15_input = input("What do you do? ")
        room_status = zork.room15(room15_input, [])
        loop = room_status[0]
    while loop == 16:
        print("---------------------------------------------------------")
        print("You are stuck deep in the maze with little options left.")
        room16_input = input("What do you do? ")
        room_status = zork.room16(room16_input, [])
        loop = room_status[0]










        
