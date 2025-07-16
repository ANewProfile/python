import string

LOWERCASE = [letter for letter in string.ascii_lowercase]
UPPERCASE = [letter for letter in string.ascii_uppercase]


def encode(plaintext, shift):
    cipher = []
    for letter in plaintext:
        if letter == " ":
            cipher.append(letter)
        elif letter not in LOWERCASE and letter not in UPPERCASE:
            return "!letter"
        else:
            if letter in LOWERCASE:
                key_of_letter = LOWERCASE.index(letter)
                key_of_letter += shift
                key_of_letter %= 26
                cipher.append(LOWERCASE[key_of_letter])
            elif letter in UPPERCASE:
                key_of_letter = UPPERCASE.index(letter)
                key_of_letter += shift
                key_of_letter %= 26
                cipher.append(UPPERCASE[key_of_letter])

    return "".join(cipher)

def decode(cipher, shift):
    plaintext = []
    for letter in cipher:
        if letter == " ":
            plaintext.append(letter)
        elif letter not in LOWERCASE and letter not in UPPERCASE:
            return "!letter"
        else:
            if letter in LOWERCASE:
                key_of_letter = LOWERCASE.index(letter)
                key_of_letter -= shift
                key_of_letter += 26
                key_of_letter %= 26
                plaintext.append(LOWERCASE[key_of_letter])
            elif letter in UPPERCASE:
                key_of_letter = UPPERCASE.index(letter)
                key_of_letter -= shift
                key_of_letter += 26
                key_of_letter %= 26
                plaintext.append(UPPERCASE[key_of_letter])

    return "".join(plaintext)

def main():
    encode_decode = input("Would you like to [e]ncode or [d]ecode? ")
    text = input("What would you like to encode/decode? ")
    shift = input("What is the shift? ")
    try:
        shift = int(shift)
    except ValueError:
        raise Exception("You did not enter an integer for shift")

    if encode_decode.lower() not in ("e", "d"):
        print("NOT CORRECT INPUT. PLEASE ENTER 'E' or 'D'")
    elif encode_decode.lower() == "e":
        print(encode(text, shift))
    elif encode_decode.lower() == "d":
        print(decode(text, shift))


if __name__ == "__main__":
    main()
