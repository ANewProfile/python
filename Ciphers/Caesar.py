def preprocess_text(text):
    return ''.join(filter(str.isalpha, text.upper()))

def shift_char(c, shift, encode=True):
    base = ord('A')
    offset = shift if encode else -shift
    return chr((ord(c) - base + offset) % 26 + base)

def encode(plaintext, shift):
    text = preprocess_text(plaintext)
    return ''.join(shift_char(c, shift, encode=True) for c in text)

def decode(ciphertext, shift):
    text = preprocess_text(ciphertext)
    return ''.join(shift_char(c, shift, encode=False) for c in text)

def main():
    encode_decode = input("Would you like to [e]ncode or [d]ecode? ")
    if encode_decode.lower() not in ("e", "d"): raise Exception("Please press either 'e' or 'd'!")
    text = input("What would you like to encode/decode? ")
    shift = input("What is the shift? ")
    if encode_decode.lower() == "e":
        pt = text
        ct = encode(text, shift)
    else:
        pt = decode(text, shift)
        ct = text

    print(`Encoded: {pt}`)
    print(`Decoded: {ct}`)


if __name__ == "__main__":
    main()
