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
 iscVtemp_num = 0
 iscVempty_str = ""
 iscVNumberPlayers = 0
 iscVCurrentPlayer = ""
 iscVtemp = ""
 iscVhandBrains = 0
 iscVhandShots = 0
 iscVDeadMessage = "You are Dead!"
 iscVtwo = 2
 iscVone = 1
 iscVzero = 0
 iscVdie0text = ""
 iscVhand = ""
 iscVPlayers_Group = ""
 iscVDice_Cup = ""
 iscVisRedshot = "Red shot"
 iscVisGreenshot = "Green shot"
 iscVisRedrun = "Red run"
 iscVisYellowshot = "Yellow shot"
 iscVisYellowrun = "Yellow run"
 iscVisGreenrun = "Green run"
 iscVisRedbrains = "Red brains"
 iscVisYellowbrains = "Yellow brains"
 iscVisGreenBrains = "Green brains"
 iscVdie2text = ""
 iscVdie1text = ""
 iscVgreen = "green"
 iscVdie1 = "die1"
 iscVdie2 = "die2"
 iscVyellow = "yellow"
 iscVred = "red"
 iscVerror = "Error!"
 iscVPlayerup = "Player up is ->"
 iscVonethousand = 1000
 iscWindow15main1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow15main1Fixed = gtk.Fixed()
 iscWindow15Die10 = gtk.Image()
 iscWindow15Die20 = gtk.Image()
 iscWindow15Roll0 = gtk.Button("Roll")
 iscWindow15test10 = gtk.Entry()
 iscWindow15test20 = gtk.Entry()
 iscWindow15die00 = gtk.Image()
 iscWindow15Label0 =gtk.Label("Hand")
 iscWindow15Test00 = gtk.Entry()
 iscWindow15Score0 = gtk.Button("Score Hand")
 iscWindow15Pass0 = gtk.Button("Pass")
 iscWindow15Brains0 =gtk.Label("Brains")
 iscWindow15Shots0 =gtk.Label("Shots")
 iscWindow15getdice0 = gtk.Button("get dice")
 iscWindow15dialog0 = gtk.Entry()
 iscWindow15maindialog0 = gtk.Entry()

 iscWindow112Player1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow112Player1Fixed = gtk.Fixed()
 iscWindow112addPlayer0 = gtk.Button("Add")
 iscWindow112done0 = gtk.Button("Done")
 iscWindow112Plist0 = gtk.TextView(buffer=None)
 iscWindow112Pname0 = gtk.TextView(buffer=None)
 iscWindow112Label0 =gtk.Label("Enter your name")
 iscWindow112Shuffle0 = gtk.Button("Shuffle")
 iscWindow112firstup0 = gtk.Entry()
 iscWindow112Firstup0 =gtk.Label("First up")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()



#EndOfClass

def iscScoreHand12():
 if thisiscApp1.iscVhand.score():
  iscgetHandShots14()
  #iscScoreHand12Alive
 else:
  iscSetTextBox2()
  #iscScoreHand12Dead
