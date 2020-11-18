import sys
import serial
import time
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_rtu as modbus_rtu

import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import *

logger = modbus_tk.utils.create_logger("console")
#master = modbus_rtu.RtuMaster(serial.Serial(port="COM3", baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))

class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ports = ['COM%s' % (i + 1) for i in range(256)]
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                #s.close()
                result.append(port)
                self.dict={'Ports':result}
                #print("Result",result)
            except (OSError, serial.SerialException):
                pass

        #self.dict = {'Asia': ['Japan', 'China', 'Malaysia'],
        #             'Europe': ['Germany', 'France', 'Switzerland']}

        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)

        self.variable_a.trace('w', self.update_options)

        self.optionmenu_a = tk.OptionMenu(self, self.variable_a, *self.dict.keys())
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, '')

        self.variable_a.set('Select Port')

        self.optionmenu_a.pack()
        self.optionmenu_b.pack()
        self.pack()


    def update_options(self, *args):
        countries = self.dict[self.variable_a.get()]
        self.variable_b.set(countries[0])

        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')

        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: self.variable_b.set(nation))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("GoMBus")
    # Add a grid
    mainframe = Frame(root)
    mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)
        
    # Create a Tkinter variable
    tkvar = StringVar(root)

    app = App(root)
    app.mainloop()
