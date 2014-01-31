# -*- coding: utf-8 -*-
from lirc.lirc import Lirc

lircParse = None

def init():
    global lircParse
    if(lircParse == None):
        lircParse = Lirc('/etc/lirc/lircd.conf')

def send_once(device_id, irCode):
    init()
    global lircParse
    lircParse.send_once(device_id, irCode)

def devices():
    init()
    global lircParse
    return lircParse.devices()