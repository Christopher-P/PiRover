import serial

arduinoSerialData = serial.Serial('/dev/ttyACM1', 9600)

arduinoSerialData.write('20');

