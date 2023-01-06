from tkinter import *
from os.path import exists
import keyboard
import pyautogui as pc
import time

cache_exists = exists('cache.txt')

defaultkeys = ['f10', 'f9']

keys = list()

if cache_exists == True:
    cacheread = open('cache.txt', 'r')
    keys = cacheread.readlines(0)
    cacheread.close()

    for i in range(len(keys)):
        keys[i] = keys[i].rstrip('\n')

elif cache_exists == False:
    cachewrite = open('cache.txt', 'w')
    cachewrite.write(f'{defaultkeys[0]}\n{defaultkeys[1]}')
    keys = defaultkeys
    cachewrite.close()

main = Tk()
main.resizable(False, False)

def boxchecked():
    if cbtnvar.get() == 0:
        iinpt.config(state=DISABLED)
    else:
        iinpt.config(state=NORMAL)
    
def spam():
    rang = int(inpt2.get())
    if cbtnvar.get() == 1:
        brk = float(iinpt.get())
        for i in range(rang):
            pc.typewrite(f'{inpt.get()}\n')
            time.sleep(brk)
    else:
        for i in range(rang):
            pc.typewrite(f'{inpt.get()}\n')    

def wait():
    cacheread = open('cache.txt', 'r')
    keys = cacheread.readlines(0)
    cacheread.close()

    for i in range(len(keys)):
        keys[i] = keys[i].rstrip('\n')

    while (True):
        kbw = keyboard.read_key()
        if kbw == keys[0]:
            spam()
            break
        if kbw == keys[1]:
            exit()

def chgkeys():
    keyconfg = Tk()
    keyconfg.resizable(False, False)

    key1l = Label(keyconfg, text='SPAM KEY: ')
    key1 = Entry(keyconfg)
    key2l = Label(keyconfg, text='EXIT KEY: ')
    key2 = Entry(keyconfg)

    def applycmd():
        conclusion1 = ''
        conclusion1color = ''

        if key1.get() == '' or key2.get() == '':
            conclusion1 = 'INVALID'
            conclusion1color = '#ff0000'

        elif key1.get() == key2.get():
            conclusion1 = 'INVALID'
            conclusion1color = '#ff0000'
            
        else:            
            cachewrite1 = open('cache.txt', 'w')
            cachewrite1.write(f'{key1.get()}\n{key2.get()}')
            cachewrite1.close()

            conclusion1 = 'SUSSESS'
            conclusion1color = '#00ff00'

        state = Label(keyconfg, text=conclusion1, foreground=conclusion1color, padx=10, font='bold')

        state.grid(column=2, row=2)

        cacheread = open('cache.txt', 'r')
        keys = cacheread.readlines(0)
        cacheread.close()

        for i in range(len(keys)):
            keys[i] = keys[i].rstrip('\n')

        lab3 = Label(main, text=f'SPAM - {keys[0]}\nEXIT - {keys[1]}', pady=10, padx=10)
        lab3.grid(column=1, row=7)
        

    def closewin():
        keyconfg.destroy()

    closebtn = Button(keyconfg, text='CLOSE', command=closewin, padx=5)
    applybtn = Button(keyconfg, text='APPLY', command=applycmd, padx=5)

    key1l.grid(column=1, row=0)
    key1.grid(column=2, row=0)
    key2l.grid(column=1, row=1)
    key2.grid(column=2, row=1)
    closebtn.grid(column=3, row=0)
    applybtn.grid(column=3, row=1)

    keyconfg.mainloop()

def rescache():
    cachewrite2 = open('cache.txt', 'w')
    cachewrite2.write(f'{defaultkeys[0]}\n{defaultkeys[1]}')
    cachewrite2.close()

    cacheread = open('cache.txt', 'r')
    keys = cacheread.readlines(0)
    cacheread.close()

    for i in range(len(keys)):
        keys[i] = keys[i].rstrip('\n')

    lab3 = Label(main, text=f'SPAM - {keys[0]}\nEXIT - {keys[1]}', pady=10, padx=10)
    lab3.grid(column=1, row=7)

cbtnvar = IntVar()

lab1 = Label(main, text='ENTER THE SPAM:')
inpt = Entry(main)
lab2 = Label(main, text='ENTER THE RANGE OF SPAM:')
inpt2 = Entry(main)
cbtn = Checkbutton(main, text='ADD A BREAK', variable=cbtnvar, command=boxchecked)
iinpt = Entry(main, state=DISABLED)
btnrun = Button(main, text='RUN', command=wait, padx=10)
lab3 = Label(main, text=f'SPAM - {keys[0]}\nEXIT - {keys[1]}', pady=10, padx=10)
lab4 = Label(main, text='NOTE: IF THE SPAMS CRASHING TURN ON THE BREAK', padx=10)
changkeys = Button(main, text='CHANGE KEYS', command=chgkeys)
resetcache = Button(main, text='RESET KEYS', command=rescache)
btnexit = Button(main, text='EXIT', command=exit, padx=10)

lab1.grid(column=1, row=0)
inpt.grid(column=1, row=1)
lab2.grid(column=1, row=2)
inpt2.grid(column=1, row=3)
cbtn.grid(column=1, row=4)
iinpt.grid(column=1, row=5)
btnrun.grid(column=1, row=6)
lab3.grid(column=1, row=7)
lab4.grid(column=1, row=8)
changkeys.grid(column=1, row=9)
resetcache.grid(column=1, row=10)
btnexit.grid(column=1, row=11)

main.mainloop()
