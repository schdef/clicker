# -*- coding: utf-8 -*-
import remote

def command(irCode):
    remote.command(irCode)

def standby():
    pass

def up():
    irCode = [1, 171, 0, 206, 0, 30, 0, 22, 0, 30, 0, 74, 0, 30, 0, 73, 0, 30, 0, 74, 0, 29, 0, 22, 0, 30, 0, 73, 0, 29, 0, 74, 0, 30, 0, 73, 0, 29, 0, 74, 0, 30, 0, 74, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 22, 0, 30, 0, 74, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 74, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 23, 0, 30, 7, 101, 1, 170, 0, 101, 0, 30, 255, 255]
    command(irCode)

def down():
    irCode = [1, 171, 0, 207, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 74, 0, 30, 0, 22, 0, 29, 0, 74, 0, 30, 0, 73, 0, 29, 0, 74, 0, 29, 0, 74, 0, 30, 0, 74, 0, 29, 0, 74, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 29, 0, 74, 0, 30, 0, 73, 0, 30, 0, 22, 0, 29, 0, 74, 0, 30, 0, 73, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 22, 0, 29, 0, 22, 0, 30, 0, 73, 0, 30, 0, 73, 0, 29, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 23, 0, 30, 7, 102, 1, 170, 0, 101, 0, 30, 255, 255]
    command(irCode)

def full_down():
    down()
    down()
    down()
    down()
    down()

def left():
    irCode = [1, 171, 0, 206, 0, 30, 0, 22, 0, 29, 0, 74, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 74, 0, 30, 0, 73, 0, 29, 0, 74, 0, 30, 0, 74, 0, 30, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 21, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 7, 207, 1, 170, 0, 101, 0, 30, 255, 255]
    command(irCode)

def right():
    irCode = [1, 171, 0, 207, 0, 30, 0, 22, 0, 30, 0, 74, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 74, 0, 30, 0, 74, 0, 29, 0, 74, 0, 30, 0, 74, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 74, 0, 29, 0, 74, 0, 29, 0, 74, 0, 30, 0, 74, 0, 30, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 21, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 73, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 7, 103, 1, 171, 0, 101, 0, 30, 255, 255]
    command(irCode)

def full_right():
    right()
    right()
    right()
    right()
    right()
    right()

def menu():
    irCode = [1, 171, 0, 206, 0, 30, 0, 22, 0, 30, 0, 73, 0, 29, 0, 74, 0, 29, 0, 74, 0, 30, 0, 22, 0, 29, 0, 74, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 74, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 22, 0, 29, 0, 74, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 22, 0, 29, 0, 22, 0, 29, 0, 22, 0, 29, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 22, 0, 29, 0, 22, 0, 29, 0, 22, 0, 30, 0, 23, 0, 30, 255, 255]
    command(irCode)

def okay():
    irCode = [1, 171, 0, 206, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 73, 0, 29, 0, 74, 0, 30, 0, 22, 0, 29, 0, 74, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 74, 0, 30, 0, 73, 0, 29, 0, 74, 0, 30, 0, 22, 0, 30, 0, 74, 0, 30, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 7, 5, 1, 170, 0, 206, 0, 30, 0, 22, 0, 30, 0, 73, 0, 30, 0, 74, 0, 30, 0, 73, 0, 30, 0, 22, 0, 30, 0, 74, 0, 29, 0, 74, 0, 30, 0, 73, 0, 30, 0, 73, 0, 30, 0, 74, 0, 29, 0, 74, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 29, 0, 74, 0, 30, 0, 22, 0, 29, 0, 22, 0, 29, 0, 74, 0, 30, 0, 21, 0, 30, 0, 22, 0, 29, 0, 22, 0, 30, 0, 22, 0, 30, 0, 22, 0, 30, 0, 21, 0, 30, 0, 22, 0, 29, 0, 74, 0, 29, 0, 74, 0, 29, 0, 22, 0, 29, 0, 23, 0, 30, 0, 22, 0, 30, 0, 23, 0, 29, 255, 255]
    command(irCode)

def play_pause():
    pass

def press_button(button):
    eval(button + "()")
