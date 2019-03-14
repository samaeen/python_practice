import sqlite3
#import serial

conn = sqlite3.connect('Library.db')
c = conn.cursor()

StudentID=input("Enter your ID")
c.execute("UPDATE Booklist SET StudentID=1303013 WHERE StudentID=1102130")

BookName=input("Enter the bookname: ")

#ser=serial.Serial('COM13',9600)


if (c.execute("SELECT * FROM Booklist WHERE BookName=?",(BookName,))):

    data = c.fetchall()
    #print(row)
    for row in data:
        BarcodeID=row[3]
    c.execute("UPDATE Booklist SET StudentID=1303013 WHERE StudentID=1102130")    

print(BarcodeID)
#while (1==1):
     #ser.write(BarcodeID.encode())   

c.close
conn.close()
