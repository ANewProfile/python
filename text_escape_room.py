def room_one():
    unlocked = False
    t_unlocked = False
    tv_unlocked = False
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
        if t_unlocked and tv_unlocked and w_unlocked:
            unlocked = True
        move = input('Would you like to the [t]able, [tv], [w]hiteboard, or [d]oor? ')
        if move.lower() == 't':
            if t_unlocked:
                print('You already solved this puzzle! Try a different one or go to the door!')
                continue
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
                continue
            else:
                print('You turn on the TV, and the screen shows an encrypted message. It says: hte hSpi ni teh mdiled ahs a lbcak xeetroir.')
                answer = input('What is the correct clue for this puzzle? ')
                if answer.lower() == 'the ship in the middle has a black exterior.':
                    print('That\'s the correct answer! Remember this clue for later!')
                    tv_unlocked = True
                else:
                    print('That\'s not the correct answer!')
        elif move.lower() == 'w':
            if w_unlocked:
                print('You already solved this puzzle! Try a different one or go to the door!')
                continue
            else:
                print('You walk up to the whiteboard, where there is an encoded message: Jxu Udwbyix ixyf buqlui qj dydu. | 16')
                answer = input('What is the correct clue for this puzzle? ')
                if answer.lower() == 'the english ship leaves at nine.':
                    print('That\'s the correct answer! Remember this clue for later!')
                    w_unlocked = True
                else:
                    print('That\'s not the correct answer!')
        elif move.lower() == 'd':
            if unlocked:
                return True
            else:
                print('You haven\'t unlocked the door yet. Try again once you\'ve solved all the puzzles!')
                continue
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
    if room_one():
        print('You escaped room one!')
    if room_two():
        print('You escaped room two!')
    if room_three():
        print('You escaped room three!')
    if room_four():
        print('You escaped room four!')
    if room_five():
        print('You escaped the whole escape room! Nice job!')
