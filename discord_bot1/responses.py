import random


def get_response(message: str) -> str:
    p_message = message.lower()
    user = message.author

    if p_message == 'hello' or p_message == 'hi':
        return f'Hey there, {user}!'

    if p_message == 'roll':
        return f'Your dice roll is: {str(random.randint(1, 6))}'

    if p_message == '!help':
        return '`I\'m not helping you!`'
