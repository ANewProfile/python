# Welcome message
print('Welcome the the Prisoner\'s Dilemma game. Each turn, you choose to either split or steal. If you and the computer both split, you both get three points.\n\
If one person splits and the other person steals, whoever steals gets five points. If you both steal, you each get one coin. First to 100 points wins! Good luck!')

# Set variables
game_over = False
last_move = True
points_user = 0
points_com = 0

while not game_over:
    # Check for victory
    if points_user >= 100 and points_com >= 100:
        print('It\'s a tie!')
        game_over = True
        break
    elif points_user >= 100:
        print('You win! Congratulations!')
        game_over = True
        break
    elif points_com >= 100:
        print('You lose! Better luck next time!')
    else:
        pass
    
    # Determine the user's move
    while True:
        user_input = input('Would you like to [s]plit or [st]eal? ')
        if user_input.lower() == 's':
            user_move = True
            break
        elif user_input.lower() == 'st':
            user_move = False
            break
        else:
            print('Invalid')

    # Determine the computer's move and the user's last move
    com_move = last_move
    last_move = user_move
    
    # Analyze the computer's and user's moves and add points
    if com_move == True and user_move == True:
        points_user += 3
        points_com += 3
        print('You both split! You each got three points.')
        print(f'Computer\'s score: {points_com}')
        print(f'Your score: {points_user}')
    elif com_move == True and user_move == False:
        points_user += 5
        print('You stole and the computer split! You get five points.')
        print(f'Computer\'s score: {points_com}')
        print(f'Your score: {points_user}')
    elif com_move == False and user_move == True:
        points_com += 5
        print('You split and the computer stole! The computer gets five points.')
        print(f'Computer\'s score: {points_com}')
        print(f'Your score: {points_user}')
    elif com_move == False and user_move == False:
        points_user += 1
        points_com += 1
        print('You both stole! You each get one point.')
        print(f'Computer\'s score: {points_com}')
        print(f'Your score: {points_user}')