def iscWindow15():
 thisiscApp1.iscWindow15Die10 = gtk.Image()
 thisiscApp1.iscWindow15Die20 = gtk.Image()
 thisiscApp1.iscWindow15Roll0 = gtk.Button("Roll")
 thisiscApp1.iscWindow15test10 = gtk.Entry()
 thisiscApp1.iscWindow15test20 = gtk.Entry()
 thisiscApp1.iscWindow15die00 = gtk.Image()
 thisiscApp1.iscWindow15Label0 =gtk.Label("Hand")
 thisiscApp1.iscWindow15Test00 = gtk.Entry()
 thisiscApp1.iscWindow15Score0 = gtk.Button("Score Hand")
 thisiscApp1.iscWindow15Pass0 = gtk.Button("Pass")
 thisiscApp1.iscWindow15Brains0 =gtk.Label("Brains")
 thisiscApp1.iscWindow15Shots0 =gtk.Label("Shots")
 thisiscApp1.iscWindow15getdice0 = gtk.Button("get dice")
 thisiscApp1.iscWindow15dialog0 = gtk.Entry()
 thisiscApp1.iscWindow15maindialog0 = gtk.Entry()
 thisiscApp1.iscWindow15main1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow15main1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow15main1.set_title("Z_dice")
 thisiscApp1.iscWindow15main1.set_default_size(640, 480)
 thisiscApp1.iscWindow15main1.add(thisiscApp1.iscWindow15main1Fixed)
 thisiscApp1.iscWindow15main1Fixed.width = 640
 thisiscApp1.iscWindow15main1Fixed.height = 480
 thisiscApp1.iscWindow15main1.connect("delete_event", iscWindow15Closed)
 thisiscApp1.iscWindow15main1.set_resizable(False)
 thisiscApp1.iscWindow15main1Fixed.show()
 iscWindow15Die10EventBox = gtk.EventBox()
 iscWindow15Die10EventBox.set_size_request(60, 60)
 iscWindow15Die10EventBox.connect("button_press_event", iscWindow15Die1Clicked)
 thisiscApp1.iscWindow15Die10.set_size_request(60, 60)
 iscWindow15Die10EventBox.add(thisiscApp1.iscWindow15Die10)
 thisiscApp1.iscWindow15main1Fixed.put(iscWindow15Die10EventBox, 140, 150)
 thisiscApp1.iscWindow15Die10.show()
 iscWindow15Die10EventBox.show()
 iscWindow15Die20EventBox = gtk.EventBox()
 iscWindow15Die20EventBox.set_size_request(60, 60)
 iscWindow15Die20EventBox.connect("button_press_event", iscWindow15Die2Clicked)
 thisiscApp1.iscWindow15Die20.set_size_request(60, 60)
 iscWindow15Die20EventBox.add(thisiscApp1.iscWindow15Die20)
 thisiscApp1.iscWindow15main1Fixed.put(iscWindow15Die20EventBox, 230, 150)
 thisiscApp1.iscWindow15Die20.show()
 iscWindow15Die20EventBox.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15Roll0, 32, 256)
 thisiscApp1.iscWindow15Roll0.set_size_request(80, 26)
 thisiscApp1.iscWindow15Roll0.connect("clicked", iscWindow15RollClicked)
 thisiscApp1.iscWindow15Roll0.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15test10, 228, 249)
 thisiscApp1.iscWindow15test10.set_text("test box")
 thisiscApp1.iscWindow15test10.set_size_request(132, 27)
 thisiscApp1.iscWindow15test10.connect("changed", iscWindow15test1Changed)
 thisiscApp1.iscWindow15test10.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15test20, 231, 282)
 thisiscApp1.iscWindow15test20.set_text("TextBox")
 thisiscApp1.iscWindow15test20.set_size_request(132, 25)
 thisiscApp1.iscWindow15test20.connect("changed", iscWindow15test2Changed)
 thisiscApp1.iscWindow15test20.show()
 iscWindow15die00EventBox = gtk.EventBox()
 iscWindow15die00EventBox.set_size_request(60, 60)
 iscWindow15die00EventBox.connect("button_press_event", iscWindow15die0Clicked)
 thisiscApp1.iscWindow15die00.set_size_request(60, 60)
 iscWindow15die00EventBox.add(thisiscApp1.iscWindow15die00)
 thisiscApp1.iscWindow15main1Fixed.put(iscWindow15die00EventBox, 50, 150)
 thisiscApp1.iscWindow15die00.show()
 iscWindow15die00EventBox.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15Label0, 145, 120)
 thisiscApp1.iscWindow15Label0.set_size_request(45, 18)
 thisiscApp1.iscWindow15Label0.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15Test00, 228, 219)
 thisiscApp1.iscWindow15Test00.set_text("Textbox0")
 thisiscApp1.iscWindow15Test00.set_size_request(130, 25)
 thisiscApp1.iscWindow15Test00.connect("changed", iscWindow15Test0Changed)
 thisiscApp1.iscWindow15Test00.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15Score0, 29, 291)
 thisiscApp1.iscWindow15Score0.set_size_request(80, 26)
 thisiscApp1.iscWindow15Score0.connect("clicked", iscWindow15ScoreClicked)
 thisiscApp1.iscWindow15Score0.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15Pass0, 130, 281)
 thisiscApp1.iscWindow15Pass0.set_size_request(80, 26)
 thisiscApp1.iscWindow15Pass0.connect("clicked", iscWindow15PassClicked)
 thisiscApp1.iscWindow15Pass0.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15Brains0, 52, 120)
 thisiscApp1.iscWindow15Brains0.set_size_request(55, 20)
 thisiscApp1.iscWindow15Brains0.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15Shots0, 233, 120)
 thisiscApp1.iscWindow15Shots0.set_size_request(57, 18)
 thisiscApp1.iscWindow15Shots0.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15getdice0, 31, 222)
 thisiscApp1.iscWindow15getdice0.set_size_request(80, 26)
 thisiscApp1.iscWindow15getdice0.connect("clicked", iscWindow15getdiceClicked)
 thisiscApp1.iscWindow15getdice0.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15dialog0, 61, -105)
 thisiscApp1.iscWindow15dialog0.set_text("dialog")
 thisiscApp1.iscWindow15dialog0.set_size_request(234, 62)
 thisiscApp1.iscWindow15dialog0.connect("changed", iscWindow15dialogChanged)
 thisiscApp1.iscWindow15dialog0.show()
 thisiscApp1.iscWindow15main1Fixed.put(thisiscApp1.iscWindow15maindialog0, 52, 12)
 thisiscApp1.iscWindow15maindialog0.set_text("TextBox")
 thisiscApp1.iscWindow15maindialog0.set_size_request(240, 92)
 thisiscApp1.iscWindow15maindialog0.connect("changed", iscWindow15maindialogChanged)
 thisiscApp1.iscWindow15maindialog0.show()
 thisiscApp1.iscWindow15main1.show()
 iscCombineText218()
 #iscWindow15Opened
 #iscWindow15Done


