def main():
    which = input('Would you like to convert feet-inches to meters-centimeters or meters-centimeters to fee-inches(FI-MC or MC-FI respectively)? ')

    if which.lower() == 'fi-mc':
        try:
            feet = float(input('How many feet? '))
            inches = float(input('How many inches? '))
        except Exception as e:
            print(e)

        total_inches = feet*12 + inches
        total_centimeters = total_inches * 2.54

        print(f'Your end result is approximately{total_centimeters} centimeters!')
    

    if which.lower() == 'mc-fi':
        try:
            meters = float(input('How many meters? '))
            centimeters = float(input('How many centimeters? '))
        except Exception as e:
            print(e)

        total_centimeters = meters*100 + centimeters
        total_inches = total_centimeters / 2.54

        print(
            f'Your end result is approximately {total_inches} inches!')
