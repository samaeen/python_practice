import serial

ser=serial.Serial('COM3',9600)
while (1==1):
        data=ser.readline()
        dataU=str(data[0:3])
        print (dataU)
        if dataU==str("b'694'"):
                print('ChorDhukse')
