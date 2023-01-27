import termcolor

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', "%", '^', '&', '*', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '-', '_', '=', '+', '[', '{', ']', '}', '|', ':', '"', "'", ';', '/', '?', '>', '.', ',', '<', '`', '~']
encrypting = True
decrypting = False
sentence = ""
encryption_key = 0
encryption = ""
total_alphabet = len(alphabet)


def encrypt(num, sentence):
    sentence_letters = []
    for letter in sentence:
        index = alphabet.index(letter)
        shift_index = (index + num) % total_alphabet
        new_letter = alphabet[shift_index]
        sentence_letters.append(new_letter)
    return "".join(sentence_letters)


def decrypt(num, sentence):
    sentence_letters = []
    for letter in sentence:
        index = alphabet.index(letter)
        shift_index = (index - num) % total_alphabet
        new_letter = alphabet[shift_index]
        sentence_letters.append(new_letter)
    return "".join(sentence_letters)


print("Welcome to the encrypter/decrypter!")
while encrypting:
    sentence = input(
        "What is the sentence you want to encrypt? ")
    encryption_key = int(
        input("What encryption key would you like? "))
    encryption = encrypt(encryption_key, sentence)
    print(termcolor.colored(
        f"Your encrypted text is:", 'blue', attrs=['bold']))
    print(termcolor.colored(encryption, 'green'))
    continue_encrypting = input("Do you want to keep encrypting[y/n]? ")
    if continue_encrypting.lower() == "y":
        continue
    elif continue_encrypting.lower() == "n":
        encrypting = False
        decrypting = True
    else:
        print("Invalid.")

while decrypting:
    desentence = input(
        "What is the sentence you want to decrypt? ")
    decryption_key = int(
        input("What decryption key would you like? "))
    decryption = decrypt(decryption_key, desentence)
    print(termcolor.colored(
        f"Your decrypted text is:", 'blue', attrs=['bold']))
    print(termcolor.colored(f'{decryption}', 'green'))
    decrypting = False
