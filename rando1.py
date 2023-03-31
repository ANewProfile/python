cost = float(input("What is the cost? "))
tip = float(input("How much do you want to tip(don't write %)? "))
hwpep = int(input("How many people to split the bill? "))
print(
    f"Each person will tip {round((cost * (tip/100))/hwpep, 3)}, total cost/person will be {(cost/hwpep) + ((cost * (tip/100))/hwpep)}")
