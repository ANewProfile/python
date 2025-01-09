# imports
import socket
import threading
from tkinter import *

# setting up the variables for socket
host = '192.168.4.151'
port = 98273

users = {}
MAX_USERS = 10
APP_OPEN = False

s = socket.socket()
s.bind((host, port))
s.listen(MAX_USERS)

def listen_for_new_users():
    global users
    
    while True:
        conn, addr = s.accept() 
        users[addr] = conn

        listen_thread = threading.Thread(target=listen, args=(conn, addr))
        listen_thread.start()

def send(to, msg):
    global users

    conn = users[to]
    conn.sendall(msg)

def listen(conn, addr):
    while True:
        try:
            message = conn.recv(1024)
        except:
            message = ('exit' + ' ' * 1020).encode()
        
        if message.decode().strip().lower() == 'exit':
            conn.close()
            users.pop(addr)
        else:
            for user in users:
                if user != addr:
                    send(to=addr, msg=message)

def on_exit():
    global users, APP_OPEN

    if APP_OPEN:
        root.destroy()
        APP_OPEN = False
    
    for _, conn in users.items():
        conn.close()
    
    s.close()

root = Tk()
root.title("Server")
APP_OPEN = True

root.protocol("WM_DELETE_WINDOW", on_exit)

close_button = Button(root, text="Close", command=on_exit)
close_button.pack()

new_user_thread = threading.Thread(target=listen_for_new_users)
new_user_thread.start()

root.mainloop()
