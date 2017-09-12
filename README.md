# PiRover
(Please forgive my bad spelling!)
Code used to create a self-driving rover for Whitworth CS Honours

## Raspberry Pi
The raspberry pi has everything it needs to be able to run the current python scripts located on it.
If you need to reinstall all of the software and updates it will take a long time (~1 day), so be hesitant to do so.
Currently the raspberry pi has both 2.7 and 3.5 versions of python installed. I had trouble connecting over Whitworth University Wi-fi and even over dormitory Ethernet connections.
I bypassed this problem by connecting the Raspberry Pi to a spare Ethernet cable in the CS Labs. 

The Raspberry Pi outputs to HDMI and Whitworth University has very few HDMI compatible monitors. The monitors in Eric Johnston that support HDMI are the newer large monitors in the upstairs CS lecture room.
Some of the teaching computers also accept HDMI, but this may only output to the projector.


## Arduino
The Arduino serves as an in-between for our raspberry pi and our servos/motors. The servos could potentially be linked directly to the raspberry pi, but I am unsure if the pi could handle the draw.
Currently, the raspberry pi will run its code and then send information (speed and turn amounts) to the Arduino. The pi will then wait for a response from the Arduino to continue.
The Arduino, once data has been sent to it, will adjust the wheels and motor and start going. It will then send a bit back to the raspberry pi and then wait for another response.
This handoff system ensures that only one device will be driving and we can simulate the two different hardware devices to be on a "single thread".

The Arduino has two modes, one for manual drive and another for auto drive. Depending on which mode is chosen, the motor will do something slightly different. 
In auto drive mode, the motor is set to go for 1 second and then stop for 1 second. This is because the pi cannot run the CURRENT AI fast enough to have a continuous motor (the AI currently takes around ~1 second to run a single image through).

Please do not rapidly switch between forward and backwards as the motor will not behave as intended. It will not cause the motor to explode if done on accident, but repeatedly doing so could cause permanent damage.
Simple wait a second with the motor in neutral and proceed in the desired direction.

## Pi camera
This is the original raspberry pi camera (Raspberry PI 5MP). It works well enough to take decent photos while moving. The camera is mounted directly to the chassis of the rover.
This is done to prevent the shifting of the suspended frame to alter the rotation of the pictures taken (the frame tilts to its right side with the camera being the front).
It is mounted upside down to allow the cable to run upwards.
The cable is extremely long so the camera can be mounted to any location on the rover.


## Pi Power Supply
The power supply is currently mounted above the Raspberry Pi and connects to its power port via a USB to Micro USB cable. The power supply is "ZILU Smart Power Basic 4400mAh".
It has enough power to supply the raspberry pi and its peripherals. It does not have enough power to supply the Arduino’s servos/motors in addition to the Raspberry Pi.
This supply will last long enough to do a day’s work on the pi (more than 3 hours). 


## Motor Power Supply
The motor is powered separately from a battery pack under the raspberry pi. The supply bank can be charged using the battery chargers located in the supply box. I have not run into the issue of it running out of power, so it should last at least 1 hour.
There are additional battery packs in the supply box, but I doubt they will be required.


## Bread Board
The Arduino shield should look something like this: https://arduino-info.wikispaces.com/SensorShield#SSM
The pins in the red area can be broken into 3-pin groupings (vertically in the photo). Each 3-pin grouping has a G,V (+), and S.
G stands for Ground, V (+) stands for power source, S stands for source (control).

The bread board is used because the servos need to be powered separately (as the power draw from the raspberry pi to the Arduino is too much!). 
So, the servos are powered by a four pack of double batteries wired in series (which equates to 6 volts, which is enough for our needs).
Each servo/motor has 3 pin connections: ground, high (power source), and control. Instead of using the high source from the Arduino, we replace it with our battery pack (Note: the separated sides of the bread board are all connected along the long side).
So, for each servo/motor we plug the red wire into high (yes, all of them are connected to the same high alongside the breadboards channel). 
Each Arduino output pin's ground is connected to the same ground (adjacent to the high channel), which is also connected to the battery pack's low cable (Black), which is also connected to a dedicated Arduino grounding pin, with all of the servo/motor grounding wires connected as well(black).
Each servo/motor has a white control wire, this wire should be directly connected to the Arduino’s control pins. The wiring should be finished now! 


## Gathering Data
To gather data (by manually driving the rover) please see the readme under generateData!

