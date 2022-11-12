import random
import termcolor
import time


def determine_computer_turn(num, current_num):
    sum_distance = abs(100 - (num + current_num))
    difference_distance = abs(100 - (current_num - num))
    product_distance = abs(100 - (num * current_num))
    quotient_distance = abs(100 - round(current_num / num))
    distances = {"+": sum_distance, "-": difference_distance, "*": product_distance, "/": quotient_distance}
    smallest_distance = distances["+"]
    smallest_operation = "+"
    for operation in distances:
        if distances[operation] < smallest_distance:
            smallest_distance = distances[operation]
            smallest_operation = operation
    return smallest_operation


def change_current_num(current_num, turn, num):
    if turn == "+":
        return current_num + num
        print("Your number is now " + current_user_num)
    elif turn == "-":
        return current_num - num
        print(current_user_num)
    elif turn == "*":
        return current_num * num
    elif turn == "/":
        return round(current_num / num)


game_over = False
current_user_num = 1
current_computer_num = 1
print(
    "Welcome to race to 100! Your goal is to get to exactly 100 before the computer does using the operations +,-,*,or/. Both you and the computer start at 1 and will receive separate random numbers to use.")
while not game_over:
    user_num = random.randint(1, 10)
    computer_num = random.randint(1, 10)
    print("\nYour turn, you can use the number " + str(user_num))
    valid = False
    while not valid:
        user_turn = input("Would you like to +, -, *, or / " + str(user_num) + " from " + str(current_user_num) + " ")
        if user_turn in ["+", "-", "*", "/"]:
            valid = True
        else:
            print("Invalid. Try again.")

    print(
        termcolor.colored("You did " + str(current_user_num) + str(user_turn) + str(user_num), "blue", attrs=['bold']))
    current_user_num = change_current_num(current_user_num, user_turn, user_num)
    print(termcolor.colored("Your number is now " + str(current_user_num), "blue", attrs=['bold']))

    time.sleep(1)

    computer_turn = determine_computer_turn(computer_num, current_computer_num)

    print(termcolor.colored("\nThe computer did " + str(current_computer_num) + str(computer_turn) + str(computer_num),
                            "red", attrs=['bold']))
    current_computer_num = change_current_num(current_computer_num, computer_turn, computer_num)
    print(termcolor.colored("The computer's number is now " + str(current_computer_num), "red", attrs=['bold']))

    time.sleep(1)

    if current_user_num == 100:
        print(termcolor.colored("You win! Nice Job!", "green", attrs=['bold']))
        game_over = True
    elif current_computer_num == 100:
        print(termcolor.colored("You lose. Better luck next time!", "yellow", attrs=['bold']))
        game_over = True
    elif current_computer_num == current_user_num:
        print(termcolor.colored("You tied!", "blue", attrs=['bold']))