from tkinter import *

def check():
    input_username = username.get()
    if input_username in users:
        if users[input_username] == pswd.get():
            print(f'You are {input_username}!')
        else:
            print('Invalid username or password!')
    else:
        print('Invalid username or password!')
    
    username.delete(0, END)
    pswd.delete(0, END)
    

users = {
    'hungry': 'food',
    'thirsty': 'drink'
}

root = Tk()
root.title('Login')

username_label = Label(root, text='Username')
username = Entry(root)

pswd_label = Label(root, text='Password')
pswd = Entry(root, show='*')

button = Button(root, text='Login', command=check)

username_label.pack()
username.pack()
pswd_label.pack()
pswd.pack()
button.pack()


root.mainloop()
