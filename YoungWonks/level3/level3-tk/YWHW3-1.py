from tkinter import *


def send():
    message = message_box.get()
    if not message:
        return
    
    message_label = Label(messages_frame, text=message)
    message_label.pack()
    
    message_box.delete(0, END)


root = Tk()
root.title('One-Sided Messaging App')

messages_frame = Frame(root)
send_frame = Frame(root)

message_box_label = Label(send_frame, text='Message')
message_box = Entry(send_frame)

send_button = Button(send_frame, text='Send', command=send)


messages_frame.pack()
send_frame.pack()

message_box_label.pack()
message_box.pack()
send_button.pack()

root.mainloop()
