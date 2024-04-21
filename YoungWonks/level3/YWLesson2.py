from tkinter import *
from tkinter import messagebox
from random import choice, shuffle


def randomize_word(word):
    word_list = list(word)
    shuffle(word_list)
    return ''.join(word_list)

def check_guess():
    if guess.get() == word.get():
        try:
            words.remove(word.get())
            word.set(choice(words))
            fake_word.set(randomize_word(word.get()))
            messagebox.showinfo('You got the answer correct!', 'Nice job! You guessed the answer correctly!')
        except IndexError:
            if not finished:
                impossible_list = list('impossible')
                shuffle(impossible_list)
                words.append(''.join(impossible_list))
                words.remove(word.get())
                word.set(choice(words))
                fake_word.set(randomize_word(word.get()))
                messagebox.showinfo('You got the answer correct!', 'Nice job! You guessed the answer correctly!')
            else:
                messagebox.showinfo('You finished everything!', 'Congratulations! You finished all the words!')
    else:
        messagebox.showerror('You got the answer incorrect!', 'Nice try! You guessed the answer incoorectly! Try again to move on!')        
    
    guess.delete(0, END)


root = Tk()

finished = False
words = ['word', 'letter', 'sentence', 'space', 'comment', 'terminal', 'comments', 'comma', 'period']
word = StringVar()
word.set(choice(words))
fake_word = StringVar()
fake_word.set(randomize_word(word.get()))


label = Label(root, text='Guess the jumbled word!')
word_label = Label(root, textvariable=fake_word)
guess = Entry(root)
submit = Button(root, text='Submit Guess', command=check_guess)


label.pack()
word_label.pack()
guess.pack()
submit.pack()


root.mainloop()

'''
Guess the jumbled word
One word, random letter orientation
Entry box - enter the correct spelling
Submit button - check if correct spelling is correct spelling
  If correct: show that they got it correct
  If incorrect: retry same word

After finishing all words: show info ('You finished everything!')
'''