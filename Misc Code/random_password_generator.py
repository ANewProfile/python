import random

password = []
length = input('What length do you want your password? ')
real_length = int(length)
index = 1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',\
                  'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'\
                    , 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'\
                        , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@'\
                            , '#', '$', "%", '^', '&', '*', '(', ')'\
                            , '1', '2', '3', '4', '5', '6', '7', '8'\
                                , '9', '0', ' ', '-', '_', '=', '+'\
                                    , '[', '{', ']', '}', '|', ':'\
                                        , '"', "'", ';', '/', '?'\
                                            , '>', '.', ',', '<'\
                                                , '`', '~']


def make_password(len, password, i):
    if i <= len:
        l = random.choice(alphabet)
        password.append(l)
        make_password(len, password, i + 1)

    else:
        pass

    return ''.join(password)


real_password = make_password(real_length, password, index)
print(f'Your password is: {real_password}')
