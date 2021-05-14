import random
from tkinter import *
root=Tk()
root.geometry("700x450")
l1=Label(root,text='',font=("times",200))

def roll():
    n=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(n)}{random.choice(n)}')
    l1.pack()



    
b1=Button(root,text="please roll..",command=roll)
b1.place(x=330,y=0)
root.mainloop()
