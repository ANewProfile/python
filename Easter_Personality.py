import random as rd

values = {
    "bird": 0,
    "octopus": 0,
    'dinosaur': 0,
    'rabbit': 0
}


print("Welcome to the Easter Personality game for kids and adults! You found an egg! Hmm.... What animal is inside. ")
print("By answering these questions, you will know which animal chose to pop out and meet you! Lets get started!\n")


q1_not_done = True


while q1_not_done:
    q1 = input("Would you rather be able to [f]ly where ever you want, or [s]wim where ever you want? ")
    if q1.lower() == "f":
        values["bird"] += 2
        q1_not_done = False

    elif q1.lower() == "s":
        values["octopus"] += 1
        q1_not_done = False
    else:
        print("Invalid. Please type either f or s.")

q2_not_done = True

while q2_not_done:
    q2 = input("Would you rather be really [s]trong, or be able to [j]ump really high? ")
    if q2 == "s":
        values['dinosaur'] += 3
        q2_not_done = False
    elif q2 == "j":
        values['rabbit'] += 1
        q2_not_done = False
    else:
        print("Invalid. Please type either s or j.")

q3_not_done = True

while q3_not_done:
    q3 = input("Would you consider yourself [t]ough, or [g]raceful? ")
    if q3 == "t":
        values['dinosaur'] += 3
        q3_not_done = False
    elif q3 == "g":
        values["bird"] += 1
        q3_not_done = False
    else:
        print("Invalid. Please type either t or g.")

q4_not_done = True

while q4_not_done:
    q4 = input("Would you rather live in the [o]cean, or live [u]nderground? ")
    if q4 == "o":
        values["octopus"] += 3
        q4_not_done = False
    elif q4 == "u":
        values['rabbit'] += 2
        q4_not_done = False
    else:
        print("Invalid. Please type either o or u.")


sorted_animals = sorted(values.keys(), key=lambda k: values[k])

print('\nThe animal that you will meet is a/an....................' + str(sorted_animals[-1]) + '! Congragulations on finishing the test! Thanks for doing this. It really helps a lot!')
