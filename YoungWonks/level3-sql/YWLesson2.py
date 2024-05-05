# Login GUI 
# User can: login or register
# If login: enter username and a password with submit button
# If register: first name, last name, dob, username, password, verify password with register button
# Add registered data to database
import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('LoginDatabaseProject.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, dob TEXT, firstname TEXT, lastname TEXT)")


def login():
    # Show the login screen
    switch_landing_login.switch12()

def register():
    # show the register screen
    switch_landing_register.switch12()

def submitlogin():
    # submit the login
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (login_username.get(), login_password.get()))
    user = c.fetchall()
    if user:
        messagebox.showinfo('Successful login!', f'You have successfully logged in as {login_username.get()}!')
        conn.commit()
    else:
        messagebox.showerror('Incorrect credentials!', 'Invalid username or password')
    
    login_username.delete(0, END)
    login_password.delete(0, END)

def submitregister():
    # submit the register
    c.execute("SELECT * FROM users WHERE username = ?", (register_username.get(),))
    current_user = c.fetchall()
    if (not current_user) and (register_password.get() == register_confirm_password.get()) and register_username.get() and register_password.get() and register_dob.get() and register_firstname.get() and register_lastname.get():
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (register_username.get(), register_password.get(), register_dob.get(), register_firstname.get(), register_lastname.get()))
        messagebox.showinfo('Success! Yayyy!', 'You have successfully added a user!')
        conn.commit()
    elif current_user:
        messagebox.showerror('Error', 'User already exists')
    elif register_password.get() != register_confirm_password.get():
        messagebox.showerror('Error', 'Passwords do not match')
    else:
        messagebox.showerror('Error', 'Please fill out all of the forms')
    
    register_username.delete(0, END)
    register_password.delete(0, END)
    register_confirm_password.delete(0, END)
    register_dob.delete(0, END)
    register_firstname.delete(0, END)
    register_lastname.delete(0, END)


class SwitchFrames:
    def __init__(self, frame1, frame2):
        self.frame1 = frame1
        self.frame2 = frame2
    
    def switch12(self):
        self.frame1.pack_forget()
        self.frame2.pack()
    
    def switch21(self):
        self.frame2.pack_forget()
        self.frame1.pack()


root = Tk()

landing_frame = Frame(root)
login_frame = Frame(root)
register_frame = Frame(root)

switch_landing_login = SwitchFrames(landing_frame, login_frame)
switch_landing_register = SwitchFrames(landing_frame, register_frame)

landing_instructions = Label(landing_frame, text="Would you like to login or register?")
landing_login_button = Button(landing_frame, text="Login", command=login)
landing_register_button = Button(landing_frame, text="Register", command=register)

login_username_label = Label(login_frame, text="Username")
login_username = Entry(login_frame)
login_password_label = Label(login_frame, text="Password")
login_password = Entry(login_frame)
login_button = Button(login_frame, text="Login", command=submitlogin)

register_firstname_label = Label(register_frame, text="First Name")
register_firstname = Entry(register_frame)
register_lastname_label = Label(register_frame, text="Last Name")
register_lastname = Entry(register_frame)
register_dob_label = Label(register_frame, text="Date of Birth")
register_dob = Entry(register_frame)
register_username_label = Label(register_frame, text="Username")
register_username = Entry(register_frame)
register_password_label = Label(register_frame, text="Password")
register_password = Entry(register_frame)
register_confirm_password_label = Label(register_frame, text="Confirm Password")
register_confirm_password = Entry(register_frame)
register_button = Button(register_frame, text="Register", command=submitregister)


landing_frame.pack()

landing_instructions.pack()
landing_login_button.pack()
landing_register_button.pack()

login_username_label.pack()
login_username.pack()
login_password_label.pack()
login_password.pack()
login_button.pack()

register_firstname_label.pack()
register_firstname.pack()
register_lastname_label.pack()
register_lastname.pack()
register_dob_label.pack()
register_dob.pack()
register_username_label.pack()
register_username.pack()
register_password_label.pack()
register_password.pack()
register_confirm_password_label.pack()
register_confirm_password.pack()
register_button.pack()


root.mainloop()
conn.close()