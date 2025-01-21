import sqlite3 as sql
from tkinter import *
import threading
import socket
import time


APP_OPEN = False
SQL_OPEN = False
CONNECTED = False
SENT_EXIT = False


host = 'localhost'
port = 12355
s = socket.socket()
s.connect((host, port))

sql_conn = sql.connect('EvaluationLvl3.db')
c = sql_conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS messages (time TEXT,sender TEXT,msg TEXT)')


def send():
    global SENT_EXIT
    readable = entry_box.get()
    entry_box.delete(0, END)

    if readable.strip().lower() == 'exit':
        s.sendall(readable.encode())
        SENT_EXIT = True
        on_exit()
    else:
        msg = f'{time.time()}, from client: {readable}'

        if len(msg) > 1024:
            msg = msg[:1024]
        elif len(msg) < 1024:
            msg = msg + ' ' * (1024 - len(msg))

        s.sendall(msg.encode())
        c.execute('INSERT INTO messages VALUES (?,?,?)', (str(time.time()), 'client', readable))
        sql_conn.commit()

        message_box['state'] = 'normal'
        message_box.insert(END, msg.strip() + '\n')
        message_box['state'] = 'disabled'


def listen():
    global SENT_EXIT
    while True:
        try:
            received = s.recv(1024)
        except:
            received = ('exit' + ' ' * 1020).encode()

        msg = received.decode().strip()
        if msg.lower() == 'exit':
            SENT_EXIT = True
            on_exit()
        else:
            message_box['state'] = 'normal'
            message_box.insert(END, msg + '\n')
            message_box['state'] = 'disabled'

def on_exit():
    print('exiting')
    global APP_OPEN, SQL_OPEN, CONNECTED, SENT_EXIT, root, sql_conn, s
    if APP_OPEN:
        root.destroy()
        APP_OPEN = False
    
    if SQL_OPEN:
        sql_conn.close()
        SQL_OPEN = False
    
    if not SENT_EXIT:
        s.sendall(('exit' + ' ' * 1020).encode())
        SENT_EXIT = True

    if CONNECTED:
        s.close()
        CONNECTED = False


root = Tk()
root.title("Client")
root.protocol("WM_DELETE_WINDOW", on_exit)
APP_OPEN = True


listen_thread = threading.Thread(target=listen)
listen_thread.start()

message_box = Text(root)
message_box['state'] = 'disabled'

messages = c.execute('SELECT * FROM messages')
print(messages)
last_five = messages.fetchall()[-5:]
print(last_five)
for message in last_five:
    msg = f'{message[0]}, from {message[1]}: {message[2]}'
    print(msg)

    message_box['state'] = 'normal'
    message_box.insert(END, msg + '\n')
    message_box['state'] = 'disabled'

entry_box = Entry(root)
send_button = Button(root, text='Send', command=send)

message_box.pack()
entry_box.pack()
send_button.pack()

root.mainloop()
