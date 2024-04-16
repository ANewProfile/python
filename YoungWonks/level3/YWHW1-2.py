from tkinter import *


root = Tk()
root.title('Calculator')


def add():
    try:
        print(float(first_num_box.get()) + float(second_num_box.get()))
    except ValueError:
        print('Please enter two valid floats (or integers)')

def subtract():
    try:
        print(float(first_num_box.get()) - float(second_num_box.get()))
    except ValueError:
        print('Please enter two valid floats (or integers)')

def multiply():
    try:
        print(float(first_num_box.get()) * float(second_num_box.get()))
    except ValueError:
        print('Please enter two valid floats (or integers)')

def divide():
    try:
        print(float(first_num_box.get()) / float(second_num_box.get()))
    except ValueError:
        print('Please enter two valid floats (or integers)')


first_num_label = Label(root, text='Enter the first number:')
first_num_box = Entry(root)

second_num_label = Label(root, text='Enter the second number:')
second_num_box = Entry(root)

add_button = Button(root, text='Addition', command=add)
subtract_button = Button(root, text='Subtraction', command=subtract)
multiply_button = Button(root, text='Multiplication', command=multiply)
divide_button = Button(root, text='Division', command=divide)

first_num_label.pack()
first_num_box.pack()
second_num_label.pack()
second_num_box.pack()
add_button.pack()
subtract_button.pack()
multiply_button.pack()
divide_button.pack()


root.mainloop()
