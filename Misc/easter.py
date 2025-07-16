num_kids = int(
    input("How many kids and teachers are currently at the school? "))
money = int(input("How much did we earn? "))
num_eggs = int(input("How many eggs are we hiding? "))
eggs = 64/288
total_donating = 0
per = 0


def calc(kids, money, eggs, num, donating):
    donating += money
    donating -= eggs*num
    donating -= 100
    farm_school = donating/kids
    return round(farm_school, 2), round(per, 2)


get_cost = list(calc(num_kids, money, eggs, num_eggs, total_donating))
print(
    f'We are subtracting ${get_cost[0]} from each student and teacher for farm school, and we are donating $100 to the Boston Childrens Hospital')
