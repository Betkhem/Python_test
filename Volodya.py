from random import randint
from tkinter import *
from tkinter import scrolledtext

def ButClick():
    try:
        MinNum = int(txt1.get())
        MaxNum = int(txt2.get())
        Num = int(txt3.get())
    except ValueError:
        messagebox.showerror('ValueEror!!','Eror! Invalid numbers')
    else:
        Nums = ''
        if MinNum <=MaxNum:
            i = 0
            while i < Num:
                numOne = randint(MinNum,MaxNum)
                Nums = Nums + ':' + str(numOne)
                i+=1
            scr.insert(INSERT,str(Nums) + '\n')
        else:
            messagebox.showerror('ValueEror!!', 'Eror! Invalid numbers')
    pass

root = Tk()
root.title('Random.org')

lb1 = Label(root, text = 'Min number')
lb1.grid(
    row = 0,
    column = 0,
    pady = 10,
    padx = 10)
txt1 = Entry(root, width = 30)
txt1.grid(
    row=0,
    column=1,
    pady=10,
    padx=10)
lb2 = Label(root, text = 'Max number')
lb2.grid(
    row = 1,
    column = 0,
    pady = 10,
    padx = 10)
txt2 = Entry(root, width = 30)
txt2.grid(
    row=1,
    column=1,
    pady=10,
    padx=10)
lb3 = Label(root, text = 'number')
lb3.grid(
    row = 2,
    column = 0,
    pady = 10,
    padx = 10)
txt3 = Entry(root, width = 30)
txt3.grid(
    row=2,
    column=1,
    pady=10,
    padx=10)
but = Button(root,width=15,height=2,text='OK', command=ButClick)
but.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=10,
    padx=10)
scr = scrolledtext.ScrolledText(root,height = 10)
scr.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=10,
    padx=10)
root.mainloop()
