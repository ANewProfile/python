def add_digits(num, sum=0):
    if len(str(num)) > 1:
        return add_digits(int(str(num)[1:]), sum+int(str(num)[:1]))
    else:
        return sum + num

print(add_digits(12345))