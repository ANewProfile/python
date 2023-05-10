from threading import Thread
import webbrowser
import os
import time

input('Would you like to see the terms and conditions? ')

done = False

webbrowser.open_new_tab('file:///'+os.getcwd()+'/'+'termsandconditions.html')



def one(timer=300):
    while True:
        if timer > 0:
            time.sleep(1)
            timer -= 1
        else:
            return


def two():
    trust = input('Do you agree to the terms and conditions([y]es or [n]o)? ')
    while True:
        try:
            if trust.lower() == 'y':
                if done is False:
                    print('You lied!!!!!!!')
                    return
                else:
                    print('Wow. I think I\'ve met the most trustworthy person on the internet.')
                    return
            elif trust.lower() == 'n':
                print('SERIOUSLY BRO!!!???')
                return
            else:
                raise Exception('Not an answer')
        except Exception as e:
            print(e)



t1 = Thread(target=one)
t2 = Thread(target=two)

t1.start()
done = True
t2.start()