def main():
    which = input('Would you like to convert [F-C] or [C-F]? ')


    def fc(temp):
        mult = 5/9
        newtemp = temp-32
        return newtemp * mult


    def cf(temp):
        mult = 9/5
        newtemp = temp * mult
        return newtemp + 32


    if which.lower() == 'f-c':
        temp = float(input('What would you like to convert(F)? '))
        f2c = fc(temp)
        print(f'Your new temp is: {f2c}')
    elif which.lower() == 'c-f':
        temp = float(input('What would you like to convert(C)? '))
        c2f = cf(temp)
        print(f'Your new temp is: {c2f}')
