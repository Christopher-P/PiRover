#This file uses spaces not tabs!
#This file can be run as is using "python GatherData.py"

#Serial is the library used to connect the arduino the pi
import serial
#Struct is for changing our data to something the arduino can used (sent via the serial port)
import struct
#CSV is Comma Seperated Values, it is a file format that seperates data with commas
#It is used to store our controller inputs along with the time the info was gathered
import csv

#Raspberry PI camera interface
import picamera
#System time
import time

#Used to generate random values to make output more readable (Not necessary)
#It is hard to see changes in the output when everyhting is outputed the same way
#This makes sure we can see each update as it is printed 
import random

#Used to run our data gathering on a seperate thread so we can control the rover
# at the same time (prevents choppy rover driving)
#Also used to run our controller on a seperate thread
from threading import Thread

#-------------------------CONTROLLER SPECFIC CODE---------------------------------------------#
#IF YOU DO NOT USE A STEAM CONTROLLER, THEN PUT OTHER CODE HERE TO GET INPUTS FROM IT
#This code was modified to allow us to get the inputs of our controller
#Original code: https://github.com/ynsta/steamcontroller

#Used to start the controller code (Steam controller needs new thread to prevent choppiness)
from Controller import initOther
#Used to get the last postion the stick was at (updated very quickly)
from Controller import getLastPos
#Used to get the last button pressed (pressing steam home button will stop the program)
from Controller import getLastPressed

#Experimentally found max stick postion
#Used to scale our input values from -1 to 1
MAX_STICK = 32767.0

#Used in converting our circular control pad to a square
def sgn(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

#The math is decently hard
#Research papaer: https://arxiv.org/ftp/arxiv/papers/1509/1509.06344.pdf
#Pages 1 - 6
#Takes in two x,y values on a circle and converts them to x,y coordinates on a square!
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

#Simple function to start a thread from
#Might be unnecessary if you can launch the thread directly from initOther(), Havent tried might be worth a shot!
def getData():
    initOther()

#Used to store data (picture, input pairs using time as a key)
#Launched as a seperate thread to prevent choppiness
def getPicture():    
    #Init Raspberry Pi camera
    camera = picamera.PiCamera()
    #I found that sports mode is the best picture taking method for a moving rover
    #could be tested more to find a better method, but it works
    camera.exposure_mode = 'sports'
    #The camera is actually upside down so we need to turn it right side up
    camera.rotation = 180
    
    #Also loop!!!
    while True:
        #The sleep time dictates how often we take a picture and gather input (Keep in mind there is sometime used to take the picture and save it)
        time.sleep(0.5)
        
        #If B is pressed then we are not in recording mode, if A is pressed then we are in record mode (More modes might be usefull, like a turn on auto drive or turn on manual drive!)
        #Having a pause recording mode is really helpful when something goes wrong (like when someone asks about your sick rover and you have to stop and explain it ;)  )
        if getLastPressed() == "A":
            #Get last controller input
            vals = getLastPos()
            
            #get the time in milliseconds (this time is used to link our inputs to our picture by storing the time in the "Outputs.csv" file and then marking the picture with that same time)
            #This is convient since we will never have mismatched input and picture since time is unique! (possible problems with edge cases)
            nowTime = str(int(time.time() * 1000))
            
            #vals[0] is our x Pos (in circle format), vals[1] is our y Pos (in circle format)
            #example format: -1024, 2401, 1498855986705
            fields = [vals[0], vals[1], nowTime]
            
            #output the data to a the Outputs.csv file located in data (if data and outputs does not exist create (or add some code to do it for you!)) 
            with open('data/Outputs', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
                    
            #captures the picture and saves it in data as nowTime.jpg
            camera.capture('data/%s.jpg' % nowTime)


#Setup serial connection
ardData = serial.Serial()

#9600 is a standard
#I dont know what happens when it is changed (you would also need to change the arduino rate aswell to sync)
ardData.baudrate = 9600

#If the python code generates an error like: No port found on /dev/ttyACM0 
#then switch to the other (it is either going to be 1 or 0)
#This happens when the python code crashes but the arduino is fine
'''ardData.port = "/dev/ttyACM1"'''
ardData.port = "/dev/ttyACM0"
ardData.open()

#Start getData thread (Launches code inside getData()  ) 
threadController = Thread(target=getData)
threadController.start()

#Start getPicture thread (Launches code inside getPicture() )
threadCamera = Thread(target=getPicture)
threadCamera.start()

print "Setup Finished!"

#Always loop
while 1:
    #Get last values
    vals = getLastPos()
    
    #Scale the joystick values to go from -1 to 1
    newVals = ( float(vals[0]) / MAX_STICK, float(vals[1]) / MAX_STICK)

    #Convert the scaled values to square based coordinate system
    newVals = circleToSquare(newVals[0],newVals[1])

    #prints a random value to keep us updated that our code has not crashed!
    print random.random()
    #prints the values that are about to be sent to the arduino in the correct arduino amounts
    #the arduino runs the servos off values from 0 to 179 with 90-ish being nuetral
    print int(newVals[0] * 89 + 90), int(newVals[1] * 30 + 90)
    
    #Old code
    #'''if (ardData.inWaiting() > 100):'''
    #ardData.flushInput()
    #print "flushed"
    
    #Send code to the arduino in binary format (the last value of 1 is not needed BUT the arduino is expecting three values so just keep in there until you want to optimize the system)
    ardData.write(struct.pack('>BBB', int(newVals[0] * 89 + 90), int(newVals[1] * 30 + 90), 1))
    
    #Succesful write is displayed
    print "After write"
    
    #Waits for the arduino to send back a completion bit
    while(ardData.read() == ""):
        print "Waiting"
    
    #just to not overload the arduino
    time.sleep(0.1)
    print "woot"



        
