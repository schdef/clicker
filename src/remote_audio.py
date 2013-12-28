# -*- coding: utf-8 -*-
import remote

def command(irCode):
    remote.command(irCode)

def optical():
    irCode = [1, 163, 0, 213, 0, 26, 0, 26, 0, 25, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 25, 0, 26, 0, 26, 0, 78, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 78, 0, 25, 0, 78, 0, 25, 0, 78, 0, 25, 0, 26, 0, 25, 0, 78, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 78, 0, 25, 0, 79, 0, 25, 0, 78, 0, 25, 0, 79, 0, 25, 0, 78, 0, 26, 0, 26, 0, 25, 0, 79, 0, 25, 0, 79, 0, 25, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 25, 0, 26, 0, 25, 0, 27, 0, 23, 8, 38, 1, 163, 0, 107, 0, 26, 17, 147, 1, 163, 0, 107, 0, 27, 255, 255]
    command(irCode)

def aux():
    irCode=[1, 166, 0, 210, 0, 28, 0, 24, 0, 25, 0, 26, 0, 25, 0, 26, 0, 25, 0, 25, 0, 28, 0, 24, 0, 25, 0, 26, 0, 25, 0, 26, 0, 25, 0, 79, 0, 27, 0, 24, 0, 25, 0, 26, 0, 25, 0, 25, 0, 29, 0, 23, 0, 25, 0, 79, 0, 25, 0, 78, 0, 29, 0, 76, 0, 25, 0, 25, 0, 29, 0, 24, 0, 26, 0, 78, 0, 26, 0, 25, 0, 28, 0, 76, 0, 25, 0, 26, 0, 26, 0, 25, 0, 27, 0, 78, 0, 25, 0, 78, 0, 28, 0, 77, 0, 26, 0, 26, 0, 26, 0, 77, 0, 28, 0, 24, 0, 25, 0, 78, 0, 29, 0, 76, 0, 25, 0, 25, 0, 27, 0, 24, 0, 24, 8, 37, 1, 166, 0, 105, 0, 22, 17, 150, 1, 166, 0, 104, 0, 24, 255, 255]
    command(irCode)

def mute():
    irCode=[1, 166, 0, 210, 0, 27, 0, 25, 0, 27, 0, 25, 0, 25, 0, 26, 0, 25, 0, 25, 0, 27, 0, 25, 0, 27, 0, 24, 0, 25, 0, 26, 0, 25, 0, 78, 0, 29, 0, 24, 0, 25, 0, 26, 0, 26, 0, 25, 0, 27, 0, 25, 0, 27, 0, 77, 0, 26, 0, 77, 0, 29, 0, 76, 0, 26, 0, 24, 0, 27, 0, 77, 0, 26, 0, 25, 0, 25, 0, 25, 0, 27, 0, 24, 0, 27, 0, 25, 0, 25, 0, 26, 0, 26, 0, 77, 0, 29, 0, 76, 0, 26, 0, 25, 0, 27, 0, 77, 0, 26, 0, 77, 0, 27, 0, 77, 0, 26, 0, 77, 0, 27, 0, 77, 0, 26, 0, 25, 0, 25, 0, 25, 0, 23, 255, 255]
    command(irCode)

def standby():
    irCode = [1, 163, 0, 214, 0, 24, 0, 27, 0, 24, 0, 79, 0, 25, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 25, 0, 27, 0, 25, 0, 79, 0, 25, 0, 27, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 79, 0, 25, 0, 80, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 27, 0, 25, 0, 27, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 80, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 80, 0, 23, 255, 255]
    command(irCode)

def radio():
    irCode = [1, 166, 0, 210, 0, 27, 0, 25, 0, 26, 0, 26, 0, 25, 0, 26, 0, 25, 0, 26, 0, 25, 0, 26, 0, 25, 0, 26, 0, 25, 0, 27, 0, 25, 0, 79, 0, 26, 0, 26, 0, 25, 0, 26, 0, 25, 0, 27, 0, 25, 0, 27, 0, 25, 0, 79, 0, 25, 0, 78, 0, 26, 0, 78, 0, 26, 0, 25, 0, 25, 0, 79, 0, 26, 0, 25, 0, 25, 0, 26, 0, 25, 0, 26, 0, 25, 0, 27, 0, 25, 0, 27, 0, 25, 0, 27, 0, 25, 0, 79, 0, 25, 0, 26, 0, 25, 0, 79, 0, 26, 0, 78, 0, 26, 0, 78, 0, 26, 0, 78, 0, 26, 0, 78, 0, 26, 0, 79, 0, 25, 0, 25, 0, 23, 8, 39, 1, 167, 0, 104, 0, 22, 17, 151, 1, 165, 0, 106, 0, 21, 255, 255]
    command(irCode)

