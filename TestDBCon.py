import mysql.connector
from datetime import datetime
now = datetime.now() # current date and time

today = now.strftime("%d/%m/%y, %H:%M:%S")
def func():
    connection = mysql.connector.connect(host='localhost', user='', passwd='', db='test')
    cursor = connection.cursor()            
    SQLCommand = ("SELECT * FROM android_data")
    SQLInsert1 = "INSERT INTO android_event VALUES (%s, %s)"
    #SQLInsert2 = "INSERT INTO android_data VALUES (\"LML ON\")"
    #cursor.execute(SQLCommand)
    val=("L5 ON", str(today))
    #gul=("LML ON")
    cursor.execute(SQLInsert1,val)
    #cursor.execute(SQLInsert2)
    connection.commit()
    print(cursor.rowcount, "record inserted")
    #results = cursor.fetchall()            
    #rows=len(results)
    #print(results)

func()
    
