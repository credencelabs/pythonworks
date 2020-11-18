import serial
import time
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_rtu as modbus_rtu

import tkinter
import tkinter.messagebox as messagebox
from tkinter import *

root = Tk()
root.title("GoMBus")

logger = modbus_tk.utils.create_logger("console")
#master = modbus_rtu.RtuMaster(serial.Serial(port="COM3", baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = StringVar(root)
def serial_ports():
    ports = ['COM%s' % (i + 1) for i in range(256)]
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            #s.close()
            result.append(port)
            #print("Result",result)
        except (OSError, serial.SerialException):
            pass
    return result

popupMenu = OptionMenu(mainframe, tkvar, serial_ports())
Label(mainframe, text="Select Port").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()
