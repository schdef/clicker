# -*- coding: utf-8 -*-
from lirc.lirc import Lirc

lircParse = Lirc('/etc/lirc/lircd.conf')

def command(irCode):
    lircParse.send_once('TV', irCode)

def standby():
    command('KEY_POWER')

def input_source():
    command('KEY_SOURCE')

def press_button(button):
    eval(button + "()")
