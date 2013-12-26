# -*- coding: utf-8 -*-
import serial
import irtoy

def command(irCode):
    with serial.Serial('/dev/ttyACM0') as serialDevice:
        toy = irtoy.IrToy(serialDevice)
        try:
            toy.transmit(irCode)
        except:
            print "Unexpected error:", sys.exc_info()[0]
        finally:
            toy.reset()
