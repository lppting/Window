#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import json


OPEN = 20
CLOSE = 21

WIN_CLOSE = 19
WIN_OPEN = 26

BLIND_CLOSE  = 5
BLIND_OPEN = 6
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(OPEN,GPIO.OUT)
GPIO.setup(CLOSE,GPIO.OUT)
GPIO.setup(WIN_CLOSE,GPIO.OUT)
GPIO.setup(WIN_OPEN,GPIO.OUT)
GPIO.setup(BLIND_CLOSE,GPIO.OUT)
GPIO.setup(BLIND_OPEN,GPIO.OUT)

def PiOpen(pin,OpenTime):
    GPIO.output(pin,True)
    time.sleep(OpenTime)
    GPIO.output(pin,False)
#    GPIO.cleanup()
def PiClose(pin,CloseTime):
    GPIO.output(pin,True)
    time.sleep(CloseTime)
    GPIO.output(pin,False)
#    GPIO.cleanup()    
def WINClose(pin,CloseTime):
    GPIO.output(pin,True)
    time.sleep(CloseTime)
    GPIO.output(pin,False)

def WINOpen(pin,CloseTime):
    GPIO.output(pin,True)
    time.sleep(CloseTime)
    GPIO.output(pin,False)

def BClose(pin,CloseTime):
    GPIO.output(pin,True)
    time.sleep(CloseTime)
    GPIO.output(pin,False)

def BOpen(pin,CloseTime):
    GPIO.output(pin,True)
    time.sleep(CloseTime)
    GPIO.output(pin,False)

def MainControl(ControlTime,pinx,piny):
#    OPEN = 21
#    CLOSE = 20
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(OPEN,GPIO.OUT)
#    GPIO.setup(CLOSE,GPIO.OUT)
#    print OPEN
    T = ControlTime
    if T > 0:
        PiOpen(pinx,T)
    if T < 0:
        PiClose(piny,0-T)
#    GPIO.cleanup()

if __name__ == "__main__":
#    MainControl(-18)    
#    GPIO.cleanup()
#    d = {"solar":0,"window":0,"blind":0}
#    data = json.dumps(d,indent=4)
    f = open("c.json","r+")
    text = f.read()
    f.close()
    data = json.loads(text)
    s = float(data["solar"])
    w = float(data["window"])
    b = float(data["blind"])
    MainControl(s,OPEN,CLOSE)
    MainControl(w,WIN_OPEN,WIN_CLOSE)
    MainControl(b,BLIND_OPEN,BLIND_CLOSE)
