def foobar(input: str):
    num = input[:-2]
    p = int(input[-1])
    new_num = []
    target_digit = num[-p]
    for i in range(0, len(num)-p):
        new_num.append(str(int(num[i]) + int(num[-p]))[-1])
        
    new_num.append(num[-p])
    for i in range(p-1, 1-1, -1):
        new_num.append(str(abs(int(num[-i]) - int(num[-p]))))
    
    return "".join(new_num)
