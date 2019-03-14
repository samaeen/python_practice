import serial
ser=serial.Serial('COM7',9600)
while (1==1):
    value=input("enter somethin")
    ser.write(value.encode())



