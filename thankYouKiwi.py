import random
import termcolor
tries=0
print("Welcome to Hangman. I, ComputerBot5000, will be your host. Just play Hangman the Way you normally do, spaces and exclamations included. You have 6 wrong tries. Go!")
words = ["kiwi", "thanks!", "congratulations!", "new job", "thank you!"]
word = random.choice(words)
board="-" * len(word)
print(board)
game_over=False
while game_over==False:
  wrong= True
  guess=input("Guess a letter or symbol. ")
  for i in range(0,len(word)):
    if guess.lower()==word[i]:
      board = board[:i] + word[i] + board[i+1:]
      wrong = False
  if wrong:
    tries+=1
  print(board)
  if board==word:
    print(termcolor.colored("You win!", "green", attrs = ['reverse', 'bold']))
    game_over=True
  if tries==6:
    game_over=True
    print(termcolor.colored("You lose. Better luck next time! The word was " + word,"red",attrs=['bold', 'underline']))


