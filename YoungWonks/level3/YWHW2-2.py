from tkinter import *


root = Tk()


def add_user():
    with open('YoungWonks/level3/YWHWAssets/applicants.txt', 'a') as applicants:
        applicants.write(f'{first_name_box.get()} {last_name_box.get()}: {age_box.get()}yo, {number_box.get()}\n')
    
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    age_box.delete(0, END)
    number_box.delete(0, END)


first_name_label = Label(root, text='First Name')
first_name_box = Entry(root)

last_name_label = Label(root, text='Last Name')
last_name_box = Entry(root)

age_label = Label(root, text='Age')
age_box = Entry(root)

number_label = Label(root, text='Phone Number')
number_box = Entry(root)

submit_button = Button(root, text='Submit', command=add_user)


first_name_label.pack()
first_name_box.pack()
last_name_label.pack()
last_name_box.pack()
age_label.pack()
age_box.pack()
number_label.pack()
number_box.pack()
submit_button.pack()


root.mainloop()
