two_digit_number = input('Enter a two digit number: ')
if len(two_digit_number) == 2:
    total = 0
    for num in two_digit_number:
        total += num
    print(f'The sum of the two digits in your number is: {total}')
