from tkinter import *
from tkinter import messagebox
from random import randint


def check_answer():
    try:
        if int(guess_box.get()) == number.get():
            if messagebox.askyesno('You Won!', 'Congratulations! You guessed the number! Would you like to play again?'):
                number.set(randint(1, 1000))
            else:
                root.quit()
        elif int(guess_box.get()) > number.get():
            messagebox.showinfo('You guessed incorrectly!', 'Your number is too high!')
        else:
            messagebox.showinfo('You guessed incorrectly!', 'Your number is too low!')
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid integer!')
    
    guess_box.delete(0, END)


root = Tk()
playing = BooleanVar()
playing.set(True)
number = IntVar()
number.set(randint(1, 1000))


instructions = Label(root, text='Guess the number from 1 to 1000!')
guess_box = Entry(root)
guess_button = Button(root, text='Submit Guess', command=check_answer)

instructions.pack()
guess_box.pack()
guess_button.pack()


root.mainloop()
