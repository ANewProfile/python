def string_to_letters_counts(input: str):
    letters = []
    counts = []
    
    sort_input = sorted(input)
    
    for letter in sort_input:
        if letter == ' ':
            continue
        
        if letter.upper() in letters:
            counts[letters.index(letter.upper())] += 1
        else:
            letters.append(letter.upper())
            counts.append(1)
    
    return letters, counts

def update_history(new_letters, old_history):
    new_history = old_history.copy()
    
    for i in range(0, len(new_letters)):
        if new_history[i][-1] != new_letters[i]:
            new_history[i].append(new_letters[i])
    
    return new_history

def reset(input: str):
    letters, counts = string_to_letters_counts(input)
    return letters, counts, {}

def add(letters, counts, add, history):
    add_letters, add_counts = string_to_letters_counts(sorted(add))
    new_letters = letters.copy()
    new_counts = counts.copy()
    new_history = history.copy()
    
    for letter in add_letters:
        if letter == ' ':
            continue
        
        if letter in new_letters:
            new_counts[new_letters.index(letter)] += add_counts[add_letters.index(letter)]
        else:
            new_letters.append(letter)
            new_counts.append(add_counts[add_letters.index(letter)])
    
    new_history = update_history(sorted(new_letters), new_history)

    return new_letters, new_counts, new_history

def delete(letters, counts, delete, history):
    delete_letters, delete_counts = string_to_letters_counts(sorted(delete))
    new_letters = letters.copy()
    new_counts = counts.copy()
    new_history = history.copy()
    
    for letter in delete_letters:
        if letter == ' ':
            continue
        
        if letter in new_letters:
            new_counts[new_letters.index(letter)] -= delete_counts[delete_letters.index(letter)]
        
    for letter in new_letters:
        if new_counts[new_letters.index(letter)] <= 0:
            new_counts.remove(new_counts[new_letters.index(letter)])
            new_letters.remove(letter)
    
    new_history = update_history(sorted(new_letters), new_history)

    return new_letters, new_counts, new_history

def report(history, num):
    return ''.join(history[num])

def parse(input: str):
    lines = [line for line in input.split()]
    commands = {}
    
    i = 0
    for line in lines:
        command = line.split()[0]
        detail = line.split()[1]
        
        if command == 'RESET':
            commands[i] = (reset, detail)
        elif command == 'ADD':
            commands[i] = (add, detail)
        elif command == 'DELETE':
            commands[i] = (delete, detail)
        else:
            commands[i] = (report, detail)
        
        
    return commands
    


def main(input: str):
    commands = parse(input)
    pointer = 0
    
    letters, counts, history = reset(commands[pointer])
    pointer += 1
    while pointer <= max(commands.keys()):
        if commands[pointer][0] not in (reset, report):
            letters, counts, history = commands[pointer][0](letters, counts, commands[pointer][1], history)
        elif commands[pointer][0] == report:
            print(report(history, commands[pointer][1]))
        else:
            letters, counts, history = reset(commands[1])


main('''
    RESET abracadabracabob
    REPORT 3
    REPORT 5
    ADD BATH
    DELETE boa
    REPORT 5
    DELETE drr
    REPORT 5
    RESET American Computer Science League
    ADD Computer
    DELETE Computer
    DELETE COMPUTER
    REPORT 10''')