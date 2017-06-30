import serial
import struct
import csv

import picamera
import time

import random
from threading import Thread
import time
from Controller import initOther
from Controller import getLastPos
from Controller import getLastPressed

MAX_STICK = 32767.0

def sgn(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

def circleToSquare(u,v):
    newU = u**2
    newV = v**2
    
    if (u == 0 or v == 0):
        return ((u,v))

    new2 = (newU + newV)**0.5/(sgn(u) * u + sgn(v) * v)**0.5
    
    if (newU >= newV):
        return ((sgn(u) * new2, sgn(u) * v / u * new2))
    else:
        return ((sgn(v) * u / v * new2, sgn(v) * new2))

    return (x,y)

    
def getData():
    initOther()

def getPicture():    
    camera = picamera.PiCamera()
    camera.exposure_mode = 'sports'
    camera.rotation = 180
    
    while True:
        time.sleep(0.5)
        if getLastPressed() == "A":
            vals = getLastPos()
            nowTime = str(int(time.time() * 1000))
            fields = [vals[0], vals[1], nowTime]
            with open('data/Outputs', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
            camera.capture('data/%s.jpg' % nowTime)



ardData = serial.Serial()
ardData.baudrate = 9600
#ardData.write_timeout = 0

'''ardData.port = "/dev/ttyACM1"'''
ardData.port = "/dev/ttyACM0"
ardData.open()

threadController = Thread(target=getData)
threadController.start()

threadCamera = Thread(target=getPicture)
threadCamera.start()

print "hello"
while 1:
    vals = getLastPos()
    
    newVals = ( float(vals[0]) / MAX_STICK, float(vals[1]) / MAX_STICK)

    newVals = circleToSquare(newVals[0],newVals[1])

    print random.random()
    print int(newVals[0] * 89 + 90), int(newVals[1] * 30 + 85)
    
    #'''if (ardData.inWaiting() > 100):'''
    #ardData.flushInput()
    #print "flushed"
    
    ardData.write(struct.pack('>BBB', int(newVals[0] * 89 + 90), int(newVals[1] * 30 + 90), 1))
    print "After write"
    while(ardData.read() == ""):
        print "Waiting"
    time.sleep(0.1)
    print "woot"



        
