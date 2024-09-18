def compare_strings(stringa, stringb):
    final = []
    done = False
    for i in range(0, len(stringa)):
        done = False
        for j in range(0, len(stringb)):
            if done:
                continue
            
            if stringa[i] == stringb[j]:
                final.append(stringa[i])
                stringb = stringb[j:]
                done = True
                
                
    return final

def main(input: str):
    final = []
    split_input = input.split()
    stringa = split_input[0]
    stringb = split_input[1]
    
    # Left to right (lr)
    lrab = compare_strings(stringa, stringb)
    lrba = compare_strings(stringb, stringa)
    
    # Right to left (rl)
    stringa = stringa[::-1]
    stringb = stringb[::-1]
    rlab = compare_strings(stringa, stringb)
    rlba = compare_strings(stringb, stringa)
    
    for letter in lrab:
        if ((letter in lrba) and
            (letter in rlab) and
            (letter in rlba)):
            if letter not in final:
                final.append(letter)
    
    if final:
        return "".join(sorted(final))
    else:
        return "NONE"

print(main('javaprogramming programinjava'))