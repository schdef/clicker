# -*- coding: utf-8 -*-
import time
import SwitchState
from datetime import datetime

from WashingMachineStates import WashingMachineState
import GPIOHelper

switchPin = 18
washingMachineState = WashingMachineState.START
lastSwitchEvent = time.time()
switchState = SwitchState.SwitchState.UNKNOWN
delayInSeconds = 5

def setState(state):
    global washingMachineState
    global lastSwitchEvent
    global switchState
    #print "setState"
    washingMachineState = state
    lastSwitchEvent = time.time()
    switchState = SwitchState.SwitchState.UNKNOWN

def nextState():
    global washingMachineState
    if(washingMachineState == WashingMachineState.START):
        washingMachineState = WashingMachineState.IN_PROGRESS
    elif(washingMachineState == WashingMachineState.IN_PROGRESS):
        washingMachineState = WashingMachineState.FINISHING
    elif(washingMachineState == WashingMachineState.FINISHING):
        washingMachineState = WashingMachineState.END


def getState():
    #d = datetime.now()
    #print str("getState start " + d.strftime('%H:%M:%S'))
    global washingMachineState
    global lastSwitchEvent
    result=WashingMachineState.START
    if(washingMachineState == WashingMachineState.START):
        print "START"
        state = getSwitchState()
        if(state == SwitchState.SwitchState.OFF and ((lastSwitchEvent + delayInSeconds) < time.time())):
            nextState()
        result=washingMachineState
    elif(washingMachineState == WashingMachineState.IN_PROGRESS):
        print "IN_PROGRESS"
        state = getSwitchState()
        if(state == SwitchState.SwitchState.ON):
            lastSwitchEvent = time.time()
            nextState()
        result=washingMachineState
    elif(washingMachineState == WashingMachineState.FINISHING):
        print "FINISHING"
        if(time.time() > (lastSwitchEvent + delayInSeconds)):
            nextState()
        result=washingMachineState
    elif(washingMachineState == WashingMachineState.END):
        print "END"
        result=washingMachineState
    else:
        result=WashingMachineState.UNKNOWN
    #d = datetime.now()
    #print str("getState end " + d.strftime('%H:%M:%S'))
    return result

def getSwitchState():
    return GPIOHelper.getSwitchState(switchPin)
