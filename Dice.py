#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gobject
import random
import os
import sys
import gtk
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
 iscWindow4Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow4Window1Fixed = gtk.Fixed()
 iscWindow4Die10 = gtk.Image()
 iscWindow4Die20 = gtk.Image()
 iscWindow4Roll0 = gtk.Button("Roll")
 iscWindow4test10 = gtk.Entry()
 iscWindow4test20 = gtk.Entry()
 iscWindow4die00 = gtk.Image()
 iscWindow4Label0 =gtk.Label("Hand")
 iscWindow4Test00 = gtk.Entry()
 iscWindow4Score2 = gtk.Button("Score Hand")
 iscWindow4Pass3 = gtk.Button("Pass")
 iscWindow4Brains5 =gtk.Label("Brains")
 iscWindow4Shots6 =gtk.Label("Shots")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()



#EndOfClass

def iscSetTextBox1():
 thisiscApp1.iscWindow4test20.set_text(thisiscApp1.iscVdie2text)
 #iscSetTextBox1Done


def iscSetTextBox2():
 thisiscApp1.iscWindow4test10.set_text(thisiscApp1.iscVdie1text)
 #iscSetTextBox2Done


def iscSetTextBox3():
 thisiscApp1.iscWindow4Test00.set_text(thisiscApp1.iscVdie0text)
 #iscSetTextBox3Done


def iscGetDiceText6():
 d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVtwo]
 thisiscApp1.iscVdie2text = d.__repr__()
 iscIfThen35()
 iscSetTextBox1()
 #iscGetDiceText6Done

def iscGetDiceText8():
 d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVone]
 thisiscApp1.iscVdie1text = d.__repr__()
 iscIfThen22()
 iscGetDiceText6()
 iscSetTextBox2()
 #iscGetDiceText8Done

def iscPortalDestination9():
 iscGetDiceText11()
 #iscPortalDestination9Arrived


def iscGetDiceText11():
 d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVzero]
 thisiscApp1.iscVdie0text = d.__repr__()
 iscIfThen29()
 iscGetDiceText8()
 iscSetTextBox3()
 #iscGetDiceText11Done

def iscRoll_Hand14():
 thisiscApp1.iscVhand.roll()
 iscPortalDeparture12()
 #iscRoll_Hand14Rolled

def iscIfThen15():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture16()
  #iscIfThen15True

  pass
 else:
  iscSetLabel77()
  #iscIfThen15False

  pass

def iscSetCanvasPicture16():
 thisiscApp1.iscWindow4Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture16Done


def iscIfThen17():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture18()
  #iscIfThen17True

  pass
 else:
  iscIfThen15()
  #iscIfThen17False

  pass

def iscSetCanvasPicture18():
 thisiscApp1.iscWindow4Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture18Done


def iscIfThen19():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture62()
  #iscIfThen19True

  pass
 else:
  iscIfThen54()
  #iscIfThen19False

  pass

def iscIfThen20():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture45()
  #iscIfThen20True

  pass
 else:
  iscIfThen21()
  #iscIfThen20False

  pass

def iscIfThen21():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture47()
  #iscIfThen21True

  pass
 else:
  iscSetLabel77()
  #iscIfThen21False

  pass

def iscIfThen22():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture55()
  #iscIfThen22True

  pass
 else:
  iscIfThen48()
  #iscIfThen22False

  pass

def iscIfThen23():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture46()
  #iscIfThen23True

  pass
 else:
  iscIfThen20()
  #iscIfThen23False

  pass

def iscIfThen24():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture44()
  #iscIfThen24True

  pass
 else:
  iscIfThen23()
  #iscIfThen24False

  pass

def iscIfThen25():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture43()
  #iscIfThen25True

  pass
 else:
  iscIfThen24()
  #iscIfThen25False

  pass

def iscIfThen26():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture42()
  #iscIfThen26True

  pass
 else:
  iscIfThen25()
  #iscIfThen26False

  pass

def iscIfThen27():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture41()
  #iscIfThen27True

  pass
 else:
  iscIfThen26()
  #iscIfThen27False

  pass

def iscIfThen28():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture40()
  #iscIfThen28True

  pass
 else:
  iscIfThen27()
  #iscIfThen28False

  pass

def iscIfThen29():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture39()
  #iscIfThen29True

  pass
 else:
  iscIfThen28()
  #iscIfThen29False

  pass

def iscAppQuit30():
 thisiscApp1.destroy(None,None)
 #iscAppQuit30Done


def iscGet_Hand32():
 thisiscApp1.iscVhand.fill(thisiscApp1.iscVDice_Cup)
 iscRoll_Hand37()
 #iscGet_Hand32Done

