def remove_double_consonants(string1: str, string2: str):
    old_char = ''
    for i in (0, len(string1)):
        if string1[i] == old_char:
            print(f'old string {string1}')
            string1 = string1[:i] + string1[i+2:]
            print(f'new string {string1}\n')
        old_char = string1[i]
    
    for i in (0, len(string2)):
        if string2[i] == old_char:
            print(f'old string {string2}')
            string2 = string2[:i] + string2[i+2:]
            print(f'new string {string2}\n')
        old_char = string2[i]

    return string1, string2

def remove_vowels(string1: str, string2: str):
    removals = 0
    for i in range(0, len(string1)):
        print(i - removals)
        if string1[i-removals] in ('A', 'E', 'I', 'O', 'U'):
            # print(f'removing index {i} char {string1[i]}')
            string1 = string1[:i-removals] + string1[i-removals+1:]
            print(f'new string1 is {string1}')
            removals += 1
    
    removals = 0
    for i in range(0, len(string2)):
        if string2[i-removals] in ('A', 'E', 'I', 'O', 'U'):
            string2 = string2[:i-removals] + string2[i-removals+1:]
            removals += 1
    
    return string1, string2
            
    
def lr_remove_like(string1: str, string2: str):
    if string2 > string1:
        for i in range(0, len(string1)):
            if string1[i] == string2[i]:
                string1 = string1[:i-1] + string1[i+1:]
                string2 = string2[:i-1] + string2[i+1:]
    else:
        for i in range(0, len(string2)):
            if string1[i] == string2[i]:
                string1 = string1[:i-1] + string1[i+1:]
                string2 = string2[:i-1] + string2[i+1:]
    
    return string1, string2
        
    
    
def rl_remove_like(string1: str, string2: str):
    if string2 > string1:
        for i in range(0, len(string1)):
            if string1[-i] == string2[-i]:
                string1 = string1[:-i-1] + string1[-i+1:]
                string2 = string2[:-i-1] + string2[-i+1:]
    else:
        for i in range(0, len(string2)):
            if string1[i] == string2[i]:
                string1 = string1[:-i-1] + string1[-i+1:]
                string2 = string2[:-i-1] + string2[-i+1:]
    
    return string1, string2


def main(input: str):
    
    string1, string2 = input.split()
    string1, string2 = remove_vowels(string1, string2)
    # string1, string2 = remove_double_consonants(string1, string2)
    # string1, string2 = lr_remove_like(string1, string2)
    # string1, string2 = rl_remove_like(string1, string2)
    
    # output
    output = string1, string2
    return output

print(main('MISSISSIPPI MISSOURI'))