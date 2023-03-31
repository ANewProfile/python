import random
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
non_occupied = []
no_num = ''
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
    if one != 1 and two != 2 and three != 3 and four != 4 and five != 5 and six != 6 and seven != 7 and eight != 8 and nine != 9:
        print(f"The winner is... just kidding, it's a draw!")
        exit()
    elif one == two == three:
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
    if real_turn == 'X':
        move = input(f'{real_turn}, it\'s your turn: ')
        if int(move) == 1 and one == 1:
            one = real_turn
        elif int(move) == 2 and two == 2:
            two = real_turn
        elif int(move) == 3 and three == 3:
            three = real_turn
        elif int(move) == 4 and four == 4:
            four = real_turn
        elif int(move) == 5 and five == 5:
            five = real_turn
        elif int(move) == 6 and six == 6:
            six = real_turn
        elif int(move) == 7 and seven == 7:
            seven = real_turn
        elif int(move) == 8 and eight == 8:
            eight = real_turn
        elif int(move) == 9 and nine == 9:
            nine = real_turn
        else:
            print("Invalid.")
        check_win()
        turn += 1
    else:
        if one == two and three == 3:
            three = real_turn
        elif two == three and one == 1:
            one = real_turn
        elif one == three and two == 2:
            two = real_turn
        elif four == five and six == 6:
            six = real_turn
        elif five == six and four == 4:
            four = real_turn
        elif four == six and five == 5:
            five = real_turn
        elif seven == eight and nine == 9:
            nine = real_turn
        elif eight == nine and seven == 7:
            seven = real_turn
        elif seven == nine and eight == 8:
            eight = real_turn
        elif one == four and seven == 7:
            seven = real_turn
        elif four == seven and one == 1:
            one = real_turn
        elif one == seven and four == 4:
            four = real_turn
        elif two == five and eight == 8:
            eight = real_turn
        elif five == eight and two == 2:
            two = real_turn
        elif two == eight and five == 5:
            five = real_turn
        elif three == six and nine == 9:
            nine = real_turn
        elif six == nine and three == 3:
            three = real_turn
        elif three == nine and six == 6:
            six = real_turn
        elif one == five and nine == 9:
            nine = real_turn
        elif one == nine and five == 5:
            five = real_turn
        elif five == nine and one == 1:
            one = real_turn
        elif three == five and seven == 7:
            seven = real_turn
        elif five == seven and three == 3:
            three = real_turn
        elif three == seven and five == 5:
            five = real_turn
        elif one == 1 or three == 3 or seven == 7 or nine == 9:
            if one == 1:
                non_occupied.append(1)
            elif three == 3:
                non_occupied.append(3)
            elif seven == 7:
                non_occupied.append(7)
            elif nine == 9:
                non_occupied.append(9)
            no_num = random.choice(non_occupied)
            if no_num == 1:
                one = real_turn
            elif no_num == 3:
                three = real_turn
            elif no_num == 7:
                seven = real_turn
            elif no_num == 9:
                nine = real_turn

        else:
            random_num = random.randint(1, 9)
            if random_num == 1 and one == 1:
                one = real_turn
            elif random_num == 2 and two == 2:
                two = real_turn
            elif random_num == 3 and three == 3:
                three = real_turn
            elif random_num == 4 and four == 4:
                four = real_turn
            elif random_num == 5 and five == 5:
                five = real_turn
            elif random_num == 6 and six == 6:
                six = real_turn
            elif random_num == 7 and seven == 7:
                seven = real_turn
            elif random_num == 8 and eight == 8:
                eight = real_turn
            elif random_num == 9 and nine == 9:
                nine == real_turn
        check_win()
        turn += 1
