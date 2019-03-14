import sqlite3
import serial

Roll=input("Enter Roll Number: ")
BookName=input("Enter the bookname: ")

ser=serial.Serial('COM8',9600)

conn = sqlite3.connect('Library.db')
c = conn.cursor()

if (c.execute("SELECT * FROM Booklist WHERE BookName=?",(BookName,))):

    data = c.fetchall()
    #print(row)
    for row in data:
        BarcodeID=row[3]
        

print(BarcodeID)
while (1==1):
     ser.write(BarcodeID.encode())   

c.close
conn.close()