def iscWindow15Closed(self, other):
 pass
 iscAppQuit72()
 #iscWindow15Closed


def iscWindow15Die1Clicked(widget, event):
 pass
 #iscWindow15Die1Clicked


def iscWindow15Die2Clicked(widget, event):
 pass
 #iscWindow15Die2Clicked


def iscWindow15RollClicked(self):
 pass
 iscRoll_Hand19()
 #iscWindow15RollClicked


def iscWindow15test1Changed(self):
 pass
 #iscWindow15test1Changed


def iscWindow15test2Changed(self):
 pass
 #iscWindow15test2Changed


def iscWindow15die0Clicked(widget, event):
 pass
 #iscWindow15die0Clicked


def iscWindow15Test0Changed(self):
 pass
 #iscWindow15Test0Changed


def iscWindow15ScoreClicked(self):
 pass
 iscScoreHand12()
 #iscWindow15ScoreClicked


def iscWindow15PassClicked(self):
 pass
 iscBank_Brains22()
 #iscWindow15PassClicked


def iscWindow15getdiceClicked(self):
 pass
 iscGet_Hand59()
 #iscWindow15getdiceClicked


def iscWindow15dialogChanged(self):
 pass
 #iscWindow15dialogChanged


def iscWindow15maindialogChanged(self):
 pass
 #iscWindow15maindialogChanged


def iscSetCanvasPicture23():
 thisiscApp1.iscWindow15die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture23Done


def iscSetCanvasPicture24():
 thisiscApp1.iscWindow15die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture24Done


def iscSetCanvasPicture25():
 thisiscApp1.iscWindow15die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture25Done


def iscSetCanvasPicture26():
 thisiscApp1.iscWindow15die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture26Done


def iscSetCanvasPicture27():
 thisiscApp1.iscWindow15die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture27Done


def iscSetCanvasPicture28():
 thisiscApp1.iscWindow15die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture28Done


def iscSetCanvasPicture29():
 thisiscApp1.iscWindow15die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture29Done


def iscSetCanvasPicture30():
 thisiscApp1.iscWindow15die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture30Done


def iscSetCanvasPicture31():
 thisiscApp1.iscWindow15Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture31Done


def iscSetCanvasPicture32():
 thisiscApp1.iscWindow15Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture32Done


def iscSetCanvasPicture33():
 thisiscApp1.iscWindow15Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture33Done


def iscSetCanvasPicture34():
 thisiscApp1.iscWindow15Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture34Done


def iscSetCanvasPicture35():
 thisiscApp1.iscWindow15Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture35Done


def iscSetCanvasPicture36():
 thisiscApp1.iscWindow15Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture36Done


def iscSetCanvasPicture37():
 thisiscApp1.iscWindow15Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture37Done


def iscSetCanvasPicture38():
 thisiscApp1.iscWindow15Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture38Done


def iscSetCanvasPicture39():
 thisiscApp1.iscWindow15Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture39Done


def iscSetLabel40():
 thisiscApp1.iscWindow15Label0.set_label(thisiscApp1.iscVerror)
 #iscSetLabel40Done


def iscSetCanvasPicture41():
 thisiscApp1.iscWindow15die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture41Done


