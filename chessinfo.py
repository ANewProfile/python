import requests

which = input('Would you like to see the data for a specific [p]rofile or the current [s]tats for a specific player? ')
if which.lower() == 'p':
    prof = input('What is the username of the account you would like to see? ')
    api = requests.get(f'https://api.chess.com/pub/player/{prof}')
    api = api.json()

    name = api['username']
    id = api['player_id']
    try:
        title = api['title']
    except:
        title = None
        pass
    status = api['status']
    
    print(f'Username: {name}\n\
          ID: {id}\n\
          Title: {title}\n\
          Status: {status}')
elif which.lower() == 's':
    prof = input('What is the username you would like to see the stats of? ')
    api = requests.get(f'https://api.chess.com/pub/player/{prof}/stats')
    api = api.json()

    cur_blitz = api['chess_blitz']['last']['rating']
    best_blitz = api['chess_blitz']['best']['rating']
    rush = api['puzzle_rush']['best']['score']
    tactics = api['tactics']['highest']['rating']

    print(f'Blitz: {cur_blitz}(best), {best_blitz}(best)\n\
       Puzzle Rush: {rush}\n\
       Tactics: {tactics}(highest)')
else:
    print('Invalid.')
