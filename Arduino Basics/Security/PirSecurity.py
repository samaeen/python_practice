import serial
import cv2
import numpy as np

cap=cv2.VideoCapture(0)

ser=serial.Serial('COM3',9600)
while (1==1):
        data=ser.readline()
        dataU=(data[0:4])
        #print (data[0:4])
        print('allIzwell')
        ret,frame=cap.read()
        cv2.imshow('frame',frame)
