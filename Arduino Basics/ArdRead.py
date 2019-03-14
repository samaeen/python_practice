import serial
import csv

ser=serial.Serial('COM7',9600)
while (1==1):
        data=ser.readline()
        print(data[0:4])

        