def iscSetCanvasPicture42():
 thisiscApp1.iscWindow15Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture42Done


def iscSetCanvasPicture43():
 thisiscApp1.iscWindow15Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture43Done


def iscSetCanvasPicture44():
 thisiscApp1.iscWindow15Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture44Done


def iscSetCanvasPicture45():
 thisiscApp1.iscWindow15Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture45Done


def iscSetCanvasPicture46():
 thisiscApp1.iscWindow15Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture46Done


def iscSetCanvasPicture47():
 thisiscApp1.iscWindow15Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture47Done


def iscSetCanvasPicture48():
 thisiscApp1.iscWindow15Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture48Done


def iscSetCanvasPicture49():
 thisiscApp1.iscWindow15Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture49Done


def iscSetCanvasPicture50():
 thisiscApp1.iscWindow15Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture50Done


def iscSetCanvasPicture51():
 thisiscApp1.iscWindow15Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture51Done


def iscSetCanvasPicture52():
 thisiscApp1.iscWindow15Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture52Done


def iscSetCanvasPicture53():
 thisiscApp1.iscWindow15die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture53Done


def iscIfThen75():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture44()
  #iscIfThen75True

  pass
 else:
  iscSetLabel40()
  #iscIfThen75False

  pass

def iscIfThen76():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture45()
  #iscIfThen76True

  pass
 else:
  iscIfThen75()
  #iscIfThen76False

  pass

def iscIfThen77():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture46()
  #iscIfThen77True

  pass
 else:
  iscIfThen76()
  #iscIfThen77False

  pass

def iscIfThen78():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture47()
  #iscIfThen78True

  pass
 else:
  iscIfThen77()
  #iscIfThen78False

  pass

def iscIfThen79():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture48()
  #iscIfThen79True

  pass
 else:
  iscIfThen78()
  #iscIfThen79False

  pass

def iscIfThen80():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture49()
  #iscIfThen80True

  pass
 else:
  iscIfThen79()
  #iscIfThen80False

  pass

def iscIfThen81():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture50()
  #iscIfThen81True

  pass
 else:
  iscIfThen80()
  #iscIfThen81False

  pass

def iscIfThen82():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture51()
  #iscIfThen82True

  pass
 else:
  iscIfThen81()
  #iscIfThen82False

  pass

def iscIfThen83():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture39()
  #iscIfThen83True

  pass
 else:
  iscSetLabel40()
  #iscIfThen83False

  pass

def iscIfThen84():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture38()
  #iscIfThen84True

  pass
 else:
  iscIfThen83()
  #iscIfThen84False

  pass

def iscIfThen85():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture37()
  #iscIfThen85True

  pass
 else:
  iscIfThen84()
  #iscIfThen85False

  pass

def iscIfThen86():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture36()
  #iscIfThen86True

  pass
 else:
  iscIfThen85()
  #iscIfThen86False

  pass

def iscIfThen87():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture35()
  #iscIfThen87True

  pass
 else:
  iscIfThen86()
  #iscIfThen87False

  pass

def iscIfThen88():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture33()
  #iscIfThen88True

  pass
 else:
  iscIfThen92()
  #iscIfThen88False

  pass

def iscIfThen89():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture32()
  #iscIfThen89True

  pass
 else:
  iscIfThen88()
  #iscIfThen89False

  pass

def iscIfThen90():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture52()
  #iscIfThen90True

  pass
 else:
  iscIfThen82()
  #iscIfThen90False

  pass

def iscIfThen91():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture31()
  #iscIfThen91True

  pass
 else:
  iscIfThen89()
  #iscIfThen91False

  pass

def iscIfThen92():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture34()
  #iscIfThen92True

  pass
 else:
  iscIfThen87()
  #iscIfThen92False

  pass

def iscIfThen93():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture30()
  #iscIfThen93True

  pass
 else:
  iscSetLabel40()
  #iscIfThen93False

  pass

def iscIfThen94():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture29()
  #iscIfThen94True

  pass
 else:
  iscIfThen93()
  #iscIfThen94False

  pass

def iscIfThen95():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture28()
  #iscIfThen95True

  pass
 else:
  iscIfThen94()
  #iscIfThen95False

  pass

def iscIfThen96():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture26()
  #iscIfThen96True

  pass
 else:
  iscIfThen95()
  #iscIfThen96False

  pass

