# -*- coding: utf-8 -*-
from lirc.lirc import Lirc

lircParse = Lirc('/etc/lirc/lircd.conf')

def command(irCode):
    lircParse.send_once('APPLE-TV', irCode)

def standby():
    pass

def up():
    command('KEY_UP')

def down():
    command('KEY_DOWN')

def full_down():
    down()
    down()
    down()
    down()
    down()

def left():
    command('KEY_LEFT')

def right():
    command('KEY_RIGHT')

def full_right():
    right()
    right()
    right()
    right()
    right()
    right()

def menu():
    command('KEY_MENUE')

def okay():
    command('KEY_MENUE')

def play_pause():
    command('KEY_PLAY')

def press_button(button):
    eval(button + "()")
