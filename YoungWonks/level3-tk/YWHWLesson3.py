from tkinter import *
from time import sleep


class FrameSwitch:
    def __init__(self, frame1, frame2):
        self.frame1 = frame1
        self.frame2 = frame2
        self.switch1 = Button(frame1, text='Switch to Frame 2', command=self.switch12)
        self.switch2 = Button(frame2, text='Switch to Frame 1', command=self.switch21)
        
    def switch12(self):
        print('Switching...')
        # sleep(1)
        self.frame1.pack_forget()
        self.frame2.pack()
        print('Switched!')

    def switch21(self):
        print('Switching...')
        # sleep(1)
        self.frame2.pack_forget()
        self.frame1.pack()
        print('Switched!')


root = Tk()


frame1 = Frame(root)
label1 = Label(frame1, text='Label in Frame 1')

frame2 = Frame(root)
label2 = Label(frame2, text='Label in Frame 2')

frameswitch12 = FrameSwitch(frame1, frame2)

frame1.pack()
label1.pack()
frameswitch12.switch1.pack()
label2.pack()
frameswitch12.switch2.pack()


root.mainloop()
