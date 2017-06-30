
#include "Time.h"
#include <Servo.h>

int n;
int s;

Servo front;
Servo back;
Servo motor;

void setup(){
  Serial.begin(9600);
  Serial.flush();
  front.attach(7);
  front.write(89);
  back.attach(11);
  back.write(89);
  motor.attach(4);
  motor.write(90);
  n = 120;
  s = 85;
}

int incoming[3] = {90,90,1};

void loop(){
  Serial.write(1); 
  while(!Serial.available()){
    
  }
  
  if(Serial.available() >= 3){
   for(int i = 0; i < 3; i++){
    incoming[i] = Serial.read();
    // Serial.println(incoming[i]);
   } 
  }
  
  n = incoming[0];
  s = incoming[1];
  
  if (s > 120){
   s = 85; 
  }
  if (s < 60){
   s = 85; 
  }
  front.write(n);
  back.write(180-n);
  /*
  digitalWrite(ledPin, HIGH);
  delay(n*100);
  digitalWrite(ledPin, LOW);
  delay(n*100);
  */
  motor.write(s);
  delay(1000);
  motor.write(89);
  delay(1000);
}
