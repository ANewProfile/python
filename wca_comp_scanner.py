import requests
from bs4 import BeautifulSoup
import termcolor
from pprint import pprint


def get_data(url):
    response = requests.get(url).text

    return response

def name_comps(comps):
    comp_names = []
    for comp in comps:
        name = comp.a.string
        comp_names.append(name)
    
    return comp_names

def get_locs(locs):
    loc_list = []
    for loc in locs:
        loc_name = loc.text
        loc_list.append(loc_name.replace('\n', '').replace('        ', ''))
    
    return loc_list

def get_opens(opens):
    open_list = []
    for open in opens:
        red_elm = open.findChildren(class_="red")
        green_elm = open.findChildren(class_="green")
        open_list.append(len(green_elm) > 0)

    return open_list


urls = ['https://www.worldcubeassociation.org/competitions?region=all&search=Massachusetts&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list',
        'https://www.worldcubeassociation.org/competitions?region=all&search=Rhode+Island&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list',
        'https://www.worldcubeassociation.org/competitions?region=all&search=New+Hampshire&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list',
        'https://www.worldcubeassociation.org/competitions?region=all&search=Connecticut&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list']

comps_locs_list = []


for url in urls:
    html = get_data(url)
    doc = BeautifulSoup(html, 'html.parser')
    list_group = doc.find(class_='list-group')
    # comp_list = soup.find(id='upcoming-comps', _class='col-md-12')
    # num_comps = list_group.find('strong')
    # num_comps = comp_list.strong
    try:
        comps_html = list_group.find_all(class_='competition-link')
        locs_html = list_group.find_all(class_='location')
        open_html = list_group.find_all(class_='date')
    except AttributeError:
        pass
    comps = name_comps(comps_html)
    locs = get_locs(locs_html)
    opens = get_opens(open_html)
    comps_locs = list(zip(locs, comps, opens))
    for item in comps_locs:
        if item not in comps_locs_list:
            comps_locs_list.append(item)
            # print("adding", item, "from", url)


# print(termcolor.colored(num_comps.string, 'blue', attrs=['bold']))
# print('----------------------------------------------------------\n')
# for item in comps_locs:
#     color = 'light_red' if item[2] is False else 'light_green'
#     print(termcolor.colored(f'{item[1]} --- {item[0]}', color, attrs=['bold', 'concealed']))


max_name_length = max(len(item[1]) for item in comps_locs_list)

for item in comps_locs_list:
    color = 'red' if item[2] is False else 'light_green'
    name = item[1].ljust(max_name_length)
    print(termcolor.colored(f'{name} --- {item[0]}', color, attrs=['bold']))
