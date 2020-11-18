import tkinter as tk
import datetime
from tkinter import *

x=0
master = tk.Tk()
master.title("TIMER")

Label(master, text=" ").grid(row=1)
#Label(master, text="CELL ANALYSER", foreground="red", font="Garamond").grid(row=x+0, column=3)
master.geometry('200x200')
#master.resizable(0,0)

seconds=0
minutes=0
hours=4
mins=str(minutes)
secs=str(seconds)
hrs=str(hours)


def go():
   s=e1.get()
   num=int(s)


def setValues():
   import time
   mydb=mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="agv@123",
      database="agv"
      )
   mycursor=mydb.cursor()
   sql="INSERT INTO LUNCH_RECORD (NAME, DATE) VALUES (%s, %s)"
   
   #disabling the textfields
   time2=time.strftime('%a %d %B %Y')
   date=str(time2)
   fout=open(date+'.txt','w')
   #Writing strings captured via textfields to the file
   emp1=str(e1.get())
   emp2=str(e2.get())
   emp3=str(e3.get())
   emp4=str(e4.get())
   emp5=str(e5.get())
   emp6=str(e6.get())
   emp7=str(e7.get())
   emp8=str(e8.get())
   emp9=str(e9.get())
   emp10=str(e10.get())
   emp11=str(e11.get())
   emp12=str(e12.get())
   emp13=str(e13.get())
   emp14=str(e14.get())
   emp15=str(e15.get())
   emp16=str(e16.get())
   emp17=str(e17.get())
   emp18=str(e18.get())
   emp19=str(e19.get())

   if(len(emp1) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp1,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")
   
   if(len(emp2) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp2,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp3) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp3,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp4) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp4,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp5) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp5,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp6) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp6,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp7) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp7,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp8) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp8,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp9) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp9,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp10) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp10,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp11) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp11,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp12) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp12,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp13) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp13,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp14) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp14,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp15) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp15,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp16) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp16,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp17) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp17,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp18) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp18,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")

   if(len(emp19) == 0):
      print("EMPTY")
   else:
      print("NOT EMPTY")
      val=(emp19,date)
      mycursor.execute(sql,val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted")
   fout.write("Personnel who went for lunch:\n")
   fout.write("%s" % (e1.get()))
   fout.write("\n")
   fout.write("%s" % (e2.get()))
   fout.write("\n")
   fout.write("%s" % (e3.get()))
   fout.write("\n")
   fout.write("%s" % (e4.get()))
   fout.write("\n")
   fout.write("%s" % (e5.get()))
   fout.write("\n")
   fout.write("%s" % (e6.get()))
   fout.write("\n")
   fout.write("%s" % (e7.get()))
   fout.write("\n")
   fout.write("%s" % (e8.get()))
   fout.write("\n")
   fout.write("%s" % (e9.get()))
   fout.write("\n")
   fout.write("%s" % (e10.get()))
   fout.write("\n")
   fout.write("%s" % (e11.get()))
   fout.write("\n")
   fout.write("%s" % (e12.get()))
   fout.write("\n")
   fout.write("%s" % (e13.get()))
   fout.write("\n")
   fout.write("%s" % (e14.get()))
   fout.write("\n")
   fout.write("%s" % (e15.get()))
   fout.write("\n")
   fout.write("%s" % (e16.get()))
   fout.write("\n")
   fout.write("%s" % (e17.get()))
   fout.write("\n")
   fout.write("%s" % (e18.get()))
   fout.write("\n")
   fout.write("%s" % (e19.get()))
   fout.write("\n")   
   fout.close()    
   e1.bind()
   e1.config(state=DISABLED)
   e2.bind()
   e2.config(state=DISABLED)
   e3.bind()
   e3.config(state=DISABLED)
   e4.bind()
   e4.config(state=DISABLED)
   e5.bind()
   e5.config(state=DISABLED)
   e6.bind()
   e6.config(state=DISABLED)
   e7.bind()
   e7.config(state=DISABLED)
   e8.bind()
   e8.config(state=DISABLED)
   e9.bind()
   e9.config(state=DISABLED)
   e10.bind()
   e10.config(state=DISABLED)
   e11.bind()
   e11.config(state=DISABLED)
   e12.bind()
   e12.config(state=DISABLED)
   e13.bind()
   e13.config(state=DISABLED)
   e14.bind()
   e14.config(state=DISABLED)
   e15.bind()
   e15.config(state=DISABLED)
   e16.bind()
   e16.config(state=DISABLED)
   e17.bind()
   e17.config(state=DISABLED)
   e18.bind()
   e18.config(state=DISABLED)
   e19.bind()
   e19.config(state=DISABLED)  
   Start()
def stop():
   import time
   time2=time.strftime('%a %d %B %Y')
   date=str(time2)
   fout=open(date+'.txt','a')
   fout.write("\n")
   fout.write("TIME TAKEN - Minutes:"+str(59-minutes)+" Seconds:"+str(60-seconds))
   fout.write("\n")
   fout.write(time2)
   fout.close()
   master.destroy()
   
def Start():
    countdown(60,59,3)


def countdown(seconds, minutes, hours):    
    # change text in label
    import time    
    labelSeconds['text'] = seconds
    labelMinutes['text'] = minutes
    labelHours['text'] =   hours    
    if (seconds >= 0 and minutes >=0 ):
        #call count down again after 1000ms (1s)
        master.after(1000, countdown, seconds-1, minutes, hours)
    if seconds == 0:
        #count down minutes
        minutes = minutes - 1
        #print("M:" + str(minutes))        
        countdown(seconds+60,minutes,hours)
    if minutes == 0:
        #count down hours
        hours = hours - 1
        countdown(seconds+60,minutes+59,hours)
#Button(master, text='Go', command=go).grid(row=x+24, column=18, sticky=S, pady=4)
Button(master, text='Start', command=setValues).grid(row=x+1, column=5, sticky=S, pady=4)
Button(master, text='Stop', command=stop).grid(row=x+1, column=26, sticky=S, pady=4)

ct=tk.Label(master, text="Charging Time:",font=("Verdana","8","bold"))
labelHeading = tk.Label(master, text="Time remaining", font=("Verdana","8","bold"))

labelHoursTitle=tk.Label(master, text="Hours", font=("Verdana","8","bold"))
labelHours = tk.Label(master, text=hrs, font=("Verdana","8","normal"))

labelMinutesTitle = tk.Label(master, text="Minutes", font=("Verdana","8","bold"))
labelMinutes = tk.Label(master, text=mins, font=("Verdana","8","normal"))

labelSecondsTitle = tk.Label(master, text="Seconds", font=("Verdana","8","bold"))
labelSeconds = tk.Label(master, text=secs, font=("Verdana","8","normal"))

#placement of objects
'''
labelHeading.grid(row=0, column=5)
ct.grid(row=2, column=3)
labelHoursTitle.grid(row=1, column=7)
labelHours.grid(row=2, column=7)

labelMinutesTitle.grid(row=1, column=18)
labelMinutes.grid(row=2,column=18)

labelSecondsTitle.grid(row=1,column=20)
labelSeconds.grid(row=2,column=20)
'''
mainloop()

