

#include "Time.h"
#include <Servo.h>
int n;
int s;
Servo myservo;
Servo motor;

void setup(){
  
  Serial.begin(9600);
  Serial.flush();
  myservo.attach(5);
  myservo.write(90);
  motor.attach(4);
  motor.write(90);
  n = 120;
  s = 85;
}

int incoming[3] = {90,90,90};

void loop(){
  Serial.println("---------");
  if(Serial.available() >= 3){
   for(int i = 0; i < 3; i++){
    incoming[i] = Serial.read();
    Serial.println(incoming[i]);
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
  myservo.write(n);
  /*
  digitalWrite(ledPin, HIGH);
  delay(n*100);
  digitalWrite(ledPin, LOW);
  delay(n*100);
  */
  motor.write(s);
  delay(100);
}
