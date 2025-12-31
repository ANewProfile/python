from random import choice

WORDS: list[str] = []
NUMBERS_INT: list[int] = list(range(0, 10)) + [12, 28]
NUMBERS: list[str] = [str(num) for num in NUMBERS_INT]
SYMBOLS: list[str] = ["!", "@", "#", "$", "%", "^", "&", "*", ";", "/", "?", "+", "=", "-", "_"]
COIN1: int = choice((0, 1))
COIN2: int = choice((0, 1)) if COIN1 == 1 else 1
FIRST_CAP: bool = True if COIN1 == 1 else False
SECOND_CAP: bool = True if COIN2 == 1 else False

def random_word() -> str:
    return choice(WORDS)

def random_number() -> str:
    return choice(NUMBERS)

def random_symbol() -> str:
    return choice(SYMBOLS)

def word_part(caps: bool) -> str:
    word: str = random_word()
    if caps:
        return word.title()
    else:
        return word

def random_password() -> str:
    word_part_1 = word_part(FIRST_CAP)
    word_part_2 = word_part(SECOND_CAP)
    number = random_number()
    symbol = random_symbol()
    return "".join((word_part_1, word_part_2, number, symbol))

if __name__ == "__main__":
    password: str = random_password()
    print(password)
