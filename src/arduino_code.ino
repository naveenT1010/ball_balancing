#include<ros.h>
#include<Servo.h>
#include<PID_v1.h>
#include<geometry_msgs/Point.h>

ros::NodeHandle nh;

const int servoPinX = 9;
const int servoPinY = 10;

float Kp = 2.5;
float Ki = 0;
float Kd = 1.1;

geometry_msgs::Point setpoint, input, output, servoOutput;

PID myPIDX(&input.x, &output.x, &setpoint.x, Kp, Ki, Kd, DIRECT);
PID myPIDY(&input.y, &output.y, &setpoint.y, Kp, Ki, Kd, DIRECT);

Servo myServoX;
Servo myServoY;

void setup(){
	Serial.begin(9600);
	myServoX.attach(servoPinX);
	myServoY.attach(servoPinY);
}