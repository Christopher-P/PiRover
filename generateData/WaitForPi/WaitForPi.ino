//This code is pretty much C++

//Servo should be a default library
//No need for any of the minds eye stuff
#include "Time.h"
#include <Servo.h>

//Holds our steering and speed values
int turn;
int speeed;

//Initializes our front wheels, back wheels, and the motor
Servo front;
Servo back;
Servo motor;

//This function is ran ONCE at the BEGINNING to setup our code
void setup(){
  //standard rate
  Serial.begin(9600);
  //clear the buffer incase a previous run left some data
  Serial.flush();
  
  //each pin grouping has a ground pin, a power source pin and a control pin
  //connect front wheels to pin grouping 7
  front.attach(7);
  //89 is straight ahead
  front.write(89);
  //connect back wheels to pin grouping 11
  back.attach(11);
  back.write(89);
  //connect motor to pin grouping 4
  motor.attach(4);
  motor.write(90);
  
  //initialize these values
  turn = 120;
  speeed = 85;
}

//array to hold the values that the pi will send to the arduino
int incoming[3] = {90,90,1};

void loop(){

  //tell pi it is ready
  Serial.write(1); 

  //while there is no data do nothing
  while(!Serial.available()){
    
  }

  //if we have the data ready store it in incoming
  if(Serial.available() >= 3){
   for(int i = 0; i < 3; i++){
    incoming[i] = Serial.read();
   } 
  }
  
  turn = incoming[0];
  speeed = incoming[1];

  //The amounts the pi sends should already be scaled for a max speed for forward and reverse
  //This is the final check to prevent the rover from going too fast
  if (speeed > 120){
   speeed = 85; 
  }
  if (speeed < 60){
   speeed = 85; 
  }

  //Turn the front wheels some amount
  front.write(turn);
  //Turn the back wheels the inverted amount
  //so the back wheels turn opposite to the front wheels (makes turning easier)
  back.write(180-turn);

  //Go forward some speed
  //In the ai code, this amount is fixed
  
  // These next few lines need to be edited between generating code and running the AI
  // since generating data requires nice smooth rover movement while the ai used a turn start stop method.
  /*********------------Manual Mode-------------*********/
  //motor.write(speeed);
  //delay(100);
  

  /**********-------------AI MODE----------------***************/
  motor.write(speeed);
  delay(1000);
  //I believe writing 89 will engage the brakes
  motor.write(89);
  delay(1000);
}
