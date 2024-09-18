def pdn_transformation(n, p, d):
    temp_number = str(n)
    target_digit = temp_number[-p]
    if int(target_digit) > 4:
        new_target_digit = str(abs(int(target_digit) - d))[0]
    elif int(target_digit) < 5:
        new_target_digit = str(int(target_digit) + d)[-1]
        
    1827354178623
    1827354168623
        
    additional_string = new_target_digit + (p-1)*'0'
    return int(temp_number[:-p] + additional_string)

print(pdn_transformation(124987, 2, 3))
print(pdn_transformation(540670, 3, 9))
print(pdn_transformation(7145042, 2, 8))
print(pdn_transformation(124987, 2, 523))
print(pdn_transformation(4386709, 1, 2))
