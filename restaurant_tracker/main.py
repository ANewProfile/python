import requests
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
# *Loc: Loc - User/Calc
# Type: Array/Tuple[String] - User
# Fav_Dishes: Array/Tuple[String] - User
# Notes: Array/Tuple[String] - User
# *IsOpen: Boolean - Calculated [default True]


class Loc:
    def __init__(self, city, country, response) -> None:
        self.city = city
        self.country = country
        self.lalo = (response['latitude'], response['longitude'])


def slugify(text: str):
    lower_text: str = text.lower()
    no_spaces: list = lower_text.split(' ')
    final: str = '-'.join(no_spaces)
    
    return final


def get_user_inputs() -> dict:
    items = {}

    # Restaurant Name
    name = input('Enter the name (return to cancel): ')
    if name == '':
        return None
    items['Name'] = name

    # Restaurant ID
    id = slugify(name)
    items['_id'] = id

    # Restaurant Link
    link = input('Enter the link (optional): ')
    if link != '':
        items['Link'] = link
    
    # Restaurant Rating
    while True:
        try:
            rating = float(input('Enter the rating: '))
            items['Rating'] = rating
            break
        except:
            print('Not a valid number.')
            continue
    
    # Restaurant Location
    city = input('What city is the restaurant in? ').lower()
    country = input('What country is the restaurant in? ').lower()
    # response = 'https://api.radar.io/v1/geocode/forward?query=841+broadway+new+york'
    url = f'https://api.radar.io/v1/geocode/forward?query={city},+{country}'
    response = requests.get(url, headers={'Authorization': 'prj_live_sk_9f1c623207cfd14adabf5ed963d167f327e22df7'}).json()
    loc = [Loc(city, country, addr) for addr in response["addresses"]][0]
    items['Loc'] = loc

    # Restaurant Type(s)
    types = []
    while True:
        type = input('Type of cuisine (return to cancel): ')
        if type == '':
            break
        types.append(type)
    if types != []:
        items['Type'] = types
    
    # Restaurant Favorite Dish(es)
    dishes = []
    while True:
        dish = input('Fav Dish (return to cancel): ')
        if dish == '':
            break
        dishes.append(dish)
    if dishes != []:
        items['Fav_Dishes'] = dishes
    
    # Restaurant Note(s)
    notes = []
    while True:
        note = input('Note (return to cancel): ')
        if note == '':
            break
        notes.append(note)
    if notes != []:
        items['Notes'] = notes

    # Restaurant Open - Default True
    items['IsOpen'] = True


    return items


# print(get_user_inputs())
entry = get_user_inputs()
print('\n\n\n')
confirm = input('Confirm [y/n]: ')

if confirm.lower() == 'y':
    # entry = get_user_inputs()
    loc_object: Loc = entry['Loc']
    entry['Loc'] = {'city': loc_object.city, 'country': loc_object.country, 'lat-long': loc_object.lalo}
    restaurantDB.insert_one(entry)
else:
    print('Ok! Thanks!')