import currency_converter
import fahrenheit_celsius
import len_converter
import sys

print('============== Welcome to the Value Converter! ==============')



while True:
    which = input(
        'Which conversion would you like to choose:\n1. Convert temperature\n\
2. Convert currency\n3. Convert lengths\n4. Exit\n')
    try:
        if which == '1':
            fahrenheit_celsius.main()
        elif which == '2':
            currency_converter.main()
        elif which == '3':
            len_converter.main()
        elif which == '4':
            exit()
        else:
            print('Invalid. Enter "1", "2", "3", or "4".')
            continue
    except Exception as e:
        if e == SystemExit:
            break
        elif e == ValueError:
            continue
        else:
            print(e)