def iscIfThen97():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture27()
  #iscIfThen97True

  pass
 else:
  iscIfThen96()
  #iscIfThen97False

  pass

def iscIfThen98():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture25()
  #iscIfThen98True

  pass
 else:
  iscIfThen97()
  #iscIfThen98False

  pass

def iscIfThen99():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture24()
  #iscIfThen99True

  pass
 else:
  iscIfThen98()
  #iscIfThen99False

  pass

def iscIfThen100():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture23()
  #iscIfThen100True

  pass
 else:
  iscIfThen99()
  #iscIfThen100False

  pass

def iscIfThen101():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture53()
  #iscIfThen101True

  pass
 else:
  iscIfThen100()
  #iscIfThen101False

  pass

def iscGetDiceText103():
 if thisiscApp1.iscVtwo  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVtwo]
  thisiscApp1.iscVdie2text = d.__repr__()
  iscIfThen90()
  #iscGetDiceText103text done
 else:
  thisiscApp1.iscVdie2text = "blank"
  iscSetCanvasPicture43()
  #iscGetDiceText103blank

def iscGetDiceText105():
 if thisiscApp1.iscVzero  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVzero]
  thisiscApp1.iscVdie0text = d.__repr__()
  iscGetDiceText107()
  iscIfThen101()
  #iscGetDiceText105text done
 else:
  thisiscApp1.iscVdie0text = "blank"
  iscSetCanvasPicture41()
  iscSetCanvasPicture42()
  iscSetCanvasPicture43()
  #iscGetDiceText105blank

def iscGetDiceText107():
 if thisiscApp1.iscVone  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVone]
  thisiscApp1.iscVdie1text = d.__repr__()
  iscIfThen91()
  iscGetDiceText103()
  #iscGetDiceText107text done
 else:
  thisiscApp1.iscVdie1text = "blank"
  iscSetCanvasPicture42()
  iscSetCanvasPicture43()
  #iscGetDiceText107blank

def iscWindow112():
 thisiscApp1.iscWindow112addPlayer0 = gtk.Button("Add")
 thisiscApp1.iscWindow112done0 = gtk.Button("Done")
 thisiscApp1.iscWindow112Plist0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow112Pname0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow112Label0 =gtk.Label("Enter your name")
 thisiscApp1.iscWindow112Shuffle0 = gtk.Button("Shuffle")
 thisiscApp1.iscWindow112firstup0 = gtk.Entry()
 thisiscApp1.iscWindow112Firstup0 =gtk.Label("First up")
 thisiscApp1.iscWindow112Player1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow112Player1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow112Player1.set_title("Player entry")
 thisiscApp1.iscWindow112Player1.set_default_size(707, 471)
 thisiscApp1.iscWindow112Player1.add(thisiscApp1.iscWindow112Player1Fixed)
 thisiscApp1.iscWindow112Player1Fixed.width = 707
 thisiscApp1.iscWindow112Player1Fixed.height = 471
 thisiscApp1.iscWindow112Player1.connect("delete_event", iscWindow112Closed)
 thisiscApp1.iscWindow112Player1.set_resizable(False)
 thisiscApp1.iscWindow112Player1Fixed.show()
 thisiscApp1.iscWindow112Player1Fixed.put(thisiscApp1.iscWindow112addPlayer0, 37, 84)
 thisiscApp1.iscWindow112addPlayer0.set_size_request(80, 26)
 thisiscApp1.iscWindow112addPlayer0.connect("clicked", iscWindow112addPlayerClicked)
 thisiscApp1.iscWindow112addPlayer0.show()
 thisiscApp1.iscWindow112Player1Fixed.put(thisiscApp1.iscWindow112done0, 243, 247)
 thisiscApp1.iscWindow112done0.set_size_request(80, 26)
 thisiscApp1.iscWindow112done0.connect("clicked", iscWindow112doneClicked)
 thisiscApp1.iscWindow112done0.show()
 thisiscApp1.iscWindow112Player1Fixed.put(thisiscApp1.iscWindow112Plist0, 14, 127)
 thisiscApp1.iscWindow112Plist0.set_size_request(189, 147)
 thisiscApp1.iscWindow112Plist0.show()
 thisiscApp1.iscWindow112Player1Fixed.put(thisiscApp1.iscWindow112Pname0, 38, 48)
 thisiscApp1.iscWindow112Pname0.set_size_request(250, 25)
 thisiscApp1.iscWindow112Pname0.show()
 thisiscApp1.iscWindow112Player1Fixed.put(thisiscApp1.iscWindow112Label0, 42, 22)
 thisiscApp1.iscWindow112Label0.set_size_request(109, 20)
 thisiscApp1.iscWindow112Label0.show()
 thisiscApp1.iscWindow112Player1Fixed.put(thisiscApp1.iscWindow112Shuffle0, 243, 202)
 thisiscApp1.iscWindow112Shuffle0.set_size_request(80, 26)
 thisiscApp1.iscWindow112Shuffle0.connect("clicked", iscWindow112ShuffleClicked)
 thisiscApp1.iscWindow112Shuffle0.show()
 thisiscApp1.iscWindow112Player1Fixed.put(thisiscApp1.iscWindow112firstup0, 243, 164)
 thisiscApp1.iscWindow112firstup0.set_text("")
 thisiscApp1.iscWindow112firstup0.set_size_request(80, 22)
 thisiscApp1.iscWindow112firstup0.connect("changed", iscWindow112firstupChanged)
 thisiscApp1.iscWindow112firstup0.show()
 thisiscApp1.iscWindow112Player1Fixed.put(thisiscApp1.iscWindow112Firstup0, 246, 133)
 thisiscApp1.iscWindow112Firstup0.set_size_request(55, 18)
 thisiscApp1.iscWindow112Firstup0.show()
 thisiscApp1.iscWindow112Player1.show()
 #iscWindow112Opened
 #iscWindow112Done