def iscinit_zdice34():
 thisiscApp1.iscVDice_Cup=Dice_Cup()
 thisiscApp1.iscVPlayers_Group=Players_Group()
 thisiscApp1.iscVhand=Hand()

 iscGet_Hand32()
 #iscinit_zdice34Done
def iscIfThen35():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture70()
  #iscIfThen35True

  pass
 else:
  iscIfThen69()
  #iscIfThen35False

  pass

def iscRoll_Hand37():
 thisiscApp1.iscVhand.roll()
 iscPortalDeparture38()
 #iscRoll_Hand37Rolled

def iscPortalDeparture38():
 iscPortalDestination9()
 #iscPortalDeparture38Done


def iscSetCanvasPicture39():
 thisiscApp1.iscWindow4die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture39Done


def iscSetCanvasPicture40():
 thisiscApp1.iscWindow4die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture40Done


def iscSetCanvasPicture41():
 thisiscApp1.iscWindow4die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture41Done


def iscSetCanvasPicture42():
 thisiscApp1.iscWindow4die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture42Done


def iscSetCanvasPicture43():
 thisiscApp1.iscWindow4die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture43Done


def iscSetCanvasPicture44():
 thisiscApp1.iscWindow4die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture44Done


def iscSetCanvasPicture45():
 thisiscApp1.iscWindow4die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture45Done


def iscSetCanvasPicture46():
 thisiscApp1.iscWindow4die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture46Done


def iscSetCanvasPicture47():
 thisiscApp1.iscWindow4die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture47Done


def iscIfThen48():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture56()
  #iscIfThen48True

  pass
 else:
  iscIfThen49()
  #iscIfThen48False

  pass

def iscIfThen49():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture57()
  #iscIfThen49True

  pass
 else:
  iscIfThen50()
  #iscIfThen49False

  pass

def iscIfThen50():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture58()
  #iscIfThen50True

  pass
 else:
  iscIfThen51()
  #iscIfThen50False

  pass

def iscIfThen51():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture59()
  #iscIfThen51True

  pass
 else:
  iscIfThen52()
  #iscIfThen51False

  pass

def iscIfThen52():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture60()
  #iscIfThen52True

  pass
 else:
  iscIfThen53()
  #iscIfThen52False

  pass

def iscIfThen53():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture61()
  #iscIfThen53True

  pass
 else:
  iscIfThen19()
  #iscIfThen53False

  pass

def iscIfThen54():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture63()
  #iscIfThen54True

  pass
 else:
  iscSetLabel77()
  #iscIfThen54False

  pass

def iscSetCanvasPicture55():
 thisiscApp1.iscWindow4Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture55Done


def iscSetCanvasPicture56():
 thisiscApp1.iscWindow4Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture56Done


def iscSetCanvasPicture57():
 thisiscApp1.iscWindow4Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture57Done


def iscSetCanvasPicture58():
 thisiscApp1.iscWindow4Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture58Done


def iscSetCanvasPicture59():
 thisiscApp1.iscWindow4Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture59Done


def iscSetCanvasPicture60():
 thisiscApp1.iscWindow4Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture60Done


def iscSetCanvasPicture61():
 thisiscApp1.iscWindow4Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture61Done


def iscSetCanvasPicture62():
 thisiscApp1.iscWindow4Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture62Done


def iscSetCanvasPicture63():
 thisiscApp1.iscWindow4Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture63Done


def iscIfThen64():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture72()
  #iscIfThen64True

  pass
 else:
  iscIfThen65()
  #iscIfThen64False

  pass

def iscIfThen65():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture73()
  #iscIfThen65True

  pass
 else:
  iscIfThen66()
  #iscIfThen65False

  pass

def iscIfThen66():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture74()
  #iscIfThen66True

  pass
 else:
  iscIfThen67()
  #iscIfThen66False

  pass

def iscIfThen67():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture75()
  #iscIfThen67True

  pass
 else:
  iscIfThen68()
  #iscIfThen67False

  pass

def iscIfThen68():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture76()
  #iscIfThen68True

  pass
 else:
  iscIfThen17()
  #iscIfThen68False

  pass

def iscIfThen69():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture71()
  #iscIfThen69True

  pass
 else:
  iscIfThen64()
  #iscIfThen69False

  pass

def iscSetCanvasPicture70():
 thisiscApp1.iscWindow4Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture70Done


def iscSetCanvasPicture71():
 thisiscApp1.iscWindow4Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture71Done


def iscSetCanvasPicture72():
 thisiscApp1.iscWindow4Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture72Done


