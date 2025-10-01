#include <Servo.h>
Servo myservo;
#define IN1 D4
#define IN2 D3
#define ENA D1  

#define INB1 D6
#define INB2 D5
#define ENB D2  



volatile long encoderCount = 0;
int motorDirection = 1;  // 当前方向：1=正转，-1=反转



void setMotorDirection(int direction) {
  if (direction == 1) {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(INB1, HIGH);
    digitalWrite(INB2, LOW);
  } else if (direction == -1) {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(INB1, LOW);
    digitalWrite(INB2, HIGH);
  } else {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);  // 停止
    digitalWrite(INB1, LOW);
    digitalWrite(INB2, HIGH);
  }
}

void setup() {
  myservo.attach(D0);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(INB1, OUTPUT);
  pinMode(INB2, OUTPUT);
  pinMode(ENB, OUTPUT);

  myservo.write(90);
  analogWrite(ENA, 1024);  
  analogWrite(ENB, 1024);  
  setMotorDirection(motorDirection);  // 启动电机
  delay(2000);
  myservo.write(45);
  analogWrite(ENA, 512);  
  analogWrite(ENB, 512);  
  delay(1000);
  setMotorDirection(-1);
  myservo.write(135);
  analogWrite(ENA, 512);  
  analogWrite(ENB, 512);  
  delay(1100);

  myservo.write(90);
  analogWrite(ENA, 0);  // 设置初始速度
  analogWrite(ENB, 0);  // 设置初始速度
}

void loop() {

}