def iscWindow112Closed(self, other):
 pass
 iscAppQuit72()
 #iscWindow112Closed


def iscWindow112addPlayerClicked(self):
 pass
 iscGetTextField66()
 #iscWindow112addPlayerClicked


def iscWindow112doneClicked(self):
 pass
 iscCloseWindow113()
 #iscWindow112doneClicked


def iscWindow112ShuffleClicked(self):
 pass
 iscShufflePlayers71()
 #iscWindow112ShuffleClicked


def iscWindow112firstupChanged(self):
 pass
 #iscWindow112firstupChanged


def iscCloseWindow113():
 thisiscApp1.iscWindow112Player1.destroy()
 iscWindow15()
 #iscCloseWindow113Done


def iscGetTextField66():
 thisiscApp1.iscVCurrentPlayer = thisiscApp1.iscWindow112Pname0.get_buffer().get_text(thisiscApp1.iscWindow112Pname0.get_buffer().get_start_iter(), thisiscApp1.iscWindow112Pname0.get_buffer().get_end_iter())
 iscAddPlayer65()
 #iscGetTextField66Done


def iscPortalDestination74():
 iscGetDiceText105()
 #iscPortalDestination74Arrived


def iscGet_Hand59():
 thisiscApp1.iscVhand.fill(thisiscApp1.iscVDice_Cup)
 iscPortalDeparture69()
 #iscGet_Hand59Done

def iscPortalDeparture69():
 iscPortalDestination74()
 #iscPortalDeparture69Done


def iscinit_zdice111():
 thisiscApp1.iscVDice_Cup=Dice_Cup()
 thisiscApp1.iscVPlayers_Group=Players_Group()
 thisiscApp1.iscVhand=Hand()

 iscWindow112()
 #iscinit_zdice111Done
def iscBank_Brains22():
 thisiscApp1.iscVCurrentPlayer.brain_count += thisiscApp1.iscVhandBrains
 iscplayerlist10()
 #iscBank_Brains22Done

def iscSetTextBox2():
 thisiscApp1.iscWindow15test10.set_text(thisiscApp1.iscVDeadMessage)
 iscnext_Player318()
 #iscSetTextBox2Done


def iscSetTextField60():
 thisiscApp1.iscWindow112Plist0.get_buffer().set_text(thisiscApp1.iscVtemp)
 iscgetCurrentPlayer68()
 #iscSetTextField60Done


def iscgetCurrentPlayer68():
 thisiscApp1.iscVCurrentPlayer=thisiscApp1.iscVPlayers_Group.group[thisiscApp1.iscVzero]
 iscgetPname115()
 #iscgetCurrentPlayer68Done

def iscgetPname115():
 thisiscApp1.iscVtemp = thisiscApp1.iscVCurrentPlayer.name
 thisiscApp1.iscVhandBrains = thisiscApp1.iscVCurrentPlayer.brain_count
 iscSetTextBox116()
 #iscgetPname115Done

