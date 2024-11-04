def sort(input: dict):
    return {key: input[key] for key in sorted(input)}

def string_to_letters_counts(input: str, history: dict):
    letters = {}
    new_history = history.copy()
    
    for letter in input:
        if letter == ' ':
            continue
        
        if letter.upper() in letters.keys():
            letters[letter.upper()] += 1
        else:
            letters[letter.upper()] = 1
            letters = sort(letters)
            new_history = update_history(new_history, letters)
    
    return letters, new_history

def update_history(old_history, new_letters):
    new_history = old_history.copy()
    
    for i in range(0, len(new_letters)):
        try:
            if new_history[i][-1] != list(new_letters.keys())[i]:
                new_history[i].append(list(new_letters.keys())[i])
        except KeyError:
            new_history[i] = [list(new_letters.keys())[i]]

    return new_history

def reset(input: str):
    letters, history = string_to_letters_counts(input, {})
    return letters, history

def add(letters, add, history):
    add_letters, new_history = string_to_letters_counts(add, history)
    new_letters = letters.copy()
    
    for letter in add_letters:
        if letter == ' ':
            continue
        
        if letter in new_letters:
            new_letters[letter] += add_letters[letter]
        else:
            new_letters[letter] = 1
            new_letters = sort(new_letters)
            new_history = update_history(new_history, new_letters)

    return new_letters, new_history

def delete(letters, delete, history):
    delete_letters, new_history = string_to_letters_counts(delete, history)
    new_letters = letters.copy()
    
    for letter in delete_letters:
        if letter == ' ':
            continue
        
        if letter in new_letters:
            new_letters[letter] -= delete_letters[letter]
    
    new_dict = new_letters.copy()
    newer_history = new_history.copy()
    for letter in new_letters:
        if new_letters[letter] <= 0:
            new_dict.pop(letter)
            newer_history = update_history(newer_history, new_dict)
            
    new_letters = sort(new_dict)

    return new_letters, new_history

def report(history, num):
    return ''.join(history[int(num)-1])

def parse(input: str):
    lines = [line for line in input.split('\n')]
    commands = {}
    
    i = 0
    for line in lines:
        command = line.split(maxsplit=1)[0]
        detail = line.split(maxsplit=1)[1]
        # print(command, detail)
        
        if command == 'RESET':
            # print(detail)
            commands[i] = (reset, detail)
        elif command == 'ADD':
            commands[i] = (add, detail)
        elif command == 'DELETE':
            commands[i] = (delete, detail)
        else:
            commands[i] = (report, detail)
        
        i += 1
        
    return commands
    


def main(input: str):
    commands = parse(input)
    # print(commands)
    pointer = 0
    
    letters, history = reset(commands[pointer][1])
    # print(history)
    pointer += 1
    while pointer <= len(commands.keys())-1:
        if commands[pointer][0] not in (reset, report):
            letters, history = commands[pointer][0](letters, commands[pointer][1], history)
        elif commands[pointer][0] == report:
            print(report(history, commands[pointer][1]))
            # report(history, commands[pointer][1])
        else:
            # print(commands[1])
            letters, history = reset(commands[pointer][1])
        # print(commands[pointer][0], commands[pointer][1])
        
        pointer += 1


main(
'''RESET simple simon
REPORT 4
ADD simply said something slowly
REPORT 4
DELETE so say something
REPORT 4
RESET peter piper picked a peck of pickled
REPORT 7
DELETE pickled
DELETE sunflowers
ADD pickled
ADD sunflowers
REPORT 5'''
)