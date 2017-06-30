

#include "Time.h"
#include <Servo.h>
//#include "Minds.h"

Servo myservo;
Servo motor;

void setup() {
  Serial.begin(9600);
  setTime(12,0,0,1,1,11);
  // put your setup code here, to run once:
  /*
  myservo.attach(5);
  myservo.write(90);
  motor.attach(4);
  motor.write(90);
  */
}

int count = 70;
void loop() {
  Serial.print("I am sending a message! : ");
  Serial.print(hour());
  printDigits(minute());
  printDigits(second());
  Serial.println();
  delay(5000);
  // put your main code here, to run repeatedly:
  //myservo.write(count);
  //count = count + 1;
  //delay(500);
  /*
 
  */
  //if (getPing(9) > 50000000)
  /*
  {
     motor.write(100);
    delay(1000);
     motor.write(100);
  delay(1000);
  motor.write(0);
  delay(500);
  motor.write(95);
  delay(1000);
  motor.write(80);
  delay(1500);
  }
  delay(3000);
  */
}

void printDigits (int digits){
  Serial.print(":");
 if(digits < 10)
    Serial.print("0");
  Serial.print(digits); 
}
