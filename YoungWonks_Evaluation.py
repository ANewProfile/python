# num1 = int(input('Choose a number: '))
# num2 = int(input('Choose a number: '))
# num3 = int(input('Choose a number: '))
# num4 = int(input('Choose a number: '))

# sum = num1 + num2 + num3 + num4
# print(f'The sum of your numbers is: {sum}')


# age = int(input('How old are you? '))

# if age < 18:
#     print('You are a child!')
# elif age >= 18 and age < 65:
#     print('You are an adult!')
# else:
#     print('You are a senior!')


# num1 = int(input('Choose a number: '))
# num2 = int(input('Choose a number: '))
# num3 = int(input('Choose a number: '))

# if num1 > num2:
#     if num1 > num3:
#         print(f'The largest number is: {num1}')
#     elif num3 > num1:
#         print(f'The largest number is: {num3}')
#     else:
#         print(f'It\'s a tie! {num1} and {num3} are both the largest numbers!')
# elif num2 > num1:
#     if num2 > num3:
#         print(f'The largest number is: {num2}')
#     elif num3 > num2:
#         print(f'The largest number is: {num3}')
#     else:
#         print(f'It\'s a tie! {num2} and {num3} are both the largest numbers!')
# else:
#     if num1 > num3:
#         print(f'It\'s a tie! {num1} and {num2} are both the largest numbers!')
#     elif num3 > num1:
#         print(f'The largest number is: {num3}')
#     else:
#         print(f'It\'s a tie! {num1}, {num2}, and {num3} are all the largest numbers!')


# import random

# nums = []
# largest_number = [0, 0]
# for i in range(0, 100):
#     num = random.randint(1, 100)
#     nums.append(num)
#     if num > largest_number[0]:
#         largest_number[0] = num
#         largest_number[1] = i

# print(nums)
# print(f'\n\nThe largest number is {largest_number[0]}, located at the {largest_number[1]}th index.')



# fake_alphabet = ['a', 'b', 'c', 'd']
# print(fake_alphabet)
# for i in range(len(fake_alphabet)):
#     new_elm = ord(fake_alphabet[i])
#     fake_alphabet[i] = new_elm
# print(fake_alphabet)



import random

dict = {'python': random.randint(1, 1000), 'html': random.randint(1, 1000),
         'css': random.randint(1, 1000), 'javascript': random.randint(1,1000),
           'c#': random.randint(1, 1000)}
sorted_dict = []
for key, value in dict.items():
    sorted_dict.append(value)
    print(sorted_dict)
sorted_dict.sort()
print(sorted_dict)
for i, item in enumerate(sorted_dict):
    for key, val in dict.items():
        if val == item:
            sorted_dict[i] = key
print('\n\n\n')
print(dict)
print(sorted_dict)
