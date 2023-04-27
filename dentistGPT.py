from coolprint import *

dentist = open('premade_dentist.txt', 'r')
dentist = dentist.read()

query = input("Enter a prompt here: ")
if query == 'What is the most efficient way to brush your teeth?':
    print(dentist)
else:
    print("As an AI language model, I don't have the capacity to understand your prompt. If you have any further issues, I would recommend trying ChatGPT: \nhttps://chat.openai.com/?model=text-davinci-002-render-sha")
