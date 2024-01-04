import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello' or p_message == 'hi':
        return 'Hey there!'
    elif p_message == 'roll':
        return str(random.randint(1, 6))
    elif p_message == 'help':
        return '911 what is your emergency? Nothing? Okay, bye!'
    elif p_message == 'kill':
        return 'That doesn\'t do anything! Try /suicide'
    elif p_message == 'suicide':
        return 'That doesn\'t do anything either. Too bad!'
    else:
        return 'Not a valid command. Do /help for a list of commands!'
