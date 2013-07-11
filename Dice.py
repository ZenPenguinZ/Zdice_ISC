#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gobject
import random
import os
import sys
import gtk
import logging
from zdice import Die
from zdice import Hand
from zdice import Player
from zdice import Players_Group
from zdice import Dice_Cup
#EndImports

class iscApp1:
 iscVerror = "Error!"
 iscVred = "red"
 iscVyellow = "yellow"
 iscVdie2 = "die2"
 iscVdie1 = "die1"
 iscVgreen = "green"
 iscVdie1text = ""
 iscVdie2text = ""
 iscVisGreenBrains = "Green brains"
 iscVisYellowbrains = "Yellow brains"
 iscVisRedbrains = "Red brains"
 iscVisGreenrun = "Green run"
 iscVisYellowrun = "Yellow run"
 iscVisYellowshot = "Yellow shot"
 iscVisRedrun = "Red run"
 iscVisGreenshot = "Green shot"
 iscVisRedshot = "Red shot"
 iscVDice_Cup = ""
 iscVPlayers_Group = ""
 iscVhand = ""
 iscVdie0text = ""
 iscVzero = 0
 iscVone = 1
 iscVtwo = 2
 iscVDeadMessage = "You are Dead!"
 iscVhandShots = 0
 iscVhandBrains = 0
 iscVtemp = ""
 iscVCurrentPlayer = ""
 iscVNumberPlayers = 0
 iscVempty_str = ""
 iscWindow11Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow11Window1Fixed = gtk.Fixed()
 iscWindow11Die10 = gtk.Image()
 iscWindow11Die20 = gtk.Image()
 iscWindow11Roll0 = gtk.Button("Roll")
 iscWindow11test10 = gtk.Entry()
 iscWindow11test20 = gtk.Entry()
 iscWindow11die00 = gtk.Image()
 iscWindow11Label0 =gtk.Label("Hand")
 iscWindow11Test00 = gtk.Entry()
 iscWindow11Score0 = gtk.Button("Score Hand")
 iscWindow11Pass0 = gtk.Button("Pass")
 iscWindow11Brains0 =gtk.Label("Brains")
 iscWindow11Shots0 =gtk.Label("Shots")
 iscWindow11getdice0 = gtk.Button("get dice")
 iscWindow11dialog2 = gtk.Entry()

 iscWindow12Player1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow12Player1Fixed = gtk.Fixed()
 iscWindow12addPlayer0 = gtk.Button("Add")
 iscWindow12done0 = gtk.Button("Done")
 iscWindow12Plist0 = gtk.TextView(buffer=None)
 iscWindow12Pname0 = gtk.TextView(buffer=None)
 iscWindow12Label0 =gtk.Label("Enter your name")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()



#EndOfClass

def iscinit_zdice15():
 thisiscApp1.iscVDice_Cup=Dice_Cup()
 thisiscApp1.iscVPlayers_Group=Players_Group()
 thisiscApp1.iscVhand=Hand()

 iscWindow12()
 #iscinit_zdice15Done
def iscCloseWindow16():
 thisiscApp1.iscWindow12Player1.destroy()
 iscWindow11()
 #iscCloseWindow16Done


def iscRoll_Hand19():
 thisiscApp1.iscVhand.roll()
 iscPortalDeparture20()
 #iscRoll_Hand19Rolled

def iscSetLabel21():
 thisiscApp1.iscWindow11Shots0.set_label(thisiscApp1.iscVtemp)
 iscgetHandBrains23()
 #iscSetLabel21Done


def iscgetHandBrains23():
 thisiscApp1.iscVhandBrains=thisiscApp1.iscVhand.brains
 iscConvertNumberToText24()
 #iscgetHandBrains23Done

def iscConvertNumberToText24():
 thisiscApp1.iscVtemp = str(thisiscApp1.iscVhandBrains)
 iscSetLabel26()
 #iscConvertNumberToText24Done


def iscSetLabel26():
 thisiscApp1.iscWindow11Brains0.set_label(thisiscApp1.iscVtemp)
 iscPortalDeparture25()
 #iscSetLabel26Done


def iscConvertNumberToText27():
 thisiscApp1.iscVtemp = str(thisiscApp1.iscVhandShots)
 iscSetLabel21()
 #iscConvertNumberToText27Done


