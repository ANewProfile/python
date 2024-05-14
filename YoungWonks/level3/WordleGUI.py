import sqlite3
from tkinter import *
from tkinter import messagebox
import random

conn = sqlite3.connect('WordleGUI.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS words (word TEXT)")
# c.execute("INSERT INTO words VALUES ('apple')")
# c.execute("INSERT INTO words VALUES ('grape')")
# c.execute("INSERT INTO words VALUES ('lemon')")
# c.execute("INSERT INTO words VALUES ('mango')")
# c.execute("INSERT INTO words VALUES ('peach')")
# c.execute("INSERT INTO words VALUES ('berry')")
# c.execute("INSERT INTO words VALUES ('olive')")
# c.execute("INSERT INTO words VALUES ('melon')")
# c.execute("INSERT INTO words VALUES ('robot')")
# c.execute("INSERT INTO words VALUES ('guava')")

# Word bank of 10 different 5-letter words
c.execute("SELECT * FROM words")
word_bank = c.fetchall()

# Commit and close the connection
conn.commit()
conn.close()

# Pick a random word from the list
target_word = random.choice(word_bank)

# Setup the main window
root = Tk()

# Labels to display guesses
labels = [[Label(root) for _ in range(5)] for _ in range(6)]
for r in range(6):
    for c in range(5):
        labels[r][c].grid(row=r, column=c, padx=5, pady=5)

# Entry box for user input
entry = Entry(root)
entry.grid(row=6, column=0, columnspan=3, pady=20)

# Function to check the guess
def check_guess():
    guess = entry.get().lower()
    if len(guess) != 5:
        print({guess})
        messagebox.showinfo("Error", "Please enter a 5-letter word.")
        entry.delete(0, END)
        return
    current_row = sum(label['text'] != '' for row in labels for label in row) // 5
    if current_row < 6:
        for i in range(5):
            labels[current_row][i]['text'] = guess[i]
            if guess[i] == target_word[i]:
                labels[current_row][i]['bg'] = 'green'
            elif guess[i] in target_word:
                labels[current_row][i]['bg'] = 'yellow'
            else:
                labels[current_row][i]['bg'] = 'red'
        if guess == target_word:
            messagebox.showinfo("Congratulations!", "You guessed the word correctly!")
        elif current_row == 5:
            messagebox.showinfo("Game Over", f"You've used all your guesses. The word was {target_word}.")
    
    entry.delete(0, END)

# Submit button
submit_button = Button(root, text="Submit", command=check_guess)
submit_button.grid(row=6, column=3, columnspan=2)

root.mainloop()
