import requests

while True:
    which = input('Would you like to see the data for a specific [p]rofile or the current [s]tats for a specific player? ')
    if which.lower() == 'p':
        prof = input('What is the username of the account you would like to see? ')
        api = requests.get(f'https://api.chess.com/pub/player/{prof}')
        if api.status_code == 200:
            api = api.json()

            title = api['title'] if 'title' in api else None
            name = api['username']
            id = api['player_id']
            name = api['username']
            id = api['player_id']

            # try:
            #     name = api['username']
            #     id = api['player_id']
            # except KeyError:
            #     print('Invalid Username.')
            #     continue
            # except requests.exceptions.JSONDecodeError:
            #     print('Invalid Username.')
            #     continue

            status = api['status']
            
            print(f'\n\nUsername: {name}\n\
ID: {id}\n\
Title: {title}\n\
Status: {status}')
            break
        else:
            print('ERROR.')
    elif which.lower() == 's':
        prof = input('What is the username you would like to see the stats of? ')
        api = requests.get(f'https://api.chess.com/pub/player/{prof}/stats')
        if api.status_code == 200:
            api = api.json()

            cur_blitz = api['chess_blitz']['last']['rating']
            best_blitz = api['chess_blitz']['best']['rating']
            rush = api['puzzle_rush']['best']['score']
            tactics = api['tactics']['highest']['rating']

            print(f'\n\nBlitz: {cur_blitz}(current), {best_blitz}(best)\n\
Puzzle Rush: {rush}(most)\n\
Tactics/Puzzles: {tactics}(highest)')
            break
        else:
            print('Invalid.')
            continue
