from tkinter import *
rootWindow = Tk()
rootWindow.title('Advance Equipments')
rootWindow.geometry("340x90+450+50")
rootWindow.resizable(0,0)
#rootWindow.overrideredirect(True)
#D:\Works\APPLICATION TESTS-STUDIES\IT\Python\File\dist\Test

def doAll():    
    f = open("sumofile.ini", "a")
    f.write("1,2,3")
    f.close()

    f = open("sumofile.txt", "a")
    f.write("1,2,3")
    f.close()

    f = open("sumofile.csv", "a")
    f.write("1,2,3")
    f.close()

    f = open("sumofile.doc", "a")
    f.write("1,2,3")
    f.close()

    f = open("sumofile.dat", "a")
    f.write("1,2,3")
    f.close()

    f = open("sumofile.pdf", "a")
    f.write("1,2,3")
    f.close()

    f = open("sumofile.h1", "a")
    f.write("1,2,3")
    f.close()

def exit():
    rootWindow.destroy()


btn_start = Button(rootWindow, text = 'Make Files', command = doAll)
btn_start.grid(sticky=EW, row = 4, column = 2)

btn_exit = Button(rootWindow, text = 'Exit', command = exit)
btn_exit.grid(sticky=EW, row = 4, column = 4)

rootWindow.iconbitmap('cap.ico')
rootWindow.mainloop()
