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
    plaintext = "THE UNBREAKABLE CIPHER"
    keyword = "GIOVAN"

    encoded = encode(plaintext, keyword)
    decoded = decode(encoded, keyword)

    print("Keyword:", keyword)
    print("Encoded:", encoded)
    print("Decoded:", decoded)

if __name__ == "__main__":
    main()
