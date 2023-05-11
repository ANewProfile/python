import asyncio
import webbrowser
import os

input('Would you like to see the terms and conditions? ')
webbrowser.open_new_tab('file:///'+os.getcwd()+'/'+'termsandconditions.html')


async def one(timer=15):
    while True:
        if timer > 0:
            await asyncio.sleep(1)
            timer -= 1
        else:
            return True


async def two(done):
    trust = input('Do you agree to the terms and conditions([y]es or [n]o)? ')
    while True:
        try:
            if trust.lower() == 'n':
                print('SERIOUSLY BRO!!!???')
                return
            elif trust.lower() == 'y':
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


async def main():
    task2 = asyncio.create_task(one())
    task = asyncio.create_task(two(task2))



asyncio.run(main())