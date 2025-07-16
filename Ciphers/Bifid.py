def generate_polybius_square():
    square = {}
    reverse_square = {}
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is merged with I
    index = 0
    for row in range(5):
        for col in range(5):
            letter = alphabet[index]
            square[letter] = (row, col)
            reverse_square[(row, col)] = letter
            index += 1
    return square, reverse_square

def preprocess_text(text):
    return text.upper().replace("J", "I").replace(" ", "")

def encode(plaintext):
    square, _ = generate_polybius_square()
    plaintext = preprocess_text(plaintext)

    rows = []
    cols = []
    for char in plaintext:
        if char in square:
            row, col = square[char]
            rows.append(row)
            cols.append(col)

    combined = rows + cols
    coords = list(zip(combined[::2], combined[1::2]))

    ciphertext = ""
    for row, col in coords:
        for key, value in square.items():
            if value == (row, col):
                ciphertext += key
                break
    return ciphertext

def decode(ciphertext):
    square, _ = generate_polybius_square()
    ciphertext = preprocess_text(ciphertext)

    coords = []
    for char in ciphertext:
        if char in square:
            coords.append(square[char][0])
            coords.append(square[char][1])

    half = len(coords) // 2
    rows = coords[:half]
    cols = coords[half:]

    plaintext = ""
    for r, c in zip(rows, cols):
        for key, value in square.items():
            if value == (r, c):
                plaintext += key
                break
    return plaintext

def main():
    pt = "ROCKET LAUNCH SPOT"
    ct = encode(pt)
    print("Encoded:", ct)
    dt = decode(ct)
    print("Decoded:", dt)

if __name__ == "__main__":
    main()
