from bs4 import BeautifulSoup
import requests
hospital_university_lines = 0
#Step 1 create a url get function
def getdata(url):
    r = requests.get(url)
    return r.text

#Step 2 pass the url into get data and convert data to html code
htmldata = getdata("https://pokemondb.net/pokedex/national")
soup = BeautifulSoup(htmldata, 'html.parser')
results = soup.find_all("span",class_="infocard-lg-data")
#ent-name is name of pokemon
#infocard-lg-data is a list of pokemon and their types
# print(str(results))
# print("NO 1" +str(results[46:86]))

print('\nThis is a list of pokemon and their types\n')
for result in results:
    name = result.find("a", class_="ent-name")
    types = result.find_all("a", class_="itype")
    print(name.text)
    for type in types:
        print("\t·" + type.text)