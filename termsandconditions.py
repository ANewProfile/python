import time
import webbrowser
import os

input('Would you like to see the terms and conditions? ')
webbrowser.open_new_tab('file:///'+os.getcwd()+'/'+'termsandconditions.html')
t1 = time.time()

def two():
    trust = input('Do you agree to the terms and conditions([y]es or [n]o)? ')
    while True:
        try:
            if trust.lower() == 'n':
                print('SERIOUSLY BRO!!!???')
                return
            elif trust.lower() == 'y':
                    if time.time() - t1 > 600:
                         done = True
                    else:
                        done = False

                    if done is True:
                        print(
                            'Wow. I think I\'ve met the most trustworthy\
 person on the internet.')
                        return
                    else:
                        print('You lied!!!!!!!')
                        return
                        
        except Exception as e:
            print(e)

two()