import requests

url = input('What URL would you like to shorten? ')
api = requests.get(f'https://api.shrtco.de/v2/shorten', params={'url': url})
api = api.json()

# print('\n\n---------------')
# print(api['result']['short_link'])
# print('---------------\n\n')

if api['ok'] == False:
    error = api['error']
    print(f'Failure because: {error}.')
elif api['ok'] == True:
    origin = api['result']['original_link']
    shorturl = api['result']['short_link']
    print(
        f'Converted ||| {origin} ||| into a shortened URL.\nShortened URL is: {shorturl}')
