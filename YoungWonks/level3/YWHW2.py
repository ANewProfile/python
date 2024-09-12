def fill(grid, move):
    new_grid = {x:y for x, y in grid.items()}
    new_grid[int(move[1])] = move[0]
    return new_grid

def check_board(grid):
    for i in range(1, 9 + 1):
        if not grid[i]:
            continue
        
        if i % 3 == 0:
            if (grid[i-1] == grid[i] or grid[i-2] == grid[i]):
                return False
        elif i % 3 == 1:
            if (grid[i+1] == grid[i] or grid[i+2] == grid[i]):
                return False
        else:
            if (grid[i-1] == grid[i] or grid[i+1] == grid[i]):
                return False

        if i in range(1, 3 + 1):
            if (grid[i+3] == grid[i] or grid[i+6] == grid[i]):
                return False
        elif i in range(1, 6 + 1):
            if (grid[i-3] == grid[i] or grid[i+3] == grid[i]):
                return False
        else:
            if (grid[i-3] == grid[i] or grid[i-6] == grid[i]):
                return False
    
    return True

def generate_moves(grid):
    possible = []
    for i in range(1, 9 + 1):
        if grid[i]:
            continue
        
        for letter in ('A', 'B', 'C'):
            fake_grid = {x: y for x, y in grid.items()}
            
            fake_grid[i] = letter
            # print(f"changing {i} to {letter}: {fake_grid}")
            if check_board(fake_grid):
                possible.append(letter+str(i))
    
    # print(possible)
    return possible
                

def solve_puzzle(grid):
    if not check_board(grid):
        print('board not good')
        return None
    
    if "" not in grid.values():
        return grid
    
    possible_next_moves = generate_moves(grid)
    # print('possible moves are', possible_next_moves)
    for move in possible_next_moves:
        new_board = fill(grid, move)
        # print("checking with new move", move)
        
        solved_board = solve_puzzle(new_board)
        if solved_board:
            return solved_board
    
    return None

def main(input: str):
    new_input = input.split(', ')
    new_input = "".join(new_input[1:])
    letters = [new_input[i:i+2] for i in range(0, len(new_input), 2)]
    grid = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    for letter_pair in letters:
        grid[int(letter_pair[0])] = letter_pair[1]

    # print(grid)
    # print(check_board(grid))
    grid = solve_puzzle(grid)

    return "".join(grid.values())
    # return grid

print(main('3, 1, A, 3, C, 8, A'))
print(main('3, 1, A, 6, C, 8, B'))
print(main('3, 1, B, 6, B, 9, C'))
print(main('2, 1, C, 5, B'))
print(main('2, 3, B, 7, A'))
