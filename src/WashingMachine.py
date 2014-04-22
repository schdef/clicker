# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import WashingMachineStates as wms
from pickle import GET

switchPin = 18
washingMachineState = wms.WashingMachineState.START
lastSwitchEvent = time.time()
switchState = wms.SwitchState.UNKNOWN

def setState(state):
    global washingMachineState
    washingMachineState = state


def nextState():
    global washingMachineState
    if(washingMachineState == wms.WashingMachineState.START):
        washingMachineState = wms.WashingMachineState.IN_PROGRESS
    elif(washingMachineState == wms.WashingMachineState.IN_PROGRESS):
        washingMachineState = wms.WashingMachineState.FINISHING
    elif(washingMachineState == wms.WashingMachineState.FINISHING):
        washingMachineState = wms.WashingMachineState.END


def getState():
    global washingMachineState
    global lastSwitchEvent
    if(washingMachineState == wms.WashingMachineState.START):
        state = getSwitchState()
        if(state == wms.SwitchState.OFF):
            nextState()
            return getState()
        else:
            return "Gerade angefangen"
    elif(washingMachineState == wms.WashingMachineState.IN_PROGRESS):
        state = getSwitchState()
        if(state == wms.SwitchState.ON):
            lastSwitchEvent = time.time()
            nextState()
            return getState()
        else:
            return "Mittendrin"
    elif(washingMachineState == wms.WashingMachineState.FINISHING):
        if(time.time() > (lastSwitchEvent + 5)):
            nextState()
            return getState()
        else:
            return "Fast fertig"
    elif(washingMachineState == wms.WashingMachineState.END):
        return "Fertig"
    else:
        return "Unbekannt"


def getSwitchState():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(switchPin, GPIO.IN)
    global lastSwitchEvent
    global switchState

    lastSwitchEvent = time.time()
    if(GPIO.input(switchPin) == GPIO.LOW):
        switchState = wms.SwitchState.ON
    else:
        switchState = wms.SwitchState.OFF
    return wms.SwitchState.OFF