def room_one():
    unlocked = False
    t_unlocked = False
    tv_onlocked = False
    w_unlocked = False
    print('+--------------------+')
    print('|  _____         |   |')
    print('|  |   |         |___|')
    print('|                    |')
    print('|                    |')
    print('|                    |')
    print('|          _________ |')
    print('| ______       |     |')
    print('+--------------------+')
    while not unlocked:
        move = input('Would you like to the [t]able, [tv], [w]hiteboard, or [d]oor? ')
        if move.lower() == 't':
            if t_unlocked:
                print('You already solved this puzzle! Try a different one or go to the door!')
            else:
                print('On the table, you find a piece of paper, but its text is encrypted. It says: .eeffoc seirrac dna xis ta sevael pihs keerG ehT')
                answer = input('What is the correct clue for this puzzle? ')
                if answer.lower() == 'the greek ship leaves at six and carries coffee.':
                    print('That\'s the correct answer! Remember this clue for later!')
                    t_unlocked = True
                else:
                    print('That\'s not the correct answer!')
        elif move.lower() == 'tv':
            if tv_unlocked:
                print('You already solved this puzzle! Try a different one or go to the door!')
            else:
                print('You turn on the TV, and the screen shows an encrypted message. It says: hte hSpi ni teh mdiled ahs a lbcak xeetroir.')
                answer = input('What is the correct clue for this puzzle? ')
                if answer.lower() == 'the ship in the middle has a black exterior':
                    print('That\'s the correct answer! Remember this clue for later!')
                    tv_unlocked = True
                else:
                    print('That\'s not the correct answer!')
        elif move.lower() == 'w':
            ...
        elif move.lower() == 'd':
            ...
        else:
            print('Invalid!')

def room_two():
    ...

def room_three():
    ...

def room_four():
    ...

def room_five():
    ...


if __name__ == "__main__":
    print('Welcome! Try to escape, and make sure to keep track of the answers to each puzzle, as they are clues to the final puzzle.')
    room_one()
    room_two()
    room_three()
    room_four()
    room_five()
