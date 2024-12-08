from tkinter import *
import webbrowser


root = Tk()
root.title('Link Buttons')

links = {
    'YouTube': 'https://www.youtube.com',
    'Google': 'https://www.google.com',
    'Reddit': 'https://www.reddit.com',
    'Twitter': 'https://www.twitter.com',
    'Facebook': 'https://www.facebook.com'
}

def add_link():
    if not link_name.get() or not link_url.get():
        return
    
    links[link_name.get()] = link_url.get()
    link_button = Button(buttons_frame, text=link_name.get(), command=webbrowser.open(link_url.get()))
    link_button.pack()
    link_name.delete(0, END)
    link_url.delete(0, END)


buttons_frame = Frame(root)
add_frame = Frame(root)

link_name_label = Label(add_frame, text='Link Name')
link_name = Entry(add_frame)

link_url_label = Label(add_frame, text='Link URL')
link_url = Entry(add_frame)
add_button = Button(add_frame, text='Add Link', command=add_link)

buttons_frame.pack()
for link in links:
    link_button = Button(buttons_frame, text=link, command=webbrowser.open(links[link]))
    link_button.pack()
    
add_frame.pack()
link_name_label.pack()
link_name.pack()
link_url_label.pack()
link_url.pack()
add_button.pack()

root.mainloop()