def iscgetHandShots29():
 thisiscApp1.iscVhandShots=thisiscApp1.iscVhand.shots
 iscConvertNumberToText27()
 #iscgetHandShots29Done

def iscSetLabel30():
 thisiscApp1.iscWindow11Label0.set_label(thisiscApp1.iscVDeadMessage)
 #iscSetLabel30Done


def iscScoreHand32():
 if thisiscApp1.iscVhand.score():
  iscgetHandShots29()
  #iscScoreHand32Alive
 else:
  iscSetLabel30()
  #iscScoreHand32Dead
def iscGet_Hand35():
 thisiscApp1.iscVhand.fill(thisiscApp1.iscVDice_Cup)
 iscPortalDeparture33()
 #iscGet_Hand35Done

def iscGetDiceText37():
 if thisiscApp1.iscVone  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVone]
  thisiscApp1.iscVdie1text = d.__repr__()
  iscIfThen65()
  iscGetDiceText45()
  #iscGetDiceText37text done
 else:
  thisiscApp1.iscVdie1text = "blank"
  iscSetCanvasPicture42()
  iscSetCanvasPicture43()
  #iscGetDiceText37blank

def iscSetCanvasPicture39():
 thisiscApp1.iscWindow11die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture39Done


def iscGetDiceText41():
 if thisiscApp1.iscVzero  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVzero]
  thisiscApp1.iscVdie0text = d.__repr__()
  iscGetDiceText37()
  iscIfThen46()
  #iscGetDiceText41text done
 else:
  thisiscApp1.iscVdie0text = "blank"
  iscSetCanvasPicture39()
  iscSetCanvasPicture42()
  iscSetCanvasPicture43()
  #iscGetDiceText41blank

def iscSetCanvasPicture42():
 thisiscApp1.iscWindow11Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture42Done


def iscSetCanvasPicture43():
 thisiscApp1.iscWindow11Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture43Done


def iscGetDiceText45():
 if thisiscApp1.iscVtwo  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVtwo]
  thisiscApp1.iscVdie2text = d.__repr__()
  iscIfThen66()
  #iscGetDiceText45text done
 else:
  thisiscApp1.iscVdie2text = "blank"
  iscSetCanvasPicture43()
  #iscGetDiceText45blank

def iscIfThen46():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture55()
  #iscIfThen46True

  pass
 else:
  iscIfThen47()
  #iscIfThen46False

  pass

def iscIfThen47():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture56()
  #iscIfThen47True

  pass
 else:
  iscIfThen48()
  #iscIfThen47False

  pass

def iscIfThen48():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture57()
  #iscIfThen48True

  pass
 else:
  iscIfThen49()
  #iscIfThen48False

  pass

def iscIfThen49():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture58()
  #iscIfThen49True

  pass
 else:
  iscIfThen50()
  #iscIfThen49False

  pass

def iscIfThen50():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture59()
  #iscIfThen50True

  pass
 else:
  iscIfThen51()
  #iscIfThen50False

  pass

def iscIfThen51():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture60()
  #iscIfThen51True

  pass
 else:
  iscIfThen52()
  #iscIfThen51False

  pass

def iscIfThen52():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture61()
  #iscIfThen52True

  pass
 else:
  iscIfThen53()
  #iscIfThen52False

  pass

def iscIfThen53():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture62()
  #iscIfThen53True

  pass
 else:
  iscIfThen54()
  #iscIfThen53False

  pass

def iscIfThen54():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture64()
  #iscIfThen54True

  pass
 else:
  iscSetLabel100()
  #iscIfThen54False

  pass

def iscSetCanvasPicture55():
 thisiscApp1.iscWindow11die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture55Done


def iscSetCanvasPicture56():
 thisiscApp1.iscWindow11die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture56Done


def iscSetCanvasPicture57():
 thisiscApp1.iscWindow11die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture57Done


def iscSetCanvasPicture58():
 thisiscApp1.iscWindow11die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture58Done


def iscSetCanvasPicture59():
 thisiscApp1.iscWindow11die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture59Done


def iscSetCanvasPicture60():
 thisiscApp1.iscWindow11die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture60Done


def iscSetCanvasPicture61():
 thisiscApp1.iscWindow11die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture61Done


def iscSetCanvasPicture62():
 thisiscApp1.iscWindow11die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture62Done


