from bs4 import BeautifulSoup
import requests

#Step 1 create a url get function
def getdata(url):
    r = requests.get(url)
    return r.text

#Step 2 pass the url into get data and convert data to html code
htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
#result = str(soup.find_all("div",class_="is_h5-2 is_developer w-richtext"))
print(soup.prettify())
html = list(soup.children)[2]

body = list(html.children)[3]
print(len(body))