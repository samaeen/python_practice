import sqlite3
#import serial

#ser=serial.Serial('COM3',9600)

conn = sqlite3.connect('Library.db')
c = conn.cursor()

if c.execute("SELECT * FROM Booklist"):

    data = c.fetchall()
    #print(row)
    for column in data:
        print(column[3][0])
        #ser.write(value.encode())

c.close
conn.close()