# lauter
def volumeUp():
    irCode = [1, 163, 0, 213, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 28, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 28, 0, 24, 0, 27, 0, 24, 0, 79, 0, 24, 0, 80, 0, 24, 0, 79, 0, 25, 0, 27, 0, 25, 0, 79, 0, 24, 0, 80, 0, 24, 0, 80, 0, 25, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 79, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 80, 0, 24, 0, 80, 0, 25, 0, 27, 0, 24, 0, 28, 0, 22, 255, 255]
    command(irCode)

def tripleVolumeUp():
    volumeUp()
    volumeUp()
    volumeUp()

# leiser
def volumeDown():
    irCode = [1, 163, 0, 213, 0, 24, 0, 27, 0, 24, 0, 27, 0, 25, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 80, 0, 25, 0, 79, 0, 24, 0, 27, 0, 25, 0, 27, 0, 25, 0, 27, 0, 25, 0, 27, 0, 25, 0, 79, 0, 25, 0, 27, 0, 25, 0, 27, 0, 24, 0, 80, 0, 25, 0, 79, 0, 24, 0, 79, 0, 25, 0, 79, 0, 25, 0, 79, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 8, 37, 1, 163, 0, 213, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 25, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 80, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 25, 0, 79, 0, 24, 0, 27, 0, 25, 0, 27, 0, 25, 0, 79, 0, 25, 0, 79, 0, 24, 0, 80, 0, 24, 0, 79, 0, 24, 0, 80, 0, 24, 0, 27, 0, 24, 0, 80, 0, 24, 0, 79, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 255, 255]
    command(irCode)

def tripleVolumeDown():
    volumeDown()
    volumeDown()
    volumeDown()

def number_one():
    irCode=[0, 44, 0, 48, 0, 91, 0, 88, 0, 91, 0, 90, 0, 44, 0, 44, 0, 91, 0, 42, 0, 46, 0, 44, 0, 43, 0, 46, 0, 42, 0, 47, 0, 45, 0, 89, 0, 45, 0, 45, 0, 44, 255, 255]
    command(irCode)

def number_two():
    irCode=[0, 45, 0, 49, 0, 45, 0, 44, 0, 46, 0, 43, 0, 91, 0, 89, 0, 45, 0, 43, 0, 90, 0, 45, 0, 45, 0, 42, 0, 46, 0, 43, 0, 46, 0, 87, 0, 91, 0, 43, 0, 46, 255, 255]
    command(irCode)

def number_three():
    irCode=[0, 45, 0, 49, 0, 44, 0, 45, 0, 44, 0, 44, 0, 91, 0, 89, 0, 46, 0, 44, 0, 89, 0, 44, 0, 46, 0, 43, 0, 42, 0, 47, 0, 43, 0, 91, 0, 89, 0, 89, 0, 46, 255, 255]
    command(irCode)

def number_four():
    irCode=[0, 48, 0, 46, 0, 45, 0, 44, 0, 46, 0, 44, 0, 89, 0, 89, 0, 47, 0, 42, 0, 88, 0, 46, 0, 45, 0, 44, 0, 44, 0, 45, 0, 45, 0, 89, 0, 44, 0, 43, 0, 91, 255, 255]
    command(irCode)

def number_five():
    irCode=[0, 42, 0, 50, 0, 89, 0, 90, 0, 89, 0, 90, 0, 45, 0, 43, 0, 92, 0, 42, 0, 43, 0, 45, 0, 43, 0, 47, 0, 42, 0, 91, 0, 48, 0, 41, 0, 47, 0, 42, 0, 47, 16, 2, 0, 46, 0, 46, 0, 89, 0, 89, 0, 89, 0, 90, 0, 43, 0, 47, 0, 88, 0, 45, 0, 49, 0, 41, 0, 45, 0, 43, 0, 47, 0, 88, 0, 44, 0, 44, 0, 50, 0, 39, 0, 45, 255, 255]
    command(irCode)

def press_button(button):
    eval(button + "()")


