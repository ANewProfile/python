# imports
import socket
import threading
import time
import sqlite3 as sql
from tkinter import *
from tkinter import messagebox


# setup vital vars
APP_OPEN = False
CONNECTED = False
EXIT_SENT = False
SQL_OPEN = False

# setup socket
host = '192.168.4.151'
port = 98273

s = socket.socket()
s.connect((host, port))
CONNECTED = True

# setup sql database 
conn = sql.connect('groupchat-users.db')
c = conn.cursor()
SQL_OPEN = True
c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, email TEXT, age INTEGER)")

def add_user(username, password, email, age):
    c.execute("INSERT INTO users (username, password, email, age) VALUES (?, ?, ?, ?)", (username, password, email, age))
    conn.commit()
    startup_switcher.switch21()


# create frame switcher
class FrameSwitch:
    def __init__(self, frame1, frame2):
        self.frame1 = frame1
        self.frame2 = frame2
        
    def switch12(self):
        print('Switching...')
        self.frame1.pack_forget()
        self.frame2.pack()
        print('Switched!')

    def switch21(self):
        print('Switching...')
        self.frame2.pack_forget()
        self.frame1.pack()
        print('Switched!')


# create functions
def login():
    username = username_input.get()
    password = password_input.get()

    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    if user:
        message_switcher.switch12()
    else:
        messagebox.showerror('Error', 'Invalid username or password')

def send(username):
    message = input_box.get()
    if not message:
        return
    
    time_sent = time.time()
    prefix = f'{username} {time_sent}: '
    
    final_message = prefix + message
    if len(final_message) > 1024:
        final_message = final_message[:1024]
    else:
        final_message = final_message + ' '*(1024-len(final_message))

    message_box['state'] = 'normal'
    message_box.insert(END, message + '\n')
    message_box['state'] = 'disabled'

    s.sendall(final_message.encode())
    
    input_box.delete(0, END)

def listen():
    while True:
        try:
            message = s.recv(1024).decode()
        except:
            on_exit()
            CONNECTED = False
            EXIT_SENT = True

        message_box['state'] = 'normal'
        message_box.insert(END, message.strip() + '\n')
        message_box['state'] = 'disabled'

def on_exit():
    if APP_OPEN:
        root.destroy()
        APP_OPEN = False
    
    if not EXIT_SENT:
        exit_message = 'exit' + ' ' * 1020
        s.sendall(exit_message.encode())
        EXIT_SENT = True
        
    if CONNECTED:
        s.close()
        CONNECTED = False
        
    if SQL_OPEN:
        conn.close()
        SQL_OPEN = False


# create tk instance
root = Tk()
root.title('Messaging App')
APP_OPEN = True
root.protocol("WM_DELETE_WINDOW", on_exit)


# start listening thread
listen_thread = threading.Thread(target=listen)
listen_thread.start()


# create frames
login_frame = Frame(root)
signup_frame = Frame(root)

messaging_frame = Frame(root)
messages_frame = Frame(messaging_frame)
send_frame = Frame(messaging_frame)


# create frame switcher
startup_switcher = FrameSwitch(login_frame, signup_frame)
message_switcher = FrameSwitch(login_frame, messaging_frame)


# create login/signup screen
username_input = Entry(login_frame)
password_input = Entry(login_frame)
login_submit = Button(login_frame, text='Login', command=login)
signup_button = Button(signup_frame, text='Sign Up', command=startup_switcher.switch12)

new_username = Entry(signup_frame)
new_password = Entry(signup_frame)
new_email = Entry(signup_frame)
new_age = Entry(signup_frame)
login_submit = Button(signup_frame, text='Already have an account? Login', command=startup_switcher.switch21)
signup_submit = Button(signup_frame, text='Submit', command=lambda: add_user(new_username.get(), new_password.get(), new_email.get(), new_age.get()))


# create messages screen
message_box = Text(messages_frame)
message_box['state'] = 'disabled'

input_box = Entry(send_frame)
send_button = Button(send_frame, text='Send', command=send)


# pack login screen
login_frame.pack()
username_input.pack()
password_input.pack()
login_submit.pack()
signup_button.pack()

root.mainloop()