## GatherData
This code will generate pairs of (inputs,image) as data. The key (unique identifier) is the time since the epoch in milliseconds.
The data can then be fed into an AI to train it. It requires an additional file to interface with a controller. In our case it is the Controller.py file (which was designed for the Steam Controller).

## Controller
This file is setup to enable the use of a Steam Controller. It gives us what the last position of the joystick and whether a or b was the last button pressed.
If another controller is to be used, then those modifications need to be kept in mind.

## Arduino
The arduino code is located in the "WaitForPi" folder. The reason that the code is in its own folder is because it is required by Arduino (the file must be in a folder with the same name :/)!
It waits for the Raspberry Pi to send 3 values across port 9600 (in our case it is direction, speed, and a spare value).
It will run differently depending on whether it is in ai mode or manual mode.
Manual mode runs smoothly with turning and speed being updated as fast as possible.
AI mode runs in a start and stop fasion, this was needed because the raspberry pi was not able to run the ai fast enough to smoothly update the arduino.

Instead of just sending a notification bit to the pi, the channel can be used to send sensor data. 

To preserve the motors do not switch between going forward and going backward quickly.
It is best to return the stick to a nuetral position (so the brakes get enabled at servo=89), and then proceed to go in the opposite direction.

The arduino code (called a "sketch") MUST be in a file with its own name (i.e. "test.ino" must be in a file name "test").
