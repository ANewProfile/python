two_digit_number = input('Enter a number: ')
total = 0
for num in two_digit_number:
    total += int(num)
print(f'The sum of the digits in your number is: {total}')
