from tkinter import *
import keyboard
import pyautogui as pc
import time

main = Tk()

def spam():
    rang = int(inpt2.get()) + 1
    if cbtnvar.get() == 1:
        brk = float(iinpt.get())
        for i in range(rang):
            pc.typewrite(f'{inpt.get()}\n')
            time.sleep(brk)
    else:
        for i in range(rang):
            pc.typewrite(f'{inpt.get()}\n')    

def wait():
    keyboard.wait('f10')
    spam()

cbtnvar = IntVar()

lab1 = Label(main, text='enter the spam:')
inpt = Entry(main)
lab2 = Label(main, text='enter the range of spam:')
inpt2 = Entry(main)
cbtn = Checkbutton(main, text='add a break', variable=cbtnvar)
iinpt = Entry(main)
btn = Button(main, text='spam', command=wait)
btn2 = Button(main, text='exit', command=exit)
lab3 = Label(main, text='note: to spam you need to press F10')
lab4 = Label(main, text='if your spams crashing turn the break on')

lab1.pack()
inpt.pack()
lab2.pack()
inpt2.pack()
cbtn.pack()
iinpt.pack()
btn.pack()
btn2.pack()
lab3.pack()

main.mainloop()
