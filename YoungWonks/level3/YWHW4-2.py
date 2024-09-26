def calibrate(string1, string2):
    if len(string1) > len(string2):
        short = string2
        long = string1
        shorts = string2
        longs = string1
    else:
        short = string1
        long = string2
        shorts = string1
        longs = string2
    
    return short, long, shorts, longs

def lr_remove_like(short: str, long: str):
    new_short = []
    new_long = []
    for i in range(len(short)):
        if short[i] != long[i]:
            new_short.append(short[i])
            new_long.append(long[i])
    
    new_long.append(long[len(short):])
    
    return ''.join(new_short), ''.join(new_long)

def remove_barriers(string1, string2, short):
    # new_1 = string1
    # new_2 = string2
    new_string1 = string1 + ' '
    new_string2 = string2 + ' '
    for i in range(0, short):
        if new_string2[i+1] == new_string1[i] and new_string1[i] != ' ':
            new_string2 = new_string2[:i] + new_string2[i+1:]
            if len(new_string1) > len(new_string2):
                new_string2, new_string1 = lr_remove_like(new_string2, new_string1)
            else:
                new_string1, new_string2 = lr_remove_like(new_string1, new_string2)
        
        if new_string1[i+1] == new_string2[i] and new_string2[i] != ' ':
            new_string1 = new_string1[:i] + new_string1[i+1:]
            if len(new_string1) > len(new_string2):
                new_string2, new_string1 = lr_remove_like(new_string2, new_string1)
            else:
                new_string1, new_string2 = lr_remove_like(new_string1, new_string2)
    
    return new_string1.rstrip(' '), new_string2.rstrip(' ')


def main(input: str):
    string1, string2 = input.split()
    short, long, shorts, longs = calibrate(string1, string2)
    
    short, long = lr_remove_like(short, long)
    if shorts == string2:
        long, short = remove_barriers(long, short, len(short))
    elif longs == string2:
        short, long = remove_barriers(short, long, len(short))
    
    # if shorts == string1:
    #     if short == string1 and long == string2:
    #         return asf(short, long)
    # else:
    #     if short == string2 and long == string2:
    #         return asf(short, long)
    
    # return main(short, long)
    return short, long

print(main('ABCDEFT ABXCGBTZFP'))