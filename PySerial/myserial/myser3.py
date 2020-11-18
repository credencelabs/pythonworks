'''
Created on Oct 29, 2020

@author: Sundar
'''
import serial
import time
serialPort = serial.Serial(port = "COM3", baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialString = "" #Used to hold data coming over UART

def getSerialData():    
    while(1):
        # Wait until there is data waiting in the serial buffer
        if(serialPort.in_waiting > 0):    
            # Read data out of the buffer until a carraige return / new line is found
            serialString = serialPort.readline()
    
            # Print the contents of the serial data
            print(serialString.decode('Ascii'))

def sendSerialData():
    # Send data to device
    # The b at the beginning is used to indicate bytes!
    serialPort.write(b"1\r\n")
    #while(1):
     #   serialPort.write(b"1\r\n")
if __name__ == '__main__':
    sendSerialData()