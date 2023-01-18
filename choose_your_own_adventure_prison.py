startstart = True
start = False
first_choice = False
second_choice = False
third_choice = False
fourth_choice = False
fifth_choice = False


def first_choice_q():
    q = input("\nYou're trapped in a prison cell, and the only thing in the room is a book, a pencil, and an eraser. You have two options:\n1. Wait for a prison guard to come and try to knock him out\nOR\n2. Try to dig a hole in the wall with your given materials and escape.\nWhat will we choose? ")
    if q == "1":
        return "1"
    elif q == "2":
        return "2"
    else:
        print("Invalid.\n\n")


def second_choice_q():
    q = input("\nYou manage to hold off and entertain yourself by reading until the guard comes by. You now have three options:\n1. Try to intimidate the guard into giving you the keys\nOR\n2. Try to reach through the bars and swipe the keys.\nOR\n3. Try to lure the guard into the cell and knock him out.\nWhat will we choose? ")
    if q == "1":
        return "3"
    elif q == "2":
        return "1"
    elif q == "3":
        return "2"
    else:
        print("Invalid.\n\n")


def third_choice_q():
    q = input("\nYou reach through the bars, and the officer steps back to call security. But not before you managed to swipe his keys. While he heads off to call security, you unlock your cell door and escape your cell. You hurredly head down the stairs, but one turn away from the exit of the main building, you hear footsteps approaching from that direction. You now have three options:\n1. Duck into a nearby closet\nOR\n2. Flee down a nearby hallway\nOR\n3. Continue down your desired path and try to subdue whoever was coming.\nWhat will we choose? ")
    if q == "1":
        return "1"
    elif q == "2":
        return "2"
    elif q == "3":
        return "3"
    else:
        print("Invalid.\n\n")


def fourth_choice_q():
    q = input("\nYou duck into the closet and wait as footsteps pass by. You wait a bit for good measure, then exit the closet. You continue down the hallway and finally escape the building. However, you find yourself in the wide open space of the courtyard. You now have two options:\n1. You can sprint across the courtyard, as it is the fastest way out, but risks being seen.\nOR\n2. You could take a slower side path on the right, with a lower chance of being seen.\nWhat will we choose? ")
    if q == "1":
        return "2"
    elif q == "2":
        return "1"
    else:
        print("Invalid.\n\n")


def fifth_choice_q():
    q = input("\nYou run out into the fresh air of the outside. You run away, but the crime you committed to get into jail, was stealing someone's computer. You know where you had it hidden. You now have two final choices:\n1. Find and return the laptop to it's owner\nOR\n2. Take the laptop for yourself.\nWhat will we choose? ")
    if q == "1":
        return "1"
    elif q == "2":
        return "2"
    else:
        print("Invalid.\n\n")


if startstart:
    print("Welcome to Escape the Prison!\n")
    startquestion = input("Are you ready to start?(y/n) ")
    if startquestion.lower() == "y":
        start = True
    elif startquestion.lower() == "n":
        print("Okay.")
    else:
        print("Invalid.\n")

if start:
    first_choice = True

if first_choice:
    go1 = first_choice_q()
    if go1 == "1":
        print("")
    elif go1 == "2":
        print('You proceed as planned, digging and digging while no one is watching, but eventually a prison guard catches on to your suspicious behavior and stops you. You are then placed in a different cell but this time the guard is better and will probably notice you more quickly. Please try again.\n\n')
        start = False


if start:
    second_choice = True

if second_choice:
    go2 = second_choice_q()
    if go2 == "1":
        print("")
    elif go2 == "2":
        print("You ask the guard, \"I recently finished my book, could you come collect it and replace it?\"\nAt which point the guard simply replied, \"No.\" Please try again.\n\n")
        start = False
    elif go2 == "3":
        print("You walk up to the guard and and reach through the bars to grab his shirt collar, at which point the guard takes a step back and calls security to place you in a more confined cell. Please try again.\n\n")
        start = False

if start:
    third_choice = True

if third_choice:
    go3 = third_choice_q()
    if go3 == "1":
        print("")
    elif go3 == "2":
        print("You race down a nearby hallway, only to run directly into a guard guarding the low-level cells of that hallway, and a second later, everything went blank. Please try again.\n\n")
        start = False
    elif go3 == "3":
        print("You continue down your desired path ready to face whoever comes at you, only to find five armed guards plus the one other guard that you had swiped the keys of, and a second later, they were on you, and you were cuffed. Please try again.\n\n")
        start = False

if start:
    fourth_choice = True

if fourth_choice:
    go4 = fourth_choice_q()
    if go4 == "1":
        print("")
    else:
        print("You sprint down the courtyard torward the prison gates. You're almost there! 3, 2, ... A couple of guards had seen you and raced over to you and cuffed you. Please try again.\n\n")
        start = False

if start:
    fifth_choice = True

if fifth_choice:
    go5 = fifth_choice_q()
    if go5 == "1":
        print("You return the laptop, making sure to stay undercover. Due to your mistake, you are now on the run from the law and must live undercover. You have escaped!")
    else:
        print("You go to find the laptop, only to find that the police have found it and has been waiting for you ever since they found you missing from your cell. You are cuffed and transported to a supermax prison. Please try again.\n\n")
