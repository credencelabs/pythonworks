import mysql.connector
import socket
import sys
from datetime import datetime
now = datetime.now() # current date and time

today = now.strftime("%d-%b-%Y, %H:%M:%S")
#today = now.strftime("%H:%M:%S")
TCP_IP = '192.168.4.3'
TCP_PORT = 80

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = (TCP_IP, TCP_PORT)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

def func():
    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
        try:
            print >>sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and send it to MySQL Database test
            #while True:
            data = connection.recv(30).decode("ASCII")
            print >>sys.stderr, 'received "%s"' % data
            connection.close()
            print >>sys.stderr, 'connection closed'
            connection = mysql.connector.connect(host='localhost', user='', passwd='', db='test')
            cursor = connection.cursor()
            SQLInsert1 = "INSERT INTO android VALUES (%s, %s)"
            sqldata1=repr(data)
            print("Here it is:"+str(sqldata1))
            sqldata2 = sqldata1.replace("u'","")
            #sqldata3 = sqldata2.replace("\r'","\n")
            sqldata3 = sqldata2.replace("'"," ")
            #val=(str(sqldata3+today),"GOOD")
            val=(str(sqldata3),str(today))
            cursor.execute(SQLInsert1,val)
            connection.commit()
            print(cursor.rowcount, "record inserted")
            connection.close()
            break
        finally:
            # Clean up the connection
            connection.close()
func()
