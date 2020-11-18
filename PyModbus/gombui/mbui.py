import serial
import time
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_rtu as modbus_rtu

import tkinter
import tkinter.messagebox as messagebox
from tkinter import *

logger = modbus_tk.utils.create_logger("console")
PORT = 1
master = modbus_rtu.RtuMaster(serial.Serial(port="COM3", baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))

class EasyModbusGUI(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self)
        #master.title("EasyModbusPython Client")
        master.title("GoMBus")
        self.pack()
        self.createWidgets()
        
        
    def createWidgets(self):
        self.pack(fill=BOTH, expand=True)
                
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        #label Read operations
        readOperationsLabel = Label(self, text="Read Operations", font = 15)
        readOperationsLabel.config(font=15)
        readOperationsLabel.grid(row = 0, column = 0)
        
        #Button Read Coils
        self.readCoils = Button(self, text="Read Coils (FC1)", width=25)#=self.__ReadCoils)
        self.readCoils.grid(row = 4, column = 0, padx = 20, pady = 6, columnspan=2)
        
        #Button Read Discrete Inputs
        self.readDiscreteInputs = Button(self, text="Read Discrete Inputs (FC2)", width=25)#=self.__ReadDiscreteInputs)
        self.readDiscreteInputs.grid(row = 5, column = 0, padx = 20, pady = 6, columnspan=2)
        
        #Button Read Holding Registers
        self.readHoldingRegisters = Button(self, text="Read Holding Registers (FC3)", width=25, command=self.__ReadHoldingRegisters)
        self.readHoldingRegisters.grid(row = 6, column = 0, padx = 20, pady = 6, columnspan=2)
 
        #Button Read Input Registers
        self.readInputRegisters = Button(self, text="Read Input Registers (FC4)", width=25)#=self.__ReadInputRegisters)
        self.readInputRegisters.grid(row = 7, column = 0, padx = 20, pady = 6, columnspan=2)       
        
        #label for COM Ports
        label = Label(self, text="COM Port:")
        label.grid(row = 2, column = 0, sticky=W)
        
        #Entry for COM Ports
        self.comPortEntry = Entry(self, width=15)
        self.comPortEntry.insert(END, "COM3")
        self.comPortEntry.grid(row = 3, column = 0, sticky=W)


        #label for Display Starting Address
        labelStartingAddress = Label(self, text="Starting Address:")
        labelStartingAddress.grid(row = 4, column = 3, sticky=W)
        
        #Text Field for starting Address
        self.startingAddress = Entry(self, width=10)
        self.startingAddress.insert(END, "1")
        self.startingAddress.grid(row = 4, column = 4, sticky=W)

        #label for Display Number of values
        labelStartingAddress = Label(self, text="Number of values:")
        labelStartingAddress.grid(row = 5, column = 3, sticky=W)
        
        #Text Field for number of Values
        self.quantity = Entry(self, width=10)
        self.quantity.insert(END, "1")
        self.quantity.grid(row = 5, column = 4, sticky=W)

        #Button for Controlling LED(Digital Output)
        self.btn = Button(self, text="ON", command=self.__SwitchOn)
        self.btn.grid(row = 7, column = 2, sticky=W)
        
        #Button for Controlling LED(Digital Output)
        self.btn = Button(self, text="OFF",command=self.__SwitchOff)
        self.btn.grid(row = 7, column = 4, sticky=W)
        
        #label for Response from server
        labelResponse = Label(self, text="Communication with Slave - Request & Response")
        labelResponse.grid(row = 2, column = 5, sticky=W, padx = 10)        
    
        #Text Field for response from server
        self.response = StringVar
        self.responseTextField = Text(self,  width=35, height = 10)
        scroll = Scrollbar(self)#=self.responseTextField.yview)
        self.responseTextField.configure(yscrollcommand=scroll.set)
        self.responseTextField.insert(END, "")
        self.responseTextField.grid(row = 2, column = 5, rowspan=8, padx = 10) 
        scroll.grid(row = 3, column = 6, rowspan=5, sticky=N+S+E)
        
        #Empty row between Read and Write operations
    
    def __SwitchOn(self):
        try:
            #Connect to the slave
            #master = modbus_rtu.RtuMaster(serial.Serial(port="COM3", baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
            #master.set_timeout(5.0)
            #master.set_verbose(True)
            self.responseTextField.insert(END,"ON\n")
            time.sleep(1)
            master.execute(1, cst.WRITE_SINGLE_REGISTER, 15, output_value=1)
            #self.responseTextField.insert(END, master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 6))
            #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 4))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 15, 0))
            
            #send some queries
            #logger.info(master.execute(1, cst.READ_COILS, 0, 10))
            #logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
            #logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
            #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 15, output_value=1))
            #logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
            #logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))
        
        except modbus_tk.modbus.ModbusError as exc:
            print("Error")
            #logger.error("%s- Code=%d", exc, exc.get_exception_code())
    
    def __SwitchOff(self):
        try:
            #Connect to the slave
            #master = modbus_rtu.RtuMaster(serial.Serial(port="COM3", baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
            #master.set_timeout(5.0)
            #master.set_verbose(True)
            self.responseTextField.insert(END,"OFF\n")
            time.sleep(1)
            master.execute(1, cst.WRITE_SINGLE_REGISTER, 15, output_value=0)
            #self.responseTextField.insert(END, master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 6))
            #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 4))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 15, 0))
            
            #send some queries
            #logger.info(master.execute(1, cst.READ_COILS, 0, 10))
            #logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
            #logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
            #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 15, output_value=0))
            #logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
            #logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))
        
        except modbus_tk.modbus.ModbusError as exc:
            print("Error")
            #logger.error("%s- Code=%d", exc, exc.get_exception_code())
    
    def __ReadHoldingRegisters(self):
        try:
            #Connect to the slave
            master = modbus_rtu.RtuMaster(serial.Serial(port="COM3", baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
            master.set_timeout(5.0)
            #master.set_verbose(True)
            self.responseTextField.insert(END,"Connected\n")
            time.sleep(5)
            self.responseTextField.insert(END, master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 6))
            #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 4))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 15, 0))
            
            #send some queries
            #logger.info(master.execute(1, cst.READ_COILS, 0, 10))
            #logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
            #logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
            #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 100, output_value=54))
            #logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
            #logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))
        
        except modbus_tk.modbus.ModbusError as exc:
            logger.error("%s- Code=%d", exc, exc.get_exception_code())
    def datatypeChanged(self,a,b,c):
        self.requestTextField.delete('1.0', END)
        if (self.variableDatatype.get()  == 'Coils (bool)'):
            self.registerValueToWrite.grid_remove()
            self.dropdownData.grid(row = 26, column = 1, sticky=W)
        else:
            self.registerValueToWrite.grid(row = 26, column = 1, sticky=W)
            self.dropdownData.grid_remove()
           
    def onReverse(self):
        self.name.set(self.name.get()[::-1])
root = Tk()
app = EasyModbusGUI(root)
app.mainloop()
