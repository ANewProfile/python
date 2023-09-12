# Challenge 1: 4x4 stars

for i in range(4):
    for i in range(4):
        print('*', end ='')
    print('')


#Challenge 2: Create a function that can tell if a number is prime
#
# def primes(x):
#     num1 = 2
#     isnotprime = False
#     for i in range(2, x):
#         if x%i == 0:
#             isnotprime = True
#             break
#     if isnotprime:
#         print("This number is not a prime number")
#     else:
#         print('This number is a prime number')
# hi = int(input("Choose a number bigger than 1. "))
#
#primes(hi)

# Challenge Number 3: Create a Cesar Cypher
#


# Challenge 3: Caesar Cypher
#
# cesarNum = int(input("What number is your cesar encryption(1 to 25)(if you want to decode something than make it negative)? "))
# encryptionSen = input("Enter the sentence you want to encrypt. ")
#
# # ceasarEncoding
# encryptedSen = ''
# for letter in encryptionSen:
#     encryptedSen += chr(ord(letter)+cesarNum)
# print("".join(str(cesarNum) + " | " + str(encryptedSen)))

# # theoEncoding
# encryptedSen = []
# for i,letter in enumerate(encryptionSen):
#     encryptedSen.append(chr(ord(letter)+cesarNum+((i*i+cesarNum)*cesarNum+777)))
# print("".join(encryptedSen))

    #Fibonacci recursion
# def fib(a, b):
#     c = a+b
#     print(c)
#     fib(b, c)
# fib(1, 1)

    #Fibonacci loop
# how_much = int(input("Which numbers do you want?(it will print Fibonacci of anything roughly lower than ur number) "))
# a = 1
# b = 1
# c = 0
# while c<how_much:
#     c = a + b
#     print(c)
#     a = b
#     b = c
