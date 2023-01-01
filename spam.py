from tkinter import *
import keyboard
import pyautogui as pc

main = Tk()

def spam():
    rang = int(inpt2.get()) + 1
    for i in range(rang):
        pc.typewrite(f'{inpt.get()}\n')

def wait():
    keyboard.wait('alt gr')
    spam()

lab1 = Label(main, text='enter the spam:')
inpt = Entry(main)
lab2 = Label(main, text='enter the range of spam:')
inpt2 = Entry(main)
btn = Button(main, text='spam', command=wait)
btn2 = Button(main, text='exit', command=exit)
lab3 = Label(main, text='note: to spam you need to press ALT GR')

lab1.pack()
inpt.pack()
lab2.pack()
inpt2.pack()
btn.pack()
btn2.pack()
lab3.pack()

main.mainloop()