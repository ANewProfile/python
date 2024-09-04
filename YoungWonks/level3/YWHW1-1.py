def binary_to(num, base):
    if base == 2:
        return num
    elif base == 8:
        final = []
        triples_list = []
        divisible_3 = ''
        divisible_3 = str(num).lstrip('0')
        if len(divisible_3) % 3 == 2:
            divisible_3 = '0' + divisible_3
        elif len(divisible_3) % 3 == 1:
            divisible_3 = '00' + divisible_3
        
        triples_list = [divisible_3[i:i+3] for i in range(0, len(divisible_3), 3)]
        for triplet in triples_list:
            final.append(str(binary_to(int(triplet.lstrip('0')), 10)))
            
            
        return int("".join(final))
    elif base == 10:
        final = 0
        num_len = len(str(num))
        for i in range (1, num_len + 1):
            final += int(str(num)[-i]) * 2**(i-1)
            
        return final
    elif base == 16:
        final = []
        quadruples_list = []
        divisible_4 = ''
        
        divisible_4 = str(num).lstrip('0')
        if len(divisible_4) % 4 == 3:
            divisible_4 = '0' + divisible_4
        elif len(divisible_4) % 4 == 2:
            divisible_4 = '00' + divisible_4
        elif len(divisible_4) % 4 == 1:
            divisible_4 = '000' + divisible_4
        
        quadruples_list = [divisible_4[i:i+4] for i in range(0, len(divisible_4), 4)]
        for quadruplet in quadruples_list:
            new_num = binary_to(int(quadruplet), 10)
            hexadecimal_chars = '0123456789ABCDEF'
            final.append(str(hexadecimal_chars[new_num-1]))
            
            
        return "".join(final)

def to_binary(num, base):
    if base == 2:
        return num
    elif base == 10:
        return bin(num)
    elif base == 8:
        final = []
        for digit in str(num):
            binary = to_binary(digit, 10)
            if len(binary) == 1:
                new_binary = "00"+binary
            elif len(binary) == 2:
                new_binary = "0"+binary
            else:
                new_binary = binary
            final.append(new_binary)
            
        return int("".join(final))
    elif base == 16:
        final = []
        for digit in str(num):
            if digit in ('A', 'B', 'C', 'D', 'E', 'F'):
                new_digit = ('A', 'B', 'C', 'D', 'E', 'F').index(digit) + 10
            else:
                new_digit = digit
            binary = to_binary(new_digit, 10)
            if len(binary) == 1:
                new_binary = "000"+binary
            elif len(binary) == 2:
                new_binary = "00"+binary
            elif len(binary) == 3:
                new_binary = "0" + binary
            else:
                new_binary = binary
            final.append(new_binary)
            
        return int("".join(final))

def convert_bases(num, orig_base, target_base):
    if type(num) != int or type(orig_base) != int or type(target_base) != int:
        raise Exception("All parameters for the function must be integers!")
    if orig_base not in (2, 8, 10, 16) or target_base not in (2, 8, 10, 16):
        raise Exception("Bases must be either 2, 8, 10, or 16!")

    if orig_base == target_base:
        return num


    if target_base == 2:
        return to_binary(num, orig_base)
    elif target_base == 10:
        return binary_to(to_binary(num, orig_base), 10)
    elif target_base == 8:
        return binary_to(to_binary(num, orig_base), 8)
    elif target_base == 16:
        return binary_to(to_binary(num, orig_base), 16)

