# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for,  \
     render_template
import remote
import remote_tv
import remote_sky
import remote_audio
import remote_appletv
from xml.dom import minidom
import urllib
import tvitem
import sys
import operator
import remote_clock
import WashingMachine
from datetime import datetime
from WashingMachineStates import WashingMachineState

BASE_URL = ''

app = Flask(__name__)

def getText(node, key):
    alist=node.getElementsByTagName(key)
    for a in alist:
        text=a.childNodes[0].nodeValue
        return text

def getAttribute(node, key, attribute):
    alist = node.getElementsByTagName(key)
    for a in alist:
        value = a.attributes[attribute].value
        return value

@app.route("/pin")
def enter_pin():
    remote_sky.pin()
    return redirect(url_for('index'))

@app.route("/tv/up")
def tv_up():
    print "up"
    remote_sky.up()
    return redirect(url_for('index'))

@app.route("/tv/down")
def tv_down():
    print "down"
    remote_sky.down()
    return redirect(url_for('index'))

@app.route("/")
def index():
    url = 'http://www.tvmovie.de/rss/tvjetzt.xml'
    tvTime = request.args.get('tv-time', '')
    if tvTime == "2015":
        url = 'http://www.tvmovie.de/rss/tv2015.xml'
    elif tvTime == "2200":
        url = 'http://www.tvmovie.de/rss/tv2200.xml'

    xmldoc = minidom.parse(urllib.urlopen(url))
    tvItemList = xmldoc.getElementsByTagName('item')

    resultList = []
    for node in tvItemList:
        title=getText(node, 'title')
        previewImageUrl = getAttribute(node, 'enclosure', 'url')
        #channel=title.split('|')[1].strip().replace(" ", "").lower()
        channel=title[6:].split('-')[0].strip().replace(" ", "").lower()

        iconName = "tv-channel/" + channel + ".gif"

        for mapKey,mapValue in remote_sky.channelMap.iteritems():
            if ((mapKey.decode("utf-8") == channel) and (mapValue !="")):
                item=tvitem.tvitem(title, channel, iconName, previewImageUrl, int(mapValue))
                resultList.append(item)
    sorted_resultList = sorted(resultList, key=operator.attrgetter('channelNumber'))
    return render_template('index.html', tvItemList=sorted_resultList)

@app.route("/tv")
def command_tv():
    command = request.args.get('command', '')

    if command == "on":
        remote_sky.standby()
        remote_tv.standby()
        remote_audio.optical()

    if command == "off":
        remote_sky.standby()
        remote_tv.standby()
        remote_audio.standby()

    if command == "switch":
        channel = request.args.get('channel', '')
        remote_sky.switch(channel)

    sys.stdout.flush()

    return redirect(url_for('index'))

@app.route("/radio")
def command_radio():
    command = request.args.get('command', '')
    if command == "on":
        remote_audio.radio()

    if command == "off":
        remote_audio.standby()

    return redirect(url_for('index'))

@app.route("/channel/<channel>", methods = ["POST"])
def channelSwitch(channel):
    remote_sky.switch(channel)
    return channel

@app.route("/blink", methods = ["POST"])
def blink():
    print "blink"
    return "blink"


@app.route("/remotecontrol/<device>/button/<button>", methods = ["POST"])
def remote_control_device_button(device, button):
    if device == "tv":
        remote_tv.press_button(str(button))
    elif device == "appletv":
        remote_appletv.press_button(str(button))
    elif device == "audio":
        remote_audio.press_button(str(button))
    elif device == "sky":
        remote_sky.press_button(str(button))
    else:
        print button
    return device

@app.route("/remotecontrol/sky")
def remote_control_sky():
    return render_template('remote_control_sky.html')

@app.route("/remotecontrol/audio")
def remote_control_audio():
    return render_template('remote_control_audio.html')

@app.route("/remotecontrol/tv")
def remote_control_tv():
    return render_template('remote_control_samsung.html')

@app.route("/remotecontrol/appletv")
def remote_control_appletv():
    return render_template('remote_control_appletv.html')

@app.route("/remotecontrol")
def remote_control():
    return render_template('remote_control.html')

@app.route("/rc")
@app.route("/rc/<device>")
def index_rc(device=None):
    # Get the devices from the config file
    devices = []
    for dev in remote.devices():
        d = {
            'id': dev,
            'name': dev,
        }
        devices.append(d)

    return render_template('remote.html', devices=devices)


@app.route("/rc/device/<device_id>")
def device(device_id=None):
    d = {'id':device_id}
    return render_template('control.html', d=d)


@app.route("/rc/device/<device_id>/clicked/<op>")
def clicked(device_id=None, op=None):
    # Send message to Lirc to control the IR
    remote.send_once(device_id, op)

    return ""

@app.route("/clock")
def clock():
    command = request.args.get('usr_time', '')
    remote_clock.setTime(command)
    return render_template('clock.html')

@app.route("/wasch")
def washing():
    d = datetime.now()
    print str("/washing start " + d.strftime('%H:%M:%S'))
    resetParam = request.query_string
    #print resetParam
    if(resetParam == 'reset'):
        #print "reset wasch"
        WashingMachine.setState(WashingMachineState.START)

    washingMachineState = WashingMachine.getState()
    if(washingMachineState == WashingMachineState.START):
        washingStatus = "Start"
    elif(washingMachineState == WashingMachineState.IN_PROGRESS):
        washingStatus = "Mittendrin"
    elif(washingMachineState == WashingMachineState.FINISHING):
        washingStatus = "Kurz vor Ende"
    elif(washingMachineState == WashingMachineState.END):
        washingStatus = "Fertig"

    d = datetime.now()
    print str("/washing end " + d.strftime('%H:%M:%S'))
    return render_template('washing.html', washingStatus=washingStatus)


if __name__ == "__main__":
    import logging
    logging.basicConfig(filename='debug.log',level=logging.DEBUG)

    app.run(host='0.0.0.0', port=80, debug=True)
