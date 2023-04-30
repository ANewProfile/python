import requests

which = input('Would you like to get the [d]aily fact or a [r]andom fact? ')
if which.lower() == 'r':
    api = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random')
elif which.lower() == 'd':
    api = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/today')
else:
    print('Invalid')

# print(api.json())

json = api.json()
fact = json['text']
source = json['source_url']

print(f'Here\'s your fact!\n{fact}\nSource: {source}')