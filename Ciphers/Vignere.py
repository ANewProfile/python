def preprocess_text(text):
    return ''.join(filter(str.isalpha, text.upper()))

def shift_char(c, k, encode=True):
    base = ord('A')
    offset = (ord(k) - base) * (1 if encode else -1)
    return chr((ord(c) - base + offset) % 26 + base)

def encode(plaintext, keyword):
    text = preprocess_text(plaintext)
    key = preprocess_text(keyword)
    full_key = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return ''.join(shift_char(c, k, encode=True) for c, k in zip(text, full_key))

def decode(ciphertext, keyword):
    text = preprocess_text(ciphertext)
    key = preprocess_text(keyword)
    full_key = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return ''.join(shift_char(c, k, encode=False) for c, k in zip(text, full_key))

def main():
    encode_decode = input("Would you like to [e]ncode or [d]ecode? ")
    if encode_decode.lower() not in ("e", "d"): raise Exception("Please press either 'e' or 'd'!")
    text = input("What would you like to encode/decode? ")
    keyword = input("What is the keyword? ")
    if encode_decode.lower() == "e":
        pt = text
        ct = encode(text, keyword)
    else:
        pt = decode(text, keyword)
        ct = text

    print(f"Encoded: {pt}")
    print(f"Decoded: {ct}")

if __name__ == "__main__":
    main()
