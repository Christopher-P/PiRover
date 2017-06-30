from threading import Thread
import time
from scCallbacks import initOther
from scCallbacks import getLastPos

def getData():
    initOther()

t = Thread(target=getData)
t.start()
minX = 0
maxX = 0
minY = 0
maxY = 0

'''
calculated min/max = 32767
'''

print "hello"
while 1:
    vals = getLastPos()
    time.sleep(0.01)
    if vals[0] < minX:
        minX = vals[0]
    if vals[0] > maxX:
        maxX = vals[0]
    if vals[1] < minY:
        minY = vals[1]
    if vals[1] > maxY:
        maxY = vals[1]
    print "minX: " , minX, " .maxX: ", maxX, " .minY: " , minY, " .maxY: ", maxY
    
