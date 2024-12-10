from tkinter import *
import socket


def send():
    message = input_box.get()
    if not message:
        return
    
    message_box['state'] = 'normal'
    message_box.insert(END, message + '\n')
    message_box['state'] = 'disabled'
    
    input_box.delete(0, END)


root = Tk()
root.title('Messaging App')

s = socket.socket()
host = 'localhost'
port = 12345

s.bind((host, port))
s.listen()
conn, addr = s.accept()

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
