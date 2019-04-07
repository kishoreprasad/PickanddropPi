 import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
pwm=GPIO.PWM(40, 50)
pwm1=GPIO.PWM(11, 50)
pwm2=GPIO.PWM(13, 30)
pwm3=GPIO.PWM(15, 50)
pwm.start(0)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(40, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(40, False)
    pwm.ChangeDutyCycle(0)
def SetAngle1(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm1.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm1.ChangeDutyCycle(0)
def SetAngle2(angle):
    duty = angle / 18 + 2
    GPIO.output(13, True)
    pwm2.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(13, False)
    pwm2.ChangeDutyCycle(0)
def SetAngle3(angle):
    duty = angle / 18 + 2
    GPIO.output(15, True)
    pwm3.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(15, False)
    pwm3.ChangeDutyCycle(0)
    
SetAngle2(25)
SetAngle1(10)
SetAngle(60)
SetAngle2(200)
SetAngle3(50)
SetAngle2(25)
SetAngle(0)
SetAngle2(200)
SetAngle3(20)
pwm.stop()
pwm1.stop()
pwm2.stop()
pwm3.stop()
GPIO.cleanup()
