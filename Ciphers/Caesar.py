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
    plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    shift = 3

    encoded = encode(plaintext, shift)
    decoded = decode(encoded, shift)

    print("Shift:", shift)
    print("Encoded:", encoded)
    print("Decoded:", decoded)

if __name__ == "__main__":
    main()
