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



# import random

# dict = {'a': random.randint(1, 100), 'b': random.randint(1, 100),
#          'c': random.randint(1, 100), 'd': random.randint(1,100),
#            'e': random.randint(1, 100)}
# sorted_dict = []
# for key, value in dict.items():
#     sorted_dict.append(value)
#     print(sorted_dict)
# sorted_dict.sort()
# print(sorted_dict)
# for i, item in enumerate(sorted_dict):
#     for key, val in dict.items():
#         if val == item:
#             sorted_dict[i] = (key, val)
# print('\n\n\n')
# print(dict)
# print(sorted_dict)



# import random

# # Create List
# nums = [random.randint(1, 100_000) for _ in range(20)]
# print(nums)

# # Mean the list w/ odd numbers
# mean_odd = 0
# total_odd = 0
# for num in nums:
#     total_odd += num
# mean_odd = total_odd / 20
# print(f'The mean is: {mean_odd}')

# # Remove Odd numbers
# even_nums = []
# for num in nums:
#     if num % 2 == 0:
#         even_nums.append(num)

# # Mean
# mean_even = 0
# total_even = 0
# for num in even_nums:
#     total_even += num
# mean_even = total_even / len(even_nums)
# print(f'The mean of the even numbers is: {mean_even}')



# alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
#             'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
#             'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
#             'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
#             'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
#             'z': 0}
# while True:
#     word = input('Enter a word(stop to exit): ')
#     if word.lower() != 'stop':
#         for letter in word.lower():
#             alphabet[letter] += 1
#     else:
#         break

# print(alphabet)
