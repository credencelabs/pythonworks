import Tkinter as tk
from Tkinter import *
import mysql.connector
import sys
from datetime import datetime
now = datetime.now() # current date and time

today = now.strftime("%d-%b-%Y")
#today = now.strftime("%d-%b-%Y, %H:%M:%S")
#today = now.strftime("%H:%M:%S")
main=tk.Tk()
main.geometry('250x100')
main.resizable(0,0)
main.title("DAILY LOG")


l1 = tk.Label(main, text="Name")
l1.grid(row=1, column=1)

e1=Entry(main)
e1.grid(row=1, column=2)

l2 = tk.Label(main, text="Date")
l2.grid(row=2, column=1)

e2=Entry(main)
e2.grid(row=2, column=2)

l3 = tk.Label(main, text="Work")
l3.grid(row=3, column=1)

e3=Entry(main)
e3.grid(row=3, column=2)

def setRecord():
    s1 = e1.get()
    print(s1)
    s2 = e2.get()
    print(s2)
    s3 = e3.get()
    print(s3)
    if(str(s2) == "TODAY"):
        DATE = str(today)
    else:
        DATE = str(s2)
    connection = mysql.connector.connect(host='localhost', user='', passwd='', db='test')
    cursor = connection.cursor()
    SQLInsert1 = "INSERT INTO tasks VALUES (%s, %s, %s)"
    val=(str(s1),str(DATE),str(s3))
    cursor.execute(SQLInsert1,val)
    connection.commit()
    print(cursor.rowcount, "record inserted")
    connection.close()

def exitWindow():
    main.destroy()


b1 = tk.Button(main,text="Record",command=setRecord)
b1.grid(row=4,column=2)

b2 = tk.Button(main,text="Exit",command=exitWindow)
b2.grid(row=4,column=3)

main.mainloop()
