import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message[0] == '/' or p_message[0] == '?':
        p_p_message = p_message[1:]
        if p_p_message == 'hello' or p_p_message == 'hi':
            return 'Hey there!'

        if p_p_message == 'roll':
            return str(random.randint(1, 6))
        
        return 'I didn\'t understand what you wrote. Try typing "!help".'

    if p_p_message == '!help':
        return '`Commands:\n1. "hello" or "hi"\n2. "roll" rolls a dice`'

