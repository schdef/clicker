# -*- coding: utf-8 -*-
import remote

def command(irCode):
   remote.command(irCode)

def standby():
    irCode = [0, 207, 0, 213, 0, 25, 0, 81, 0, 25, 0, 81, 0, 24, 0, 81, 0, 24, 0, 30, 0, 23, 0, 30, 0, 26, 0, 27, 0, 23, 0, 31, 0, 27, 0, 27, 0, 25, 0, 79, 0, 26, 0, 81, 0, 24, 0, 82, 0, 25, 0, 28, 0, 27, 0, 28, 0, 24, 0, 29, 0, 24, 0, 31, 0, 23, 0, 30, 0, 24, 0, 30, 0, 26, 0, 79, 0, 26, 0, 29, 0, 24, 0, 30, 0, 25, 0, 29, 0, 26, 0, 28, 0, 22, 0, 32, 0, 23, 0, 30, 0, 26, 0, 79, 0, 24, 0, 32, 0, 25, 0, 79, 0, 25, 0, 81, 0, 23, 0, 82, 0, 26, 0, 79, 0, 25, 0, 79, 0, 28, 0, 78, 0, 26, 255, 255]
    command(irCode)

def number_one(sameAgain):
    pass

def number_two(sameAgain):
    pass

def number_three(sameAgain):
    pass

def number_four(sameAgain):
    pass

def number_five(sameAgain):
    pass

def number_six(sameAgain):
    pass

def number_seven(sameAgain):
    pass

def number_eight(sameAgain):
    pass

def number_nine(sameAgain):
    pass

def number_zero(sameAgain):
    pass

def number(value, sameAgain):
    if value == '1': number_one(sameAgain)
    elif value == '2': number_two(sameAgain)
    elif value == '3': number_three(sameAgain)
    elif value == '4': number_four(sameAgain)
    elif value == '5': number_five(sameAgain)
    elif value == '6': number_six(sameAgain)
    elif value == '7': number_seven(sameAgain)
    elif value == '8': number_eight(sameAgain)
    elif value == '9': number_nine(sameAgain)
    elif value == '0': number_zero(sameAgain)

def up(sameAgain):
    pass

def down(sameAgain):
    pass

def input_source():
    irCode=[0, 209, 0, 208, 0, 27, 0, 77, 0, 27, 0, 77, 0, 25, 0, 79, 0, 27, 0, 25, 0, 26, 0, 26, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 77, 0, 26, 0, 78, 0, 27, 0, 77, 0, 27, 0, 24, 0, 25, 0, 27, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 77, 0, 27, 0, 24, 0, 27, 0, 24, 0, 26, 0, 25, 0, 25, 0, 26, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 25, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 77, 0, 26, 0, 78, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 8, 120, 0, 210, 0, 207, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 24, 0, 27, 0, 25, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 25, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 77, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 27, 0, 24, 0, 26, 0, 26, 0, 25, 0, 27, 0, 27, 0, 24, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 0, 77, 0, 27, 8, 120, 0, 208, 0, 209, 0, 26, 0, 78, 0, 26, 0, 78, 0, 26, 0, 78, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 78, 0, 27, 0, 77, 0, 26, 0, 78, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 78, 0, 26, 0, 26, 0, 27, 0, 25, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 26, 0, 78, 0, 26, 0, 78, 0, 26, 0, 78, 0, 26, 0, 78, 0, 27, 0, 77, 0, 26, 0, 78, 0, 26, 0, 78, 0, 26, 255, 255]
    command(irCode)

def press_button(button):
    eval(button + "()")
