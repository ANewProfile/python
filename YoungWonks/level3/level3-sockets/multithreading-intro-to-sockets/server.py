from tkinter import *
import socket
from threading import Thread

running = True

def send():
    global running
    message = input_box.get()
    if not message:
        return

    if message.lower() == 'exit':
        running = False

    if len(message) > 1024:
        send_message = message[:1024]
    else:
        send_message = message + '0'*(1024-len(message))

    message_box['state'] = 'normal'
    message_box.insert(END, send_message + '\n')
    message_box['state'] = 'disabled'

    conn.sendall(send_message.encode())
    
    input_box.delete(0, END)

    if not running:
        conn.close()
        s.close()

def listen():
    global running
    while running:
        message = conn.recv(1024).decode().strip()

        if message.lower() != 'exit':
            message_box['state'] = 'normal'
            message_box.insert(END, message + '\n')
            message_box['state'] = 'disabled'
        else:
            running = False
    
    if not running:
        conn.close()
        s.close()

def on_exit():
    exit_message = 'exit' + ' ' * 1020
    conn.sendall(exit_message.encode())
    conn.close()
    s.close()
    root.destroy()

root = Tk()
root.title('Messaging App')
root.protocol("WM_DELETE_WINDOW", on_exit)

s = socket.socket()
host = 'localhost'
port = 12345

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
