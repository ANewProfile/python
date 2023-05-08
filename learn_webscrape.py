from bs4 import BeautifulSoup
import requests

url = 'https://www.newegg.com/asus-geforce-rtx-4070-tuf-rtx4070-o12g-gaming/p/N82E16814126637?Item=N82E16814126637&quicklink=true'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
prices = doc.find_all(text="$")
parent = prices[0].parent

strong = parent.find('strong')
strong = int(strong.string)
sup = parent.find('sup')
sup = float(sup.string)

price = strong + sup

print(price)