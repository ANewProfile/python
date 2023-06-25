import tkinter as tk


text_color = '#000000'
button_width = 0
button_height = 0
title_font = ('BM Hanna 11yrs Old', 50)
buttton_font = ('Krungthep', 30)


class AddFrame:
    def __init__(self, window):
        self.frame = tk.Frame(master=window,
                              width=button_width * 2,
                              height=button_height)
        self.master = window
        
        self.name = tk.StringVar(master=self.frame, value='')
        self.id = tk.StringVar(master=self.frame, value='')
        self.link = tk.StringVar(master=self.frame, value='')
        self.rating = tk.StringVar(master=self.frame, value='')
        self.loc = tk.StringVar(master=self.frame, value='')
        self.type = tk.StringVar(master=self.frame, value='')
        self.fav_dishes = tk.StringVar(master=self.frame, value='')
        self.is_open = tk.StringVar(master=self.frame, value='')
        self.submit_btn = tk.Button(master=self.frame,
                                    command=self.submit,
                                    text='SUBMIT')

        self.name_entry = tk.Entry(master=self.frame,
                                   textvariable=self.name)
        
        self.name_entry.pack()
        self.submit_btn.pack()
    
    def submit(self):
        print(self.name.get())


class ViewFrame:
    def __init__(self, window):
        self.frame = tk.Frame(master=window,
                              width=button_width * 2,
                              height=button_height)
        self.master = window


class GUIWindow:
    def __init__(self):
        self.show_add = False
        self.show_view = False

        self.window = tk.Tk()
        self.nav_frame = tk.Frame(master=self.window,
                                  width=button_width * 2,
                                  height=button_height)
        self.add_frame = AddFrame(self.window)
        self.view_frame = ViewFrame(self.window)
        self.title_frame = tk.Label(master=self.window,
                                    width=0,
                                    height=0,
                                    text='Restaurant Tracker',
                                    font=title_font)


        self.add_button = tk.Button(master=self.nav_frame,
                                    fg=text_color, text='Add',
                                    width=button_width,
                                    height=button_height,
                                    font=buttton_font,
                                    command=self.show_add_frame)
        self.add_button.pack(fill=tk.Y, side=tk.LEFT)

        self.view_button = tk.Button(master=self.nav_frame,
                                    fg=text_color, text='View',
                                    width=button_width,
                                    height=button_height,
                                    font=buttton_font,
                                    command=self.show_view_frame)
        self.view_button.pack(fill=tk.Y, side=tk.RIGHT)


        self.title_frame.pack()
        self.nav_frame.pack()
        self.window.mainloop()
    
    def show_add_frame(self):
        self.add_frame.frame.pack()
        self.view_frame.frame.pack_forget()
    
    def show_view_frame(self):
        self.view_frame.frame.pack()
        self.add_frame.frame.pack_forget()
