import serial
import struct

import random
from threading import Thread
import time
from scCallbacks import initOther
from scCallbacks import getLastPos

def getData():
    initOther()

t = Thread(target=getData)
t.start()


ardData = serial.Serial()
ardData.baudrate = 9600
ardData.write_timeout = 0

'''ardData.port = "/dev/ttyACM1"'''
ardData.port = "/dev/ttyACM1"
ardData.open()



print "hello"
while 1:
    vals = getLastPos()
    

    newVals = ( float(vals[0]) / 32767.0, float(vals[1]) / 32767.0)

    print "Hello:"
    print random.random()
    print int(newVals[0] * 89 + 90), int(newVals[1] * 30 + 85)
    
    '''if (ardData.inWaiting() > 100):'''
    ardData.flushInput()
    print "flushed"
    
    ardData.write(struct.pack('>BBB', int(newVals[0] * 89 + 90), int(newVals[1] * 30 + 90),1))
    
    time.sleep(0.1)
    print "woot"



        
