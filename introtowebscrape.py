from bs4 import BeautifulSoup
import requests
hospital_university_lines = 0
#Step 1 create a url get function
def getdata(url):
    r = requests.get(url)
    return r.text

#Step 2 pass the url into get data and convert data to html code
htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
results = soup.find("div",class_="is_h5-2 is_vaccines w-richtext")
vaccines = str(soup.find_all("div",class_="is_h5-2 is_vaccines w-richtext")[0].get_text())
print('S1' + str(vaccines))
# print(str(results))

#is_h5-2 is_vaccines w-richtext is vaccine name
#is_h5-2 is_developer w-richtext is devoloper of vaccine
# print('\nThese are all the hospital universities reccommended for getting a drug if you have covid-19')
# for result in results:
#     if 'university' in result.text.lower():
#         if 'hospital' in result.text.lower():
#             print("\t -" + str(result.text))
#             hospital_university_lines += 1
#     # print(result.text)
#
# # print the number of hospital universities
# print('\nThere are ' + str(hospital_university_lines) + ' hospital universities')
# print(results.text[46:86])