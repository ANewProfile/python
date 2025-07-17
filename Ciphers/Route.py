import math

def preprocess_text(text):
    return ''.join(filter(str.isalpha, text.upper()))

def fill_grid(text, cols=5):
    rows = math.ceil(len(text) / cols)
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx < len(text):
                grid[r][c] = text[idx]
                idx += 1
    return grid

def spiral_coords(rows, cols, start_corner, clockwise):
    coords = []
    r1, r2, c1, c2 = 0, rows - 1, 0, cols - 1

    while r1 <= r2 and c1 <= c2:
        if clockwise:
            path = [
                [(r1, c) for c in range(c1, c2+1)],
                [(r, c2) for r in range(r1+1, r2+1)],
                [(r2, c) for c in reversed(range(c1, c2))] if r1 != r2 else [],
                [(r, c1) for r in reversed(range(r1+1, r2))] if c1 != c2 else []
            ]
        else:
            path = [
                [(r, c1) for r in range(r1, r2+1)],
                [(r2, c) for c in range(c1+1, c2+1)],
                [(r, c2) for r in reversed(range(r1, r2))] if c1 != c2 else [],
                [(r1, c) for c in reversed(range(c1+1, c2))] if r1 != r2 else []
            ]
        for part in path:
            coords.extend(part)
        r1 += 1; r2 -= 1; c1 += 1; c2 -= 1

    if start_corner == 'tr':
        coords = [(r, cols - 1 - c) for (r, c) in coords]
    elif start_corner == 'bl':
        coords = [(rows - 1 - r, c) for (r, c) in coords]
    elif start_corner == 'br':
        coords = [(rows - 1 - r, cols - 1 - c) for (r, c) in coords]
    return coords

def route_order(grid, route_type):
    rows, cols = len(grid), len(grid[0])
    if route_type.startswith('spiral'):
        corner, direction = route_type.split('_')[1:]
        clockwise = direction == 'cw'
        return spiral_coords(rows, cols, corner, clockwise)
    elif route_type == 'cols_lr':
        return [(r, c) for c in range(cols) for r in range(rows)]
    elif route_type == 'cols_rl':
        return [(r, c) for c in reversed(range(cols)) for r in range(rows)]
    elif route_type == 'rows_tb':
        return [(r, c) for r in range(rows) for c in range(cols)]
    elif route_type == 'rows_bt':
        return [(r, c) for r in reversed(range(rows)) for c in range(cols)]
    else:
        raise ValueError("Unsupported route type")

def encode(plaintext, route_type):
    text = preprocess_text(plaintext)
    grid = fill_grid(text)
    order = route_order(grid, route_type)
    return ''.join(grid[r][c] for r, c in order if grid[r][c])

def decode(ciphertext, route_type):
    text = preprocess_text(ciphertext)
    cols = 5
    rows = math.ceil(len(text) / cols)
    grid = [['' for _ in range(cols)] for _ in range(rows)]

    order = route_order(grid, route_type)
    for idx, (r, c) in enumerate(order):
        if idx < len(text):
            grid[r][c] = text[idx]

    return ''.join(''.join(row) for row in grid).rstrip()

def main():
    encode_decode = input("Would you like to [e]ncode or [d]ecode? ")
    if encode_decode.lower() not in ("e", "d"): raise Exception("Please press either 'e' or 'd'!")
    text = input("What would you like to encode/decode? ")
    type = input("What type of route will you use? ")
    if type not in ("spiral_tl_cw", "spiral_tr_ccw", "spiral_bl_cw", "spiral_br_ccw", "cols_lr", "cols_rl", "rows_tb", "rows_bt")
    if encode_decode.lower() == "e":
        pt = text
        ct = encode(text, type)
    else:
        pt = decode(text, type)
        ct = text

    print(`Encoded: {pt}`)
    print(`Decoded: {ct}`)


if __name__ == "__main__":
    main()
