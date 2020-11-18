'''
Created on Oct 13, 2020

@author: Sundar
'''
import serial.tools.list_ports
print(list(serial.tools.list_ports.comports()))
#ser = serial.Serial('COM6')  # open serial port
'''
print(serial.__version__)
print(serial.__name__)
print(serial.__path__)
'''
print(serial.Serial())