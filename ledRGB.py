#!/usr/bin/env python
# encoding: utf-8
 
import RPi.GPIO
import time
#定义GPIO引脚 
R,G,B=13,6,19

RPi.GPIO.setmode(RPi.GPIO.BCM)
 
RPi.GPIO.setup(R, RPi.GPIO.OUT)
RPi.GPIO.setup(G, RPi.GPIO.OUT)
RPi.GPIO.setup(B, RPi.GPIO.OUT)

pwmR = RPi.GPIO.PWM(R, 70)
pwmG = RPi.GPIO.PWM(G, 70)
pwmB = RPi.GPIO.PWM(B, 70)

pwmR.start(0)
pwmG.start(0)
pwmB.start(0)

def ledChange(r,g,b):
    if r>=0&&r<=255&&g>=0&&g<=255&&b>=0&&b<=255:
        pwmR.ChangeDutyCycle(r)
        pwmG.ChangeDutyCycle(g)
        pwmB.ChangeDutyCycle(b)
    else:
        print('wrong input')

def ledChange(color):
    if color=='r':
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(100)
    if color=='g':
     	pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
    if color=='b':
     	pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
    if color=='w':
     	pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
    else:
        print('wrong input')
 
try:
	t = 1
    while True:
	    ledChange(0,100,100) #红色
	    time.sleep(t)
	    ledChange(100,0,100) #绿色
	    time.sleep(t)
	    ledChange(100,100,0) #蓝色
	    time.sleep(t)
	    ledChange(0,0,100) #黄色
	    time.sleep(t)
	    ledChange(0,100,0) #紫色
	    time.sleep(t)
	    ledChange(100,0,0) #青色
	    time.sleep(t)
	    ledChange(0,0,0) #白色
	    time.sleep(t)
	    ledChange(r) #红色
	    time.sleep(t)
	   	ledChange(g) #绿色
	    time.sleep(t)
	    ledChange(b) #蓝色
	    time.sleep(t)
	    ledChange(w) #白色
	    time.sleep(t)
except KeyboardInterrupt:
    pass

#关闭RGBled灯
pwmR.stop()
pwmG.stop()
pwmB.stop()
#释放引脚
RPi.GPIO.cleanup()