def iscIfThen63():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture77()
  #iscIfThen63True

  pass
 else:
  iscIfThen69()
  #iscIfThen63False

  pass

def iscSetCanvasPicture64():
 thisiscApp1.iscWindow11die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture64Done


def iscIfThen65():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture74()
  #iscIfThen65True

  pass
 else:
  iscIfThen67()
  #iscIfThen65False

  pass

def iscIfThen66():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture91()
  #iscIfThen66True

  pass
 else:
  iscIfThen83()
  #iscIfThen66False

  pass

def iscIfThen67():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture75()
  #iscIfThen67True

  pass
 else:
  iscIfThen68()
  #iscIfThen67False

  pass

def iscIfThen68():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture76()
  #iscIfThen68True

  pass
 else:
  iscIfThen63()
  #iscIfThen68False

  pass

def iscIfThen69():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture78()
  #iscIfThen69True

  pass
 else:
  iscIfThen70()
  #iscIfThen69False

  pass

def iscIfThen70():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture79()
  #iscIfThen70True

  pass
 else:
  iscIfThen71()
  #iscIfThen70False

  pass

def iscIfThen71():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture80()
  #iscIfThen71True

  pass
 else:
  iscIfThen72()
  #iscIfThen71False

  pass

def iscIfThen72():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture81()
  #iscIfThen72True

  pass
 else:
  iscIfThen73()
  #iscIfThen72False

  pass

def iscIfThen73():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture82()
  #iscIfThen73True

  pass
 else:
  iscSetLabel100()
  #iscIfThen73False

  pass

def iscSetCanvasPicture74():
 thisiscApp1.iscWindow11Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture74Done


def iscSetCanvasPicture75():
 thisiscApp1.iscWindow11Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture75Done


def iscSetCanvasPicture76():
 thisiscApp1.iscWindow11Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture76Done


def iscSetCanvasPicture77():
 thisiscApp1.iscWindow11Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture77Done


def iscSetCanvasPicture78():
 thisiscApp1.iscWindow11Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture78Done


def iscSetCanvasPicture79():
 thisiscApp1.iscWindow11Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture79Done


def iscSetCanvasPicture80():
 thisiscApp1.iscWindow11Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture80Done


def iscSetCanvasPicture81():
 thisiscApp1.iscWindow11Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture81Done


def iscSetCanvasPicture82():
 thisiscApp1.iscWindow11Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture82Done


def iscIfThen83():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture92()
  #iscIfThen83True

  pass
 else:
  iscIfThen84()
  #iscIfThen83False

  pass

def iscIfThen84():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture93()
  #iscIfThen84True

  pass
 else:
  iscIfThen85()
  #iscIfThen84False

  pass

def iscIfThen85():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture94()
  #iscIfThen85True

  pass
 else:
  iscIfThen86()
  #iscIfThen85False

  pass

def iscIfThen86():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture95()
  #iscIfThen86True

  pass
 else:
  iscIfThen87()
  #iscIfThen86False

  pass

def iscIfThen87():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture96()
  #iscIfThen87True

  pass
 else:
  iscIfThen88()
  #iscIfThen87False

  pass

def iscIfThen88():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture97()
  #iscIfThen88True

  pass
 else:
  iscIfThen89()
  #iscIfThen88False

  pass

def iscIfThen89():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture98()
  #iscIfThen89True

  pass
 else:
  iscIfThen90()
  #iscIfThen89False

  pass

def iscIfThen90():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture99()
  #iscIfThen90True

  pass
 else:
  iscSetLabel100()
  #iscIfThen90False

  pass

def iscSetCanvasPicture91():
 thisiscApp1.iscWindow11Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture91Done


def iscSetCanvasPicture92():
 thisiscApp1.iscWindow11Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture92Done


def iscSetCanvasPicture93():
 thisiscApp1.iscWindow11Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture93Done


def iscSetCanvasPicture94():
 thisiscApp1.iscWindow11Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture94Done


def iscSetCanvasPicture95():
 thisiscApp1.iscWindow11Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture95Done


def iscSetCanvasPicture96():
 thisiscApp1.iscWindow11Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture96Done


def iscSetCanvasPicture97():
 thisiscApp1.iscWindow11Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture97Done


def iscSetCanvasPicture98():
 thisiscApp1.iscWindow11Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture98Done


def iscSetCanvasPicture99():
 thisiscApp1.iscWindow11Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture99Done


def iscSetLabel100():
 thisiscApp1.iscWindow11Label0.set_label(thisiscApp1.iscVerror)
 #iscSetLabel100Done


def iscPortalDeparture20():
 iscPortalDestination38()
 #iscPortalDeparture20Done


def iscPortalDeparture33():
 iscPortalDestination38()
 #iscPortalDeparture33Done


def iscPortalDestination38():
 iscGetDiceText41()
 #iscPortalDestination38Arrived


def iscPortalDeparture25():
 iscPortalDestination38()
 #iscPortalDeparture25Done


def iscPortalDeparture17():
 iscPortalDestination38()
 #iscPortalDeparture17Done


def iscAppQuit7():
 thisiscApp1.destroy(None,None)
 #iscAppQuit7Done


def iscWindow11():
 thisiscApp1.iscWindow11Die10 = gtk.Image()
 thisiscApp1.iscWindow11Die20 = gtk.Image()
 thisiscApp1.iscWindow11Roll0 = gtk.Button("Roll")
 thisiscApp1.iscWindow11test10 = gtk.Entry()
 thisiscApp1.iscWindow11test20 = gtk.Entry()
 thisiscApp1.iscWindow11die00 = gtk.Image()
 thisiscApp1.iscWindow11Label0 =gtk.Label("Hand")
 thisiscApp1.iscWindow11Test00 = gtk.Entry()
 thisiscApp1.iscWindow11Score0 = gtk.Button("Score Hand")
 thisiscApp1.iscWindow11Pass0 = gtk.Button("Pass")
 thisiscApp1.iscWindow11Brains0 =gtk.Label("Brains")
 thisiscApp1.iscWindow11Shots0 =gtk.Label("Shots")
 thisiscApp1.iscWindow11getdice0 = gtk.Button("get dice")
 thisiscApp1.iscWindow11dialog2 = gtk.Entry()
 thisiscApp1.iscWindow11Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow11Window1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow11Window1.set_title("Window")
 thisiscApp1.iscWindow11Window1.set_default_size(640, 480)
 thisiscApp1.iscWindow11Window1.add(thisiscApp1.iscWindow11Window1Fixed)
 thisiscApp1.iscWindow11Window1Fixed.width = 640
 thisiscApp1.iscWindow11Window1Fixed.height = 480
 thisiscApp1.iscWindow11Window1.connect("delete_event", iscWindow11Closed)
 thisiscApp1.iscWindow11Window1.set_resizable(False)
 thisiscApp1.iscWindow11Window1Fixed.show()
 iscWindow11Die10EventBox = gtk.EventBox()
 iscWindow11Die10EventBox.set_size_request(60, 60)
 iscWindow11Die10EventBox.connect("button_press_event", iscWindow11Die1Clicked)
 thisiscApp1.iscWindow11Die10.set_size_request(60, 60)
 iscWindow11Die10EventBox.add(thisiscApp1.iscWindow11Die10)
 thisiscApp1.iscWindow11Window1Fixed.put(iscWindow11Die10EventBox, 140, 150)
 thisiscApp1.iscWindow11Die10.show()
 iscWindow11Die10EventBox.show()
 iscWindow11Die20EventBox = gtk.EventBox()
 iscWindow11Die20EventBox.set_size_request(60, 60)
 iscWindow11Die20EventBox.connect("button_press_event", iscWindow11Die2Clicked)
 thisiscApp1.iscWindow11Die20.set_size_request(60, 60)
 iscWindow11Die20EventBox.add(thisiscApp1.iscWindow11Die20)
 thisiscApp1.iscWindow11Window1Fixed.put(iscWindow11Die20EventBox, 230, 150)
 thisiscApp1.iscWindow11Die20.show()
 iscWindow11Die20EventBox.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11Roll0, 29, 237)
 thisiscApp1.iscWindow11Roll0.set_size_request(80, 26)
 thisiscApp1.iscWindow11Roll0.connect("clicked", iscWindow11RollClicked)
 thisiscApp1.iscWindow11Roll0.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11test10, 228, 249)
 thisiscApp1.iscWindow11test10.set_text("test box")
 thisiscApp1.iscWindow11test10.set_size_request(132, 27)
 thisiscApp1.iscWindow11test10.connect("changed", iscWindow11test1Changed)
 thisiscApp1.iscWindow11test10.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11test20, 231, 282)
 thisiscApp1.iscWindow11test20.set_text("TextBox")
 thisiscApp1.iscWindow11test20.set_size_request(132, 25)
 thisiscApp1.iscWindow11test20.connect("changed", iscWindow11test2Changed)
 thisiscApp1.iscWindow11test20.show()
 iscWindow11die00EventBox = gtk.EventBox()
 iscWindow11die00EventBox.set_size_request(60, 60)
 iscWindow11die00EventBox.connect("button_press_event", iscWindow11die0Clicked)
 thisiscApp1.iscWindow11die00.set_size_request(60, 60)
 iscWindow11die00EventBox.add(thisiscApp1.iscWindow11die00)
 thisiscApp1.iscWindow11Window1Fixed.put(iscWindow11die00EventBox, 50, 150)
 thisiscApp1.iscWindow11die00.show()
 iscWindow11die00EventBox.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11Label0, 145, 120)
 thisiscApp1.iscWindow11Label0.set_size_request(45, 18)
 thisiscApp1.iscWindow11Label0.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11Test00, 228, 219)
 thisiscApp1.iscWindow11Test00.set_text("Textbox0")
 thisiscApp1.iscWindow11Test00.set_size_request(130, 25)
 thisiscApp1.iscWindow11Test00.connect("changed", iscWindow11Test0Changed)
 thisiscApp1.iscWindow11Test00.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11Score0, 27, 279)
 thisiscApp1.iscWindow11Score0.set_size_request(80, 26)
 thisiscApp1.iscWindow11Score0.connect("clicked", iscWindow11ScoreClicked)
 thisiscApp1.iscWindow11Score0.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11Pass0, 125, 239)
 thisiscApp1.iscWindow11Pass0.set_size_request(80, 26)
 thisiscApp1.iscWindow11Pass0.connect("clicked", iscWindow11PassClicked)
 thisiscApp1.iscWindow11Pass0.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11Brains0, 52, 120)
 thisiscApp1.iscWindow11Brains0.set_size_request(55, 20)
 thisiscApp1.iscWindow11Brains0.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11Shots0, 233, 120)
 thisiscApp1.iscWindow11Shots0.set_size_request(57, 18)
 thisiscApp1.iscWindow11Shots0.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11getdice0, 120, 274)
 thisiscApp1.iscWindow11getdice0.set_size_request(80, 26)
 thisiscApp1.iscWindow11getdice0.connect("clicked", iscWindow11getdiceClicked)
 thisiscApp1.iscWindow11getdice0.show()
 thisiscApp1.iscWindow11Window1Fixed.put(thisiscApp1.iscWindow11dialog2, 60, 17)
 thisiscApp1.iscWindow11dialog2.set_text("dialog")
 thisiscApp1.iscWindow11dialog2.set_size_request(234, 62)
 thisiscApp1.iscWindow11dialog2.connect("changed", iscWindow11dialogChanged)
 thisiscApp1.iscWindow11dialog2.show()
 thisiscApp1.iscWindow11Window1.show()
 iscPortalDeparture17()
 #iscWindow11Opened
 #iscWindow11Done


