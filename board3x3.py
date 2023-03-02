game = True

one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9

turn = 1


def display_board(one, two, three, four, five, six, seven, eight, nine):
    board = f"+---+---+---+\n| {one} | {two} | {three} |\n+---+---+---+\n| {four} | {five} | {six} |\n+---+---+---+\n| {seven} | {eight} | {nine} |\n+---+---+---+"
    print(board)


def find_turn(turn):
    if turn % 2 == 1:
        return 'X'
    else:
        return 'O'


def check_win():
    if one == two == three:
        print(f"The winner is... {one}!")
        exit()
    elif four == five == six:
        print(f"The winner is... {four}!")
        exit()
    elif seven == eight == nine:
        print(f"The winner is... {seven}!")
        exit()
    elif one == four == seven:
        print(f"The winner is... {one}!")
        exit()
    elif two == five == eight:
        print(f"The winner is... {two}!")
        exit()
    elif three == six == nine:
        print(f"The winner is... {three}!")
        exit()
    elif one == five == nine:
        print(f"The winner is.. {one}!")
        exit()
    elif three == five == seven:
        print(f"The winner is... {three}!")
        exit()


while game:
    real_turn = find_turn(turn)
    display_board(one, two, three, four, five, six, seven, eight, nine)
    move = input(f'{real_turn}, it\'s your turn: ')
    if int(move) == 1 and one != real_turn:
        one = real_turn
    elif int(move) == 2 and two != real_turn:
        two = real_turn
    elif int(move) == 3 and three != real_turn:
        three = real_turn
    elif int(move) == 4 and four != real_turn:
        four = real_turn
    elif int(move) == 5 and five != real_turn:
        five = real_turn
    elif int(move) == 6 and six != real_turn:
        six = real_turn
    elif int(move) == 7 and seven != real_turn:
        seven = real_turn
    elif int(move) == 8 and eight != real_turn:
        eight = real_turn
    elif int(move) == 9 and nine != real_turn:
        nine = real_turn
    else:
        print("Invalid.")
    check_win()
    turn += 1
