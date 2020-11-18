import sys as s
import tkinter as tk
import time
from tkinter import *

main=tk.Tk()
main.geometry('290x50')
main.resizable(0,0)
main.title("Gopran Industries")
fnt="Verdana"
pattern="bold"
size="8"

t=time.strftime("%d %B %Y")
l1=tk.Label(main, text="Today is:"+str(t),font=(fnt, size, pattern))
l1.grid(row=0, column=4)#date

def quit():                             # a custom callback function / handler
    print('Hello, I must be going...')  # kill windows and process
    s.exit(0)

#b=tk.Button(main, text="Quit",command=quit)
#b.grid(row=0, column=5)

b = Button(None, # but contains just an expression text='Hello event world',command=(lambda:print('Hello lambda world') or sys.exit()) 
              )
b.grid(row=0, column=5)
main.mainloop()
