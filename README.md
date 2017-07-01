# PiRover
(Please forgive my bad spelling!)
Code used to create a self-driving rover for Whitworth CS Honours

## Arduino
The arduino serves as an inbetween for our raspberry pi and our servos/motors. The servos could potentially be linked directly to the raspberry pi, but I am unsure if the pi could handle the draw.
Currently, the raspberry pi will run its code and then send information (speed and turn amounts) to the arduino. The pi will then wait for a response from the arduino to countinue.
The arduino, once data has been sent to it, will adjust the wheels and motor and start going. It will then send a bit back to the raspberry pi and then wait for another response.
This handoff system ensures that only one device will be driving and we can simulate the two different hardware devices to be on a "single thread".

The arduino has two modes, one for manual drive and another for auto drive. Depending on which mode is chosen, the motor will do something slightly different. 
In auto drive mode the motor is set to go for 1 second and then stop for 1 second. This is because the pi cannot run the CURRENT ai fast enough to have a continuous motor (the ai currently takes around ~1 second to run a single image through).

Please do not rapidally switch between forward and backwards as the motor will not behave as intended. It will not cause the motor to explode if done on acciddent, but repeatedly doing so could cause permanent damage.
Simple wait a second with the motor in nuetral and proceed in the desired direction.


## Bread Board
The arduino shield should look something like this: https://arduino-info.wikispaces.com/SensorShield#SSM
The pins in the red area can be broken into 3-pin groupings (vertically in the photo). Each 3-pin grouping has a G,V (+), and S.
G stands for Ground, V (+) stands for power source, S stands for source (control).

The bread board is used because the servos need to be powered seperatly (as the power draw from the raspberry pi to the arduino is too much!). 
So the servoes are powered by a four pack of double batteries wired in series (which equates to 6 volts, which is enough for our needs).
Each servo/motor has 3 pin connections: ground, high (power source), and control. Instead of using the high source from the arduino, we replace it with our battery pack (Note: the seperated sides of the bread board are all connected along the long side).
So for each servo/motor we plug the red wire into high (yes, all of them are connected to the same high alongside the breadboards channel). 
Each arduino output pin's ground is connected to the same ground (adjacent to the high channel), which is also connected to the battery pack's low cable (Black), which is also connected to a dedicated arduino grounding pin, which all of the servo/motor grounding wires (black).
Each servo/motor has a white control wire, this wire should be directly connected to the arduino's control pins. The wiring should be finished now! 


## Gathering Data
To gather data (by manually driving the rover)

This file holds the code needed to generate the data for the training algorithms
I am unsure about whether I need the file "scCallbacks" anymore, but I will keep it as a backup
