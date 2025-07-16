def fibonacci():

    numnum = int(input('How long do you want? '))
    numprinted = 0
    tempnum = 0
    num = 1

    while numnum > numprinted:
        print(num)
        numprinted += 1
        print(f"Num Printed: {numprinted}")
        tempnum = num
        print(f"TempNum: {tempnum}")
        num += tempnum
        print(f"Num: {num}")

fibonacci()