import tkinter as tk


# text_color = (0, 0, 0)
text_color = '#000000'
button_width = 0
button_height = 0
title_font = ('BM Hanna 11yrs Old', 50)
buttton_font = ('Krungthep', 30)


class GUIWindow:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.nav_frame = tk.Frame(master=self.window,
                                  width=button_width * 2,
                                  height=button_height)
        self.add_frame = tk.Frame(master=self.window,
                                  width=button_width * 2,
                                  height=button_height)
        self.title_frame = tk.Label(master=self.window,
                                  width=0,
                                  height=0,
                                  text='Restaurant Tracker',
                                  font=title_font)


        self.add_button = tk.Button(master=self.nav_frame,
                                    fg=text_color, text='Add',
                                    width=button_width,
                                    height=button_height,
                                    font=buttton_font)
        self.add_button.pack(fill=tk.Y, side=tk.LEFT)

        self.view_button = tk.Button(master=self.nav_frame,
                                    fg=text_color, text='View',
                                    width=button_width,
                                    height=button_height,
                                    font=buttton_font)
        self.view_button.pack(fill=tk.Y, side=tk.RIGHT)


        self.title_frame.pack()
        self.nav_frame.pack()
        self.add_frame.pack()
        self.window.mainloop()
