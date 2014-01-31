# -*- coding: utf-8 -*-
from lirc.lirc import Lirc

lircParse = Lirc('/etc/lirc/lircd.conf')

def command(irCode):
    lircParse.send_once('HARMON-KARDON', irCode)

def optical():
    command('KEY_OPTICAL')

def aux():
    command('KEY_AUX')

def mute():
    command('KEY_MUTE')

def standby():
    command('KEY_POWER')

def radio():
    command('KEY_RADIO')

def volumeUp():
    command('KEY_VOLUMEUP')

def tripleVolumeUp():
    volumeUp()
    volumeUp()
    volumeUp()

# leiser
def volumeDown():
    command('KEY_VOLUMEDOWN')

def tripleVolumeDown():
    volumeDown()
    volumeDown()
    volumeDown()

def number_one():
    pass

def number_two():
    pass

def number_three():
    pass

def number_four():
    pass

def number_five():
    pass

def press_button(button):
    eval(button + "()")