def iscSetTextBox116():
 thisiscApp1.iscWindow112firstup0.set_text(thisiscApp1.iscVtemp)
 #iscSetTextBox116Done


def iscAppQuit72():
 thisiscApp1.destroy(None,None)
 #iscAppQuit72Done


def iscgetHandBrains109():
 thisiscApp1.iscVhandBrains=thisiscApp1.iscVhand.brains
 iscConvertNumberToText55()
 #iscgetHandBrains109Done

def iscSetLabel56():
 thisiscApp1.iscWindow15Shots0.set_label(thisiscApp1.iscVtemp)
 iscgetHandBrains109()
 #iscSetLabel56Done


def iscConvertNumberToText57():
 thisiscApp1.iscVtemp = str(thisiscApp1.iscVhandShots)
 iscSetLabel56()
 #iscConvertNumberToText57Done


def iscRoll_Hand19():
 thisiscApp1.iscVhand.roll()
 iscPortalDeparture20()
 #iscRoll_Hand19Rolled

def iscPortalDeparture20():
 iscPortalDestination74()
 #iscPortalDeparture20Done


def iscplayerlist10():
 thisiscApp1.iscVtemp=thisiscApp1.iscVPlayers_Group.__repr__()
 thisiscApp1.iscVNumberPlayers=len(thisiscApp1.iscVPlayers_Group.group)
 iscSetTextBox1()
 #iscplayerlist10Done

def iscSetTextBox1():
 thisiscApp1.iscWindow15maindialog0.set_text(thisiscApp1.iscVtemp)
 iscnext_Player318()
 #iscSetTextBox1Done


def iscgetHandShots14():
 thisiscApp1.iscVhandShots=thisiscApp1.iscVhand.shots
 iscConvertNumberToText57()
 #iscgetHandShots14Done

def iscConvertNumberToText55():
 thisiscApp1.iscVtemp = str(thisiscApp1.iscVhandBrains)
 iscSetLabel54()
 #iscConvertNumberToText55Done


def iscSetLabel54():
 thisiscApp1.iscWindow15Brains0.set_label(thisiscApp1.iscVtemp)
 iscPortalDeparture73()
 #iscSetLabel54Done


def iscPortalDeparture73():
 iscPortalDestination74()
 #iscPortalDeparture73Done


def iscSetTextBox3():
 thisiscApp1.iscWindow15maindialog0.set_text(thisiscApp1.iscVtemp)
 iscPortalDeparture17()
 #iscSetTextBox3Done


def iscPortalDeparture17():
 iscPortalDestination74()
 #iscPortalDeparture17Done


def iscnext_Player318():
 thisiscApp1.iscVCurrentPlayer  = thisiscApp1.iscVPlayers_Group.next(thisiscApp1.iscVPlayers_Group.group.index(thisiscApp1.iscVCurrentPlayer))
 iscgetPname238()
 #iscnext_Player318Done

def iscgetPname238():
 thisiscApp1.iscVtemp = thisiscApp1.iscVCurrentPlayer.name
 thisiscApp1.iscVtemp_num = thisiscApp1.iscVCurrentPlayer.brain_count
 iscCombineText218()
 #iscgetPname238Done

def iscCombineText218():
 thisiscApp1.iscVtemp = thisiscApp1.iscVPlayerup + thisiscApp1.iscVtemp
 iscSetTextBox3()
 #iscCombineText218Done


def iscShufflePlayers71():
 thisiscApp1.iscVPlayers_Group.shuffle()
 iscplayerlist62()
 #iscShufflePlayers71Done

def iscAddPlayer65():
 thisiscApp1.iscVPlayers_Group.add(thisiscApp1.iscVCurrentPlayer)
 iscSetTextField63()
 #iscAddPlayer65Done

def iscSetTextField63():
 thisiscApp1.iscWindow112Pname0.get_buffer().set_text(thisiscApp1.iscVempty_str)
 iscplayerlist62()
 #iscSetTextField63Done


def iscplayerlist62():
 thisiscApp1.iscVtemp=thisiscApp1.iscVPlayers_Group.__repr__()
 thisiscApp1.iscVNumberPlayers=len(thisiscApp1.iscVPlayers_Group.group)
 iscSetTextField60()
 #iscplayerlist62Done

#EndOfFunctions

thisiscApp1 = iscApp1()

iscinit_zdice111()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()