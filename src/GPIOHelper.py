# -*- coding: utf-8 -*-
class GPIOMock(object):
    BOARD = 10
    IN = 0
    LOW = 0

    def setmode(self, typ):
        pass

    def setup(self, pin, typ):
        pass

    def input(self, pin):
        pass

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = GPIOMock()
from SwitchState import SwitchState
from datetime import datetime

def getSwitchState(switchPin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(switchPin, GPIO.IN)
    #d = datetime.now()
    #print str("getSwitchState start " + d.strftime('%H:%M:%S'))

    result=SwitchState.UNKNOWN
    if(GPIO.input(switchPin) == GPIO.LOW):
        #print "ON"
        result=SwitchState.ON
    else:
        #print "OFF"
        result=SwitchState.OFF

    #d = datetime.now()
    #print str("getSwitchState end " + d.strftime('%H:%M:%S'))
    return result

