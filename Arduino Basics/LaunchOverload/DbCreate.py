import sqlite3

conn = sqlite3.connect('LaunchOverLoadDetection.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS BIWTALaunchDB(launchName TEXT,waterLevel TEXT,OtherSensor TEXT)")

def data_entry():
    
    c.execute("INSERT INTO BIWTALaunchDB VALUES(?,?,?,?)",())
    conn.commit()
    c.close()
    conn.close()
    
create_table()
#data_entry()
