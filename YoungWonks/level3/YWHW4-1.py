def remove_double_consonants(string1: str, string2: str):
    old_char = ''
    
    removals = 0
    for i in range(0, len(string1)):
        # print(i - removals)
        if string1[i-removals] == old_char:
            # print(f'removing index {i} char {string1[i]}')
            string1 = string1[:i-removals] + string1[i-removals+1:]
            # print(f'new string1 is {string1}')
            removals += 1
            
        old_char = string1[i-removals]
    
    removals = 0
    for i in range(0, len(string2)):
        # print(i - removals)
        if string2[i-removals] == old_char:
            # print(f'removing index {i} char {string1[i]}')
            string2 = string2[:i-removals] + string2[i-removals+1:]
            # print(f'new string1 is {string1}')
            removals += 1
            
        old_char = string2[i-removals]
    
    return string1, string2


def remove_vowels(string1: str, string2: str):
    removals = 0
    for i in range(1, len(string1)):
        # print(i - removals)
        if string1[i-removals] in ('A', 'E', 'I', 'O', 'U'):
            # print(f'removing index {i} char {string1[i]}')
            string1 = string1[:i-removals] + string1[i-removals+1:]
            # print(f'new string1 is {string1}')
            removals += 1
    
    removals = 0
    for i in range(1, len(string2)):
        if string2[i-removals] in ('A', 'E', 'I', 'O', 'U'):
            string2 = string2[:i-removals] + string2[i-removals+1:]
            removals += 1
    
    return string1, string2
            
    
def lr_remove_like(short: str, long: str):
    new_short = []
    new_long = []
    for i in range(len(short)):
        if short[i] != long[i]:
            new_short.append(short[i])
            new_long.append(long[i])
    
    new_long.append(long[len(short):])
    
    return ''.join(new_short), ''.join(new_long)
        
    
    
def rl_remove_like(short: str, long: str):
    difference = len(long) - len(short)
    new_short = []
    new_long = [long[:difference]]
    for i in range(0, len(short)):
        if short[i] != long[i+difference]:
            new_short.append(short[i])
            new_long.append(long[i+difference])
    
    
    return ''.join(new_short), ''.join(new_long)


def main(input: str):
    
    string1, string2 = input.split()
    string1, string2 = remove_double_consonants(string1, string2)
    string1, string2 = remove_vowels(string1, string2)
    if len(string1) < len(string2):
        string1, string2 = lr_remove_like(string1, string2)
    else:
        string2, string1 = lr_remove_like(string2, string1)
        
    if len(string1) < len(string2):
        string1, string2 = rl_remove_like(string1, string2)
    else:
        string2, string1 = rl_remove_like(string2, string1)
    
    # for i in range(0, min(len(string1), len(string2))):
    #     if string1[i] == string2[i]:
    #         return main(string1, string2)
    
    # output
    if len(string1) > len(string2):
        return string2
    elif len(string1) < len(string2):
        return string1
    else:
        return sorted((string1, string2))[0]
    
    # return ''.join(string1), ''.join(string2)

print(main('MISSISSIPPI MISSOURI'))
print(main('CATHERINE KATHERYNE'))
print(main('CONSTITUTIONAL CONVENTIONAL'))
print(main('COMPARTMENTALIZATION SEMIAUTOBIOGRAPHICAL'))
print(main('PHYSICIAN PHARMACY'))