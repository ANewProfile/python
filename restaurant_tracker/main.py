import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
restaurantDB = client['restaurants'].entries


# entry = {'_id': 'dishoom', \
#          'Name': 'Dishoom', \
#             'Link': 'https://www.yelp.com/biz/dishoom-london?osq=Dishoom', \
#                 'Rating': 7.125, \
#                     'Loc': 'London', \
#                         'Type': ['Indian', 'Aranian'], \
#                             'Fav_Dishes': ['Steamed Veggie Bowl'], \
#                                 'Notes': ['Very popular', 'Long line'], \
#                                     'IsOpen': True}


# *Name: String - User
# *Id: slugify(name) - Calculated
# Link: String - User
# *Rating: Float/Double - User
# *Loc: Loc - User
# Type: Array/Tuple[String] - User
# Fav_Dishes: Array/Tuple[String] - User
# Notes: Array/Tuple[String] - User
# *IsOpen: Boolean - Calculated [default True]


def slugify(text: str):
    lower_text: str = text.lower()
    no_spaces: list = lower_text.split(' ')
    final: str = '-'.join(no_spaces)
    
    return final


def get_user_inputs():
    items = {}

    name = input('Enter the name (return to cancel): ')
    if name == '':
        return None
    items['Name'] = name

    id = slugify(name)
    items['_id'] = id

    link = input('Enter the link (optional): ')
    if link != '':
        items['Link'] = link
    
    while True:
        try:
            rating = float(input('Enter the rating: '))
            items['Rating'] = rating
            break
        except:
            print('Not a valid number.')
            continue
    
    # XXX LOCATION - IMPLEMENT ME

    types = []
    while True:
        type = input('Type of cuisine (return to cancel): ')
        if type == '':
            break
        types.append(type)
    if types != []:
        items['Type'] = types
    
    dishes = []
    while True:
        dish = input('Fav Dish (return to cancel): ')
        if dish == '':
            break
        dishes.append(dish)
    if dishes != []:
        items['Fav_Dishes'] = dishes
    
    notes = []
    while True:
        note = input('Type of cuisine (return to cancel): ')
        if note == '':
            break
        notes.append(note)
    if notes != []:
        items['Notes'] = notes

    items['IsOpen'] = true


    return items


print(get_user_inputs())

# restaurantDB.insert_one(entry)
