import sqlite3

conn = sqlite3.connect('Library.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS bookList(bookName TEXT,row  TEXT, bookShelfNum TEXT,barCodeID  TEXT)")

def data_entry():
    c.execute("INSERT INTO bookList VALUES('SedraSmith','a','z','1')")
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()
