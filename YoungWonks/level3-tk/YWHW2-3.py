from tkinter import *
from tkinter import messagebox


root = Tk()
cart = {
    
}
counter = IntVar()
counter.set(0)


def minus():
    old = counter.get()
    counter.set(old-1)
    
def plus():
    old = counter.get()
    counter.set(old+1)

def update_cart():
    cart[item_box.get()] = counter.get()
    
    counter.set(0)
    item_box.delete(0, END)

def checkout():
    items = []
    for item, count in cart.items():
        if count > 0:
            items.append(f'{item}: {count}\n')
    
    messagebox.showinfo('Checkout', f"Your items were:\n{''.join(items)}")


item_label = Label(root, text='Enter your item')
item_box = Entry(root)
count_label = Label(root, text='Enter how much you would like')
minus_button = Button(root, text='-', command=minus)
count = Label(root, textvariable=counter)
plus_button = Button(root, text='+', command=plus)
update_cart_button = Button(root, text='Update Cart', command=update_cart)
checkout_button = Button(root, text='Checkout', command=checkout)

item_label.pack()
item_box.pack()
count_label.pack()
minus_button.pack()
count.pack()
plus_button.pack()
update_cart_button.pack()
checkout_button.pack()


root.mainloop()