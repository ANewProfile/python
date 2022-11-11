num = input("Welcome to the the Palindrome Machine, where you type in a 5-digits or lower number and we will tell you if it is a palindrome. Let's Start! Type a number. ")
def palindrome(x):
    if len(x) == 1:
        print('Your number is a palindrome!')
    elif len(x) == 2:
        if x[0] == x[1]:
            print("Your number is a palindrome!")
        else:
            print("Your number is not a palindrome!")
    elif len(x) == 3:
        if x[0] == x[1] and x[0] == x[2]:
            print('Your number is a palindrome!')
        elif x[0] == x[2]:
            print("Your number is a palindrome!")
        else:
            print("False")
    elif len(x) == 4:
        if x[0] == x[1] and x[0] == x[2] and x[0] == x[3]:
            print("True")
        elif x[0] == x[3] and x[1] == x[2]:
            print('True')
    elif len(x) == 5:
        if x[0] == x[4] and x[1] == x[3]:
            print('True')
    else:
        print("Invalid.")
palindrome(num)