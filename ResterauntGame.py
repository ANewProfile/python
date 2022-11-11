#dict = {'key':'lock', 12345: 'i have absolutely no idea', 'classes': ['python', 'science', 'math']}
#print(dict['classes'])
import random as rd


player_money = rd.randint(50, 150)
buys = 0

menu = {'s': '[s]ushi', 'r': '[r]amen', 'd': '[d]umplings', 'ss': '[s]oy [s]auce'}
price = {'s': 6, 'r': 7, 'd': 5, 'ss': 0.5}


print("Welcome to Mr. Bobathans Resteraunt! You start with $" + str(player_money) + " dollars. Your goal is to run out off money while buying the LEAST amount of Asian food possible. Good Luck!")

max_buys = 0
temp_player_money = player_money
current_prices = list(price.values())
while len(current_prices) > 0:
    highest_price = max(current_prices)
    number_of_items_of_highest_price = int(temp_player_money/highest_price)
    temp_player_money -= number_of_items_of_highest_price*highest_price
    max_buys += number_of_items_of_highest_price
    current_prices.remove(highest_price)

while True:

    print("This is the menu: ")
    for item in menu:
        print(menu[item] + ".......$" + str(price[item]))

    can_afford_something = False
    for item in price:
        if player_money >= price[item]:
            can_afford_something = True
    if can_afford_something:
        buy = input(" What would you like to buy? ")

        if buy in price:
            if player_money < price[buy]:
                print("Sorry, you can't afford that.")
            else:
                player_money -= price[buy]
                print("\nYou have $" + str(player_money) + " left\n")
                buys += 1
    else:
        print("\nSorry, you can't afford anything.\n")
        if buys == max_buys:
            print("You got the same amount of buys as the computer calculated! Good Job!")
        elif buys < max_buys:
            print("You Win! You bought less items than the computer!")
        else:
            print("Sorry, you didn't get the least possible amount of buys.")
            print("You bought " + str(buys) + " items!")
        break