def iscWindow11Closed(self, other):
 pass
 iscAppQuit7()
 #iscWindow11Closed


def iscWindow11Die1Clicked(widget, event):
 pass
 #iscWindow11Die1Clicked


def iscWindow11Die2Clicked(widget, event):
 pass
 #iscWindow11Die2Clicked


def iscWindow11RollClicked(self):
 pass
 iscRoll_Hand19()
 #iscWindow11RollClicked


def iscWindow11test1Changed(self):
 pass
 #iscWindow11test1Changed


def iscWindow11test2Changed(self):
 pass
 #iscWindow11test2Changed


def iscWindow11die0Clicked(widget, event):
 pass
 #iscWindow11die0Clicked


def iscWindow11Test0Changed(self):
 pass
 #iscWindow11Test0Changed


def iscWindow11ScoreClicked(self):
 pass
 iscScoreHand32()
 #iscWindow11ScoreClicked


def iscWindow11PassClicked(self):
 pass
 #iscWindow11PassClicked


def iscWindow11getdiceClicked(self):
 pass
 iscGet_Hand35()
 #iscWindow11getdiceClicked


def iscWindow11dialogChanged(self):
 pass
 #iscWindow11dialogChanged


def iscWindow12():
 thisiscApp1.iscWindow12addPlayer0 = gtk.Button("Add")
 thisiscApp1.iscWindow12done0 = gtk.Button("Done")
 thisiscApp1.iscWindow12Plist0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow12Pname0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow12Label0 =gtk.Label("Enter your name")
 thisiscApp1.iscWindow12Player1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow12Player1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow12Player1.set_title("Player entry")
 thisiscApp1.iscWindow12Player1.set_default_size(640, 480)
 thisiscApp1.iscWindow12Player1.add(thisiscApp1.iscWindow12Player1Fixed)
 thisiscApp1.iscWindow12Player1Fixed.width = 640
 thisiscApp1.iscWindow12Player1Fixed.height = 480
 thisiscApp1.iscWindow12Player1.connect("delete_event", iscWindow12Closed)
 thisiscApp1.iscWindow12Player1.set_resizable(False)
 thisiscApp1.iscWindow12Player1Fixed.show()
 thisiscApp1.iscWindow12Player1Fixed.put(thisiscApp1.iscWindow12addPlayer0, 104, 129)
 thisiscApp1.iscWindow12addPlayer0.set_size_request(80, 26)
 thisiscApp1.iscWindow12addPlayer0.connect("clicked", iscWindow12addPlayerClicked)
 thisiscApp1.iscWindow12addPlayer0.show()
 thisiscApp1.iscWindow12Player1Fixed.put(thisiscApp1.iscWindow12done0, 105, 171)
 thisiscApp1.iscWindow12done0.set_size_request(80, 26)
 thisiscApp1.iscWindow12done0.connect("clicked", iscWindow12doneClicked)
 thisiscApp1.iscWindow12done0.show()
 thisiscApp1.iscWindow12Player1Fixed.put(thisiscApp1.iscWindow12Plist0, 60, 208)
 thisiscApp1.iscWindow12Plist0.set_size_request(188, 73)
 thisiscApp1.iscWindow12Plist0.show()
 thisiscApp1.iscWindow12Player1Fixed.put(thisiscApp1.iscWindow12Pname0, 38, 48)
 thisiscApp1.iscWindow12Pname0.set_size_request(250, 25)
 thisiscApp1.iscWindow12Pname0.show()
 thisiscApp1.iscWindow12Player1Fixed.put(thisiscApp1.iscWindow12Label0, 62, 20)
 thisiscApp1.iscWindow12Label0.set_size_request(109, 20)
 thisiscApp1.iscWindow12Label0.show()
 thisiscApp1.iscWindow12Player1.show()
 #iscWindow12Opened
 #iscWindow12Done


