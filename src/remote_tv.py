# -*- coding: utf-8 -*-
import remote

def command(irCode):
    remote.send_once('TV', irCode)

def standby():
    command('KEY_POWER')

def input_source():
    command('KEY_SOURCE')

def press_button(button):
    eval(button + "()")
