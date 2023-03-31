yr = input("What year in the 21st century do you want(56, 23, 00, 07,  etc)? ")
mnth = input("What month do you want(1, 2, 3, etc)? ")
dy = input("What day in the month is it(3, 28, 16, etc)? ")
year = int(yr)
month = int(mnth)
day = int(dy)
leap = False
num_leaps = 0
year_day = 2
true_day = 0

if year != 00 and year % 4 == 0:
    leap = True

num_leaps = (year - year % 4) / 4
year_day += year
year_day += num_leaps

if month == 1 and leap == False and day < 3:
    year_day += (3 - day)
elif month == 1 and leap == False and day == 3:
    year_day += 0
elif month == 1 and leap == False and day > 3:
    year_day += (day - 3)
elif month == 1 and leap == True and day > 4:
    year_day += (day - 4)
elif month == 1 and leap == True and day == 4:
    year_day += 0
elif month == 1 and leap == True and day < 4:
    year_day += (4 - day)
elif month == 2 and leap == False and day == 28:
    year_day += 0
elif month == 2 and leap == False and day < 28:
    year_day += (28 - day)
elif month == 2 and leap == True and day == 29:
    year_day += 0
elif month == 2 and leap == True and day < 29:
    year_day += (29 - day)
elif month == 3 and day < 14:
    year_day = + (14 - day)
elif month == 3 and day == 14:
    year_day += 0
elif month == 3 and day > 14:
    year_day += (day - 14)
elif month == 4 and day > 4:
    year_day += (4 - day)
elif month == 4 and day == 4:
    year_day += 0
elif month == 4 and day < 4:
    year_day += (4 - day)
elif month == 5 and day < 9:
    year_day += (9 - day)
elif month == 5 and day == 9:
    year_day += 0
elif month == 5 and day > 9:
    year_day += (day - 9)
elif month == 6 and day < 6:
    year_day += (6 - day)
elif month == 6 and day == 6:
    year_day += 0
elif month == 6 and day > 6:
    year_day += (day - 6)
elif month == 7 and day < 11:
    year_day += (11 - day)
elif month == 7 and day == 11:
    year_day += 0
elif month == 7 and day > 11:
    year_day += (day - 11)
elif month == 8 and day < 8:
    year_day += (8 - day)
elif month == 8 and day == 8:
    year_day += 0
elif month == 8 and day > 8:
    year_day += (day - 8)
elif month == 9 and day < 5:
    year_day += (5 - day)
elif month == 9 and day == 5:
    year_day += 0
elif month == 9 and day > 5:
    year_day += (day - 5)
elif month == 10 and day < 10:
    year_day += (10 - day)
elif month == 10 and day == 10:
    year_day += 0
elif month == 10 and day > 10:
    year_day += (day - 10)
elif month == 11 and day < 7:
    year_day += (7 - day)
elif month == 11 and day == 7:
    year_day += 0
elif month == 11 and day > 7:
    year_day += (day - 7)
elif month == 12 and day < 12:
    year_day += (12 - day)
elif month == 12 and day == 12:
    year_day += 0
elif month == 12 and day > 12:
    year_day += (day - 12)

day_num = year_day % 7

if day_num == 0:
    true_day = "Sunday"
elif day_num == 1:
    true_day = "Monday"
elif day_num == 2:
    true_day = "Tuesday"
elif day_num == 3:
    true_day = "Wednesday"
elif day_num == 4:
    true_day = "Thursday"
elif day_num == 5:
    true_day = "Friday"
elif day_num == 6:
    true_day = "Saturday"


print(f"The day of the week for the date you entered is {true_day}!")
