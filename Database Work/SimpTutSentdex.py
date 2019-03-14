import sqlite3

conn = sqlite3.connect('Library.db')
c = conn.cursor()

def read_from_db():

    c.execute("SELECT * FROM Booklist WHERE BookName='SedraSmith'")
    data = c.fetchall()
    #print(data)
    for row in data:
        print(row[2])
    
read_from_db()
c.close
conn.close()


