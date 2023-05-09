from bs4 import BeautifulSoup


"""
Lesson 1 - Searching HTML Files
"""

import requests

url = 'https://www.newegg.com/asus-geforce-rtx-4070-tuf-rtx4070-o12g-gaming/p/N82E16814126637?Item=N82E16814126637&quicklink=true'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
price_elms = doc.find_all(class_="product-price")

for elm in price_elms:
    dollar_elms = elm.find_all(text="$")
    for dollar_elm in dollar_elms:
        parent = dollar_elm.parent

        strong = parent.find('strong')
        strong = int(strong.string)
        sup = parent.find('sup')
        sup = float(sup.string)

        price = strong + sup

        print(price)


"""
Lesson 2 - Search and Filter
"""

# import re

# with open('bs4test.html', 'r') as f:
#     doc = BeautifulSoup(f, 'html.parser')

# tags = doc.find_all('input', type='text')
# for tag in tags:
#     tag['placeholder'] = 'I canged you!'

# with open('changed.html', 'w') as file:
#     file.write(str(doc))
