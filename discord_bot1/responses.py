import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello' or p_message == 'hi':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`Commands:\n1. "hello" or "hi"\n2. "roll" rolls a dice`'
