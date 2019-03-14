import serial
import sqlite3

conn = sqlite3.connect('LaunchOverLoadDetection.db')
c = conn.cursor()
ser=serial.Serial('COM3',19200)


while (1==1):
        data=ser.readline()
        print (data[0:9])
        launchName='Pinak-10'
        waterLevel=str(data[0:9])
        OtherSensor='AllIzWell'
        c.execute("INSERT INTO BIWTALaunchDB VALUES(?,?,?)",(launchName,waterLevel,OtherSensor))
        conn.commit()

c.close()
conn.close()