def iscSetCanvasPicture73():
 thisiscApp1.iscWindow4Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture73Done


def iscSetCanvasPicture74():
 thisiscApp1.iscWindow4Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture74Done


def iscSetCanvasPicture75():
 thisiscApp1.iscWindow4Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture75Done


def iscSetCanvasPicture76():
 thisiscApp1.iscWindow4Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture76Done


def iscSetLabel77():
 thisiscApp1.iscWindow4Label0.set_label(thisiscApp1.iscVerror)
 #iscSetLabel77Done


def iscPortalDeparture12():
 iscPortalDestination9()
 #iscPortalDeparture12Done


def iscWindow4():
 thisiscApp1.iscWindow4Die10 = gtk.Image()
 thisiscApp1.iscWindow4Die20 = gtk.Image()
 thisiscApp1.iscWindow4Roll0 = gtk.Button("Roll")
 thisiscApp1.iscWindow4test10 = gtk.Entry()
 thisiscApp1.iscWindow4test20 = gtk.Entry()
 thisiscApp1.iscWindow4die00 = gtk.Image()
 thisiscApp1.iscWindow4Label0 =gtk.Label("Hand")
 thisiscApp1.iscWindow4Test00 = gtk.Entry()
 thisiscApp1.iscWindow4Score2 = gtk.Button("Score Hand")
 thisiscApp1.iscWindow4Pass3 = gtk.Button("Pass")
 thisiscApp1.iscWindow4Brains5 =gtk.Label("Brains")
 thisiscApp1.iscWindow4Shots6 =gtk.Label("Shots")
 thisiscApp1.iscWindow4Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow4Window1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow4Window1.set_title("Window")
 thisiscApp1.iscWindow4Window1.set_default_size(480, 640)
 thisiscApp1.iscWindow4Window1.add(thisiscApp1.iscWindow4Window1Fixed)
 thisiscApp1.iscWindow4Window1Fixed.width = 480
 thisiscApp1.iscWindow4Window1Fixed.height = 640
 thisiscApp1.iscWindow4Window1.connect("delete_event", iscWindow4Closed)
 thisiscApp1.iscWindow4Window1.set_resizable(False)
 thisiscApp1.iscWindow4Window1Fixed.show()
 iscWindow4Die10EventBox = gtk.EventBox()
 iscWindow4Die10EventBox.set_size_request(60, 60)
 iscWindow4Die10EventBox.connect("button_press_event", iscWindow4Die1Clicked)
 thisiscApp1.iscWindow4Die10.set_size_request(60, 60)
 iscWindow4Die10EventBox.add(thisiscApp1.iscWindow4Die10)
 thisiscApp1.iscWindow4Window1Fixed.put(iscWindow4Die10EventBox, 140, 150)
 thisiscApp1.iscWindow4Die10.show()
 iscWindow4Die10EventBox.show()
 iscWindow4Die20EventBox = gtk.EventBox()
 iscWindow4Die20EventBox.set_size_request(60, 60)
 iscWindow4Die20EventBox.connect("button_press_event", iscWindow4Die2Clicked)
 thisiscApp1.iscWindow4Die20.set_size_request(60, 60)
 iscWindow4Die20EventBox.add(thisiscApp1.iscWindow4Die20)
 thisiscApp1.iscWindow4Window1Fixed.put(iscWindow4Die20EventBox, 230, 150)
 thisiscApp1.iscWindow4Die20.show()
 iscWindow4Die20EventBox.show()
 thisiscApp1.iscWindow4Window1Fixed.put(thisiscApp1.iscWindow4Roll0, 29, 237)
 thisiscApp1.iscWindow4Roll0.set_size_request(80, 26)
 thisiscApp1.iscWindow4Roll0.connect("clicked", iscWindow4RollClicked)
 thisiscApp1.iscWindow4Roll0.show()
 thisiscApp1.iscWindow4Window1Fixed.put(thisiscApp1.iscWindow4test10, 228, 249)
 thisiscApp1.iscWindow4test10.set_text("test box")
 thisiscApp1.iscWindow4test10.set_size_request(132, 27)
 thisiscApp1.iscWindow4test10.connect("changed", iscWindow4test1Changed)
 thisiscApp1.iscWindow4test10.show()
 thisiscApp1.iscWindow4Window1Fixed.put(thisiscApp1.iscWindow4test20, 231, 282)
 thisiscApp1.iscWindow4test20.set_text("TextBox")
 thisiscApp1.iscWindow4test20.set_size_request(132, 25)
 thisiscApp1.iscWindow4test20.connect("changed", iscWindow4test2Changed)
 thisiscApp1.iscWindow4test20.show()
 iscWindow4die00EventBox = gtk.EventBox()
 iscWindow4die00EventBox.set_size_request(60, 60)
 iscWindow4die00EventBox.connect("button_press_event", iscWindow4die0Clicked)
 thisiscApp1.iscWindow4die00.set_size_request(60, 60)
 iscWindow4die00EventBox.add(thisiscApp1.iscWindow4die00)
 thisiscApp1.iscWindow4Window1Fixed.put(iscWindow4die00EventBox, 50, 150)
 thisiscApp1.iscWindow4die00.show()
 iscWindow4die00EventBox.show()
 thisiscApp1.iscWindow4Window1Fixed.put(thisiscApp1.iscWindow4Label0, 145, 120)
 thisiscApp1.iscWindow4Label0.set_size_request(45, 18)
 thisiscApp1.iscWindow4Label0.show()
 thisiscApp1.iscWindow4Window1Fixed.put(thisiscApp1.iscWindow4Test00, 228, 219)
 thisiscApp1.iscWindow4Test00.set_text("Textbox0")
 thisiscApp1.iscWindow4Test00.set_size_request(130, 25)
 thisiscApp1.iscWindow4Test00.connect("changed", iscWindow4Test0Changed)
 thisiscApp1.iscWindow4Test00.show()
 thisiscApp1.iscWindow4Window1Fixed.put(thisiscApp1.iscWindow4Score2, 30, 279)
 thisiscApp1.iscWindow4Score2.set_size_request(80, 26)
 thisiscApp1.iscWindow4Score2.connect("clicked", iscWindow4ScoreClicked)
 thisiscApp1.iscWindow4Score2.show()
 thisiscApp1.iscWindow4Window1Fixed.put(thisiscApp1.iscWindow4Pass3, 125, 239)
 thisiscApp1.iscWindow4Pass3.set_size_request(80, 26)
 thisiscApp1.iscWindow4Pass3.connect("clicked", iscWindow4PassClicked)
 thisiscApp1.iscWindow4Pass3.show()
 thisiscApp1.iscWindow4Window1Fixed.put(thisiscApp1.iscWindow4Brains5, 52, 120)
 thisiscApp1.iscWindow4Brains5.set_size_request(55, 20)
 thisiscApp1.iscWindow4Brains5.show()
 thisiscApp1.iscWindow4Window1Fixed.put(thisiscApp1.iscWindow4Shots6, 233, 120)
 thisiscApp1.iscWindow4Shots6.set_size_request(57, 18)
 thisiscApp1.iscWindow4Shots6.show()
 thisiscApp1.iscWindow4Window1.show()
 iscinit_zdice34()
 #iscWindow4Opened
 #iscWindow4Done


