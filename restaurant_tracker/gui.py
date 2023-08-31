import tkinter as tk
from tkinter import messagebox
import re
from loc_object import Loc
import requests
from pprint import pprint
import pymongo


text_color = '#000000'
button_width = 0
button_height = 0
title_font = ('BM Hanna 11yrs Old', 50)
buttton_font = ('Krungthep', 30)


def slugify(text: str):  # $Text Text
    processed_text: str = re.sub('\W', '', text)  # Text Text
    lower_text: str = processed_text.lower()  # text text
    final: str = lower_text.replace(' ', '-')  # text-text
    
    return final


class InputFrame(tk.Frame):
    def __init__(self, master, label: str) -> None:
        super().__init__(master)
        self.label = tk.Label(master=self,
                              text=label)
        self.string_var = tk.StringVar(master=self,
                                       value='')
        self.entry = tk.Entry(master=self,
                              textvariable=self.string_var)
    
    def get(self):
        return self.string_var.get()
    
    def pack(self):
        self.label.pack(side='left')
        self.entry.pack(side='right')
        super().pack()


class AddFrame:
    def __init__(self, window):
        self.frame = tk.Frame(master=window,
                              width=button_width * 2,
                              height=button_height)
        self.master = window
        
        # Variables
        self.name = InputFrame(self.frame, 'Name')
        self.link = InputFrame(self.frame, 'Link')
        self.rating = InputFrame(self.frame, 'Rating')
        self.city = InputFrame(self.frame, 'City')
        self.country = InputFrame(self.frame, 'Country/State')
        self.type = InputFrame(self.frame, 'Type of Cuisine')
        self.fav_dishes = InputFrame(self.frame, 'Notable Dishes')
        self.submit_btn = tk.Button(master=self.frame,
                                    command=self.submit,
                                    text='SUBMIT')

        # Pack
        self.name.pack()
        self.link.pack()
        self.rating.pack()
        self.city.pack()
        self.country.pack()
        self.type.pack()
        self.fav_dishes.pack()
        self.submit_btn.pack()
    
    def validate_types(self):
        restaurantEntry = {}
        name = self.name.get()
        types = self.type.get().lower().replace(', ', ',').split(',')
        dishes = self.fav_dishes.get().lower().replace(', ', ',').split(',')
        try:
            city = self.city.get().lower()
            country = self.country.get().lower()
            url = f'https://api.radar.io/v1/geocode/forward?query={city},+{country}'
            response = requests.get(url, headers={'Authorization': 'prj_live_sk_9f1c623207cfd14adabf5ed963d167f327e22df7'}).json()
            # print(response)
            loc = [Loc(city, country, addr) for addr in response["addresses"]][0]
            # print(f'\n\n\nLocation Found: {response["addresses"][0]["formattedAddress"]}')
        except IndexError:
            return 'Invalid Location.'

        restaurantEntry['Name'] = name
        restaurantEntry['_id'] = slugify(name)
        restaurantEntry['Link'] = self.link.get()
        try:
            rating = float(self.rating.get())
            if (rating >= 0) and (rating <= 10):
                restaurantEntry['Rating'] = rating
            else:
                return "Rating must be between 0 and 10"
        except ValueError:
            return "Invalid rating."
        restaurantEntry['Loc'] = loc.to_dictionary()
        if types == ['']:
            return "Type required"
        else:
            restaurantEntry['Type'] = types
        if dishes == ['']:
            dishes = []
        restaurantEntry['Fav_Dishes'] = dishes

        return restaurantEntry

    def submit(self):
        # pprint(self.validate_types())
        try:
            validation = self.validate_types()
            if type(validation) is dict:
                result = GUIWindow.restaurantDB.insert_one(validation)        
                if result.acknowledged:
                    messagebox.showinfo('Success', 'Added to database.')
                    # pprint(result)
                else:
                    messagebox.showerror('Invalid', 'Invalid Operation')
            elif type(validation) is str:
                error = validation
                messagebox.showerror('Validation Error', error)
            else:
                messagebox.showerror('You shouldn\'t be seeing this', 'This error message should NEVER appear.')
        except pymongo.errors.DuplicateKeyError:
            messagebox.showerror('Duplicate Error', 'Entry has already been entered')
        except:
            messagebox.showerror('Unknown Error', 'An unknown error occurred')



class ViewFrame:
    def __init__(self, window):
        self.frame = tk.Frame(master=window,
                              width=button_width * 2,
                              height=button_height)
        self.master = window


class GUIWindow:
    def __init__(self, client):
        GUIWindow.client = client
        GUIWindow.restaurantDB = client['restaurants'].entries
        self.show_add = False
        self.show_view = False

        self.window = tk.Tk()
        self.window.title('Restaurant Tracker')
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
