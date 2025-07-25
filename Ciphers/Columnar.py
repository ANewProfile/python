import math

def preprocess_text(text):
    return ''.join(filter(str.isalpha, text.upper()))

def keyword_order(keyword):
    return sorted(range(len(keyword)), key=lambda i: (keyword[i], i))

def encode(plaintext, keyword):
    text = preprocess_text(plaintext)
    cols = len(keyword)
    rows = math.ceil(len(text) / cols)
    padded = text.ljust(rows * cols, 'X')  # pad with X

    grid = [list(padded[i:i+cols]) for i in range(0, len(padded), cols)]
    order = keyword_order(keyword)

    return ''.join(grid[r][c] for c in order for r in range(rows))

def decode(ciphertext, keyword):
    text = preprocess_text(ciphertext)
    cols = len(keyword)
    rows = math.ceil(len(text) / cols)
    total = rows * cols
    text = text.ljust(total, 'X')  # in case of missing padding

    order = keyword_order(keyword)
    inv_order = [0] * cols
    for i, pos in enumerate(order):
        inv_order[pos] = i

    col_lengths = [rows] * cols
    chunks = []
    idx = 0
    for _ in range(cols):
        chunks.append(text[idx:idx+rows])
        idx += rows

    grid = [['' for _ in range(cols)] for _ in range(rows)]
    for c, col_idx in enumerate(order):
        for r in range(rows):
            grid[r][col_idx] = chunks[c][r]

    return ''.join(''.join(row) for row in grid).rstrip('X')

def main():
    encode_decode = input("Would you like to [e]ncode or [d]ecode? ")
    if encode_decode.lower() not in ("e", "d"): raise Exception("Please press either 'e' or 'd'!")
    text = input("What would you like to encode/decode? ")
    codeword = input("What is the codeword? ")
    if not codeword:
        raise Exception("Please enter a codeword")
    if encode_decode.lower() == "e":
        pt = text
        ct = encode(text, codeword)
    else:
        pt = decode(text, codeword)
        ct = text

    print(f"Encoded: {pt}")
    print(f"Decoded: {ct}")



if __name__ == "__main__":
    main()
