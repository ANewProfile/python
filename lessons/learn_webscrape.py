import re
import requests
from bs4 import BeautifulSoup

"""
Lesson 1 - Searching HTML Files
"""


# url = 'https://www.newegg.com/asus-geforce-rtx-4070-tuf-rtx4070-o12g-gaming/p/N82E16814126637?Item=N82E16814126637&quicklink=true'
# result = requests.get(url)

# doc = BeautifulSoup(result.text, 'html.parser')
# price_elms = doc.find_all(class_="product-price")

# for elm in price_elms:
#     dollar_elms = elm.find_all(text="$")
#     for dollar_elm in dollar_elms:
#         parent = dollar_elm.parent

#         strong = parent.find('strong')
#         strong = int(strong.string)
#         sup = parent.find('sup')
#         sup = float(sup.string)

#         price = strong + sup

#         print(price)


"""
Lesson 2 - Search and Filter
"""


# with open('bs4test.html', 'r') as f:
#     doc = BeautifulSoup(f, 'html.parser')

# tags = doc.find_all(text=re.compile('\$.*'))

# tags = doc.find_all('input', type='text')
# for tag in tags:
#     tag['placeholder'] = 'I canged you!'

# with open('changed.html', 'w') as file:
#     file.write(str(doc))


"""
Lesson 3 - Navigating the HTML Tree
"""


# url = 'https://coinmarketcap.com/'
# result = requests.get(url).text
# doc = BeautifulSoup(result, 'html.parser')

# tbody = doc.tbody
# trs = tbody.contents

# # print(trs[0].next_sibling) # looks at the next sibling (item on the same column)
# # print(trs[1].previous_sibling) # looks at the previous sibling
# # print(trs[0].next_siblings) # looks at all of the next sibilings
# # print(trs[4].previous_siblings) # looks at all of the previous siblings
# # print(trs[0].parent) # looks at the parent (item that this item is inside of)
# # print(trs[0].find_parent('parent-name-here')) # looks at the first instance of a specific parent
# # print(trs[0].parent.name) # .name looks at the name of an object
# # print(trs[0].descendants) # looks at all of the descendants (things that are inside of this object)
# # print(trs[0].contents) # looks at all of the descendants
# # print(trs[0].children) # looks at all of the descendants, but will not give nested tags

# prices = {}

# for tr in trs[:10]:
#     name, price = tr.contents[2:4]
#     fixed_name = name.p.string
#     fixed_price = price.a.string

#     prices[fixed_name] = fixed_price

# print('\n-----------------------------------------------------')
# for name, price in prices.items():
#     print(f'Name: {name}\nPrice: {price}\n-----------------------------------------------------')

# # print("\n".join(prices))


"""
Lesson 4 - Finding the Best GPU Prices
"""


search_term = input("What product do you want to search for? ")

url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

for page in range(1, pages + 1):
	url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}"
	page = requests.get(url).text
	doc = BeautifulSoup(page, "html.parser")

	div = doc.find(
		class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
	items = div.find_all(text=re.compile(search_term))

	for item in items:
		parent = item.parent
		if parent.name != "a":
			continue

		link = parent['href']
		next_parent = item.find_parent(class_="item-container")
		try:
			price = next_parent.find(class_="price-current").find("strong").string
			items_found[item] = {"price": int(price.replace(",", "")), "link": link}
		except:
			pass

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
	print(item[0])
	print(f"${item[1]['price']}")
	print(item[1]['link'])
	print("-------------------------------")
