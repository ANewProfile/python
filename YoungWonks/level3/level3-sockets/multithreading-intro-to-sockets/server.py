from tkinter import *
from tkinter import messagebox
import socket
from threading import Thread


def send():
    message = input_box.get()
    if not message:
        return

    if message.lower() == 'exit':
        on_exit(close_conn=True, exit_sent=False)

    if len(message) > 1024:
        send_message = message[:1024]
    else:
        send_message = message + ' '*(1024-len(message))

    message_box['state'] = 'normal'
    message_box.insert(END, send_message + '\n')
    message_box['state'] = 'disabled'

    conn.sendall(send_message.encode())
    
    input_box.delete(0, END)

def listen():
    try:
        message = conn.recv(1024).decode()
    except:
        message = 'exit'

    if message.lower().strip() != 'exit':
        message_box['state'] = 'normal'
        message_box.insert(END, message.strip() + '\n')
        message_box['state'] = 'disabled'
    else:
        response = messagebox.askyesno('Close?', 'The other person left, would you like to close the window?')
        if response:
            on_exit(close_conn=False, exit_sent=False)

def on_exit(close_conn=True, exit_sent=False):
    root.destroy()
    if not exit_sent:
        exit_message = 'exit' + ' ' * 1020
        conn.sendall(exit_message.encode())
    if close_conn:
        conn.close()
    s.close()

root = Tk()
root.title('Messaging App')
root.protocol("WM_DELETE_WINDOW", on_exit)

s = socket.socket()
host = 'localhost'
port = 12346

s.bind((host, port))
s.listen(3)
conn, addr = s.accept()

t1 = Thread(target=listen)
t1.start()

messages_frame = Frame(root)
send_frame = Frame(root)

message_box = Text(messages_frame)
message_box['state'] = 'disabled'

input_box_label = Label(send_frame, text='Message')
input_box = Entry(send_frame)

send_button = Button(send_frame, text='Send', command=send)


message_box.pack()

input_box_label.grid(row=1, column=1)
input_box.grid(row=1, column=2)
send_button.grid(row=1, column=3)

messages_frame.pack()
send_frame.pack()

root.mainloop()