def iscWindow12Closed(self, other):
 pass
 iscAppQuit7()
 #iscWindow12Closed


def iscWindow12addPlayerClicked(self):
 pass
 iscGetTextField13()
 #iscWindow12addPlayerClicked


def iscWindow12doneClicked(self):
 pass
 iscCloseWindow16()
 #iscWindow12doneClicked


def iscGetTextField13():
 thisiscApp1.iscVCurrentPlayer = thisiscApp1.iscWindow12Pname0.get_buffer().get_text(thisiscApp1.iscWindow12Pname0.get_buffer().get_start_iter(), thisiscApp1.iscWindow12Pname0.get_buffer().get_end_iter())
 iscAddPlayer141()
 #iscGetTextField13Done


def iscAddPlayer141():
 thisiscApp1.iscVPlayers_Group.add_player(thisiscApp1.iscVCurrentPlayer)
 iscSetTextField6()
 #iscAddPlayer141Done

def iscSetTextField6():
 thisiscApp1.iscWindow12Pname0.get_buffer().set_text(thisiscApp1.iscVempty_str)
 iscplayerlist5()
 #iscSetTextField6Done


def iscSetTextField3():
 thisiscApp1.iscWindow12Plist0.get_buffer().set_text(thisiscApp1.iscVtemp)
 #iscSetTextField3Done


def iscplayerlist5():
 thisiscApp1.iscVtemp=thisiscApp1.iscVPlayers_Group.__repr__()
 thisiscApp1.iscVNumberPlayers=len(thisiscApp1.iscVPlayers_Group.player_group)
 iscSetTextField3()
 #iscplayerlist5Done

#EndOfFunctions

thisiscApp1 = iscApp1()

iscinit_zdice15()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()