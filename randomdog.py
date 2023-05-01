import requests

pic_api = requests.get("https://random.dog/woof.json")
pic_api = pic_api.json()

# fact_api = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/?number=1")
# fact_api = fact_api.json()
# print(dir(fact_api))

pic_address = pic_api['url']
# fact = fact_api[0]['fact']

print(f'Your pic address is: {pic_address}')