def iscWindow4Closed(self, other):
 pass
 iscAppQuit30()
 #iscWindow4Closed


def iscWindow4Die1Clicked(widget, event):
 pass
 #iscWindow4Die1Clicked


def iscWindow4Die2Clicked(widget, event):
 pass
 #iscWindow4Die2Clicked


def iscWindow4RollClicked(self):
 pass
 iscRoll_Hand14()
 #iscWindow4RollClicked


def iscWindow4test1Changed(self):
 pass
 #iscWindow4test1Changed


def iscWindow4test2Changed(self):
 pass
 #iscWindow4test2Changed


def iscWindow4die0Clicked(widget, event):
 pass
 #iscWindow4die0Clicked


def iscWindow4Test0Changed(self):
 pass
 #iscWindow4Test0Changed


def iscWindow4ScoreClicked(self):
 pass
 iscScoreHand96()
 #iscWindow4ScoreClicked


def iscWindow4PassClicked(self):
 pass
 #iscWindow4PassClicked


def iscSetLabel97():
 thisiscApp1.iscWindow4Label0.set_label(thisiscApp1.iscVDeadMessage)
 #iscSetLabel97Done


def iscSetLabel98():
 thisiscApp1.iscWindow4Label0.set_label(thisiscApp1.iscVisGreenBrains)
 iscPortalDeparture12()
 #iscSetLabel98Done


def iscScoreHand96():
 if thisiscApp1.iscVhand.score():
  iscgetHandShots129()
  #iscScoreHand96Alive
 else:
  iscSetLabel97()
  #iscScoreHand96Dead
def iscgetHandShots129():
 thisiscApp1.iscVhandShots=thisiscApp1.iscVhand.shots
 iscgetHandBrains131()
 #iscgetHandShots129Done

def iscgetHandBrains131():
 thisiscApp1.iscVhandBrains=thisiscApp1.iscVhand.brains
 iscSetLabel98()
 #iscgetHandBrains131Done

#EndOfFunctions

thisiscApp1 = iscApp1()

iscWindow4()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()