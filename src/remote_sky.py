# -*- coding: utf-8 -*-
from lirc.lirc import Lirc

channelMap = {
'ard':'1','zdf':'2','rtl':'4','sat.1':'5','pro7':'7','rtlii':'6','kabel1':'8','vox':'9','sport1':'290','sport1+':'235','sport1us':'52','eurosport':'239','eurosport2':'240','fueltv':'','tele5':'35','sixx':'24','dmax':'485','dasvierte':'367','comedycentral':'550','rtlnitro':'33','prosiebenmaxx':'22','arte':'480','3sat':'496','einsfestival':'491','einsplus':'492','tagesschau24':'','zdfneo':'25','zdf.kultur':'493','zdfinfo':'34','phoenix':'494','bralpha':'832','ntv':'712','n24':'711','wdr':'859','ndr':'847','mdr':'845','b3':'3','swrfernsehen':'856','rbb':'853','h3':'840','ki.ka':'','superrtl':'29','nickelodeon':'550','ric':'','anixehd':'','servustv':'28','viva':'','sat1gold':'190','deluxemusictv':'609','hse24':'','qvc':'','orf1':'','orf2':'','sf1':'','sf2':'','bbcworld':'','bloombergtv':'','cnn':'','euronews':'713','astrotv':'','gotv':'','bibel':'','skycinema':'14','skycinema+1':'321','skycinema+24':'322','skyaction':'20','skycomedy':'21','skyemotion':'32','skynostalgie':'327','skyhits':'19','skyatlantichd':'10','mgm':'309','disneycinemagic':'308','skyfussballbundesliga':'211','skysport1':'47','skysport2':'48','skysportnewshd':'200','skysportaustria':'','tntfilm':'15','axn':'27','kinowelttv':'','kabeleinsclassics':'','13thstreet':'16','fox':'11','tntserie':'13','syfy':'12','rtlcrime':'137','skykrimi':'130','sat1emotions':'144','motorvisiontv':'430','nationalgeographic':'400','natgeowild':'402','biographychannel':'','history':'407','spiegelgeschichte':'425','discoveryhd':'409','rtlliving':'17','romancetv':'145','goldstartv':'','heimatkanal':'','rtlpassion':'140','beate':'','cartoonnetwork':'','disneychannel':'500','disneyxd':'','boomerang':'','junior':'','animax':'143','nicktoons':'','classica':'','mtv':'','vh1classic':'','glitz':'23','unichan':'','e!entertainmenttelevision':'128','fashiontvhd':'','sportdigital.tv':'','extremesportschannel':'','spiegeltvwissen':'','planet':'31','silverline':'','gutelaunetv':'','jukebox':'','sonnenklar.tv':'','bongusto':'18','babytv':'','lustpur':'','animalplanet':'','automotorsport':'','motorstv':'','kidsco':'','nickjr.':'','mtvhits':'','mtvlivehd':'606','imusic1':'','trace':'','deutschesanlegerfernsehen':'','wetterfernsehen':'','yourfamilyentertainment':'','mtvmusic':'','mtvbase':'','timm':'','hustlertv':'','nl1':'','nl2':'','nl3':'','bbcentertainment':'','dr1':'','dr2':'','atv':'','puls4':'','k':'','finelivingnetwork':'','oktotv':'','mcmtop':'','tv5':'','tveén(belgien)':'','itvn':'','tvpolonia':'','tvpinfo':'','tvpkultura':'','detskimir':'','nashekino':'','rtr':'','rtvi':'','atvavrupa':'','eurod':'','eurostar':'','kanal7int':'','powertürk':'','showturk':'','tgrteu':'','türkmax':'','mezzolivehd':'','luxetv':'','prosiebenfun':'','mtvdance':'','mezzo':'','rocktv':'','disneyjunior':'','jimjam':'','thekaraokechannel':'','sonyentertainment':''
}

lircParse = Lirc('/etc/lirc/lircd.conf')


def command(irCode):
    lircParse.send_once('SKY', irCode)

def standby():
    command('KEY_POWER')

def number(value):
    command('KEY_' + value)

def switch(channel):
    channelNumber = channelMap[channel]
    for character in channelNumber:
        number(character)
    command('KEY_OK')

def pin():
    command('KEY_3')
    command('KEY_0')
    command('KEY_0')
    command('KEY_7')

def channel_up():
    command('KEY_CHANNELUP')

def channel_down():
    command('KEY_CHANNELDOWN')

def okay():
    command('KEY_OK')

def back():
    command('KEY_BACK')

def mute():
    command('KEY_MUTE')

def guide():
    command('KEY_GUIDE')

def up():
    command('KEY_UP')

def right():
    command('KEY_RIGHT')

def down():
    command('KEY_DOWN')

def left():
    command('KEY_LEFT')

def blue():
    command('KEY_BLUE')

def yellow():
    command('KEY_YELLOW')

def info():
    command('KEY_INFO')

def press_button(button):
    eval(button + "()")
