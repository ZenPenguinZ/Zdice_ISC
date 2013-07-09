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
 iscWindow20Player1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow20Player1Fixed = gtk.Fixed()
 iscWindow20addPlayer0 = gtk.Button("Add")
 iscWindow20done0 = gtk.Button("Done")
 iscWindow20Plist0 = gtk.TextView(buffer=None)
 iscWindow20Pname0 = gtk.TextView(buffer=None)
 iscWindow20Label0 =gtk.Label("Enter your name")

 iscWindow38Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow38Window1Fixed = gtk.Fixed()
 iscWindow38Die10 = gtk.Image()
 iscWindow38Die20 = gtk.Image()
 iscWindow38Roll0 = gtk.Button("Roll")
 iscWindow38test10 = gtk.Entry()
 iscWindow38test20 = gtk.Entry()
 iscWindow38die00 = gtk.Image()
 iscWindow38Label0 =gtk.Label("Hand")
 iscWindow38Test00 = gtk.Entry()
 iscWindow38Score0 = gtk.Button("Score Hand")
 iscWindow38Pass0 = gtk.Button("Pass")
 iscWindow38Brains0 =gtk.Label("Brains")
 iscWindow38Shots0 =gtk.Label("Shots")
 iscWindow38getdice0 = gtk.Button("get dice")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()



#EndOfClass

def iscSetLabel48():
 thisiscApp1.iscWindow38Label0.set_label(thisiscApp1.iscVerror)
 #iscSetLabel48Done


def iscSetCanvasPicture96():
 thisiscApp1.iscWindow38Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture96Done


def iscSetCanvasPicture94():
 thisiscApp1.iscWindow38Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture94Done


def iscSetCanvasPicture49():
 thisiscApp1.iscWindow38Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture49Done


def iscSetCanvasPicture50():
 thisiscApp1.iscWindow38Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture50Done


def iscSetCanvasPicture51():
 thisiscApp1.iscWindow38Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture51Done


def iscSetCanvasPicture52():
 thisiscApp1.iscWindow38Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture52Done


def iscSetCanvasPicture53():
 thisiscApp1.iscWindow38Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture53Done


def iscSetCanvasPicture54():
 thisiscApp1.iscWindow38Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture54Done


def iscSetCanvasPicture55():
 thisiscApp1.iscWindow38Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture55Done


def iscIfThen97():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture96()
  #iscIfThen97True

  pass
 else:
  iscSetLabel48()
  #iscIfThen97False

  pass

def iscIfThen95():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture94()
  #iscIfThen95True

  pass
 else:
  iscIfThen97()
  #iscIfThen95False

  pass

def iscIfThen57():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture49()
  #iscIfThen57True

  pass
 else:
  iscIfThen95()
  #iscIfThen57False

  pass

def iscIfThen58():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture50()
  #iscIfThen58True

  pass
 else:
  iscIfThen57()
  #iscIfThen58False

  pass

def iscIfThen59():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture51()
  #iscIfThen59True

  pass
 else:
  iscIfThen58()
  #iscIfThen59False

  pass

def iscIfThen1():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture52()
  #iscIfThen1True

  pass
 else:
  iscIfThen59()
  #iscIfThen1False

  pass

def iscIfThen60():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture53()
  #iscIfThen60True

  pass
 else:
  iscIfThen1()
  #iscIfThen60False

  pass

def iscIfThen56():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture54()
  #iscIfThen56True

  pass
 else:
  iscIfThen60()
  #iscIfThen56False

  pass

def iscSetCanvasPicture61():
 thisiscApp1.iscWindow38Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture61Done


def iscSetCanvasPicture62():
 thisiscApp1.iscWindow38Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture62Done


def iscSetCanvasPicture63():
 thisiscApp1.iscWindow38Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture63Done


def iscSetCanvasPicture64():
 thisiscApp1.iscWindow38Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture64Done


def iscSetCanvasPicture65():
 thisiscApp1.iscWindow38Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture65Done


def iscSetCanvasPicture66():
 thisiscApp1.iscWindow38Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture66Done


def iscSetCanvasPicture67():
 thisiscApp1.iscWindow38Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture67Done


def iscSetCanvasPicture68():
 thisiscApp1.iscWindow38Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture68Done


def iscSetCanvasPicture69():
 thisiscApp1.iscWindow38Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture69Done


def iscIfThen70():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture61()
  #iscIfThen70True

  pass
 else:
  iscSetLabel48()
  #iscIfThen70False

  pass

def iscIfThen93():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture62()
  #iscIfThen93True

  pass
 else:
  iscIfThen70()
  #iscIfThen93False

  pass

def iscIfThen71():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture63()
  #iscIfThen71True

  pass
 else:
  iscIfThen93()
  #iscIfThen71False

  pass

def iscIfThen72():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture64()
  #iscIfThen72True

  pass
 else:
  iscIfThen71()
  #iscIfThen72False

  pass

def iscIfThen73():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture65()
  #iscIfThen73True

  pass
 else:
  iscIfThen72()
  #iscIfThen73False

  pass

def iscIfThen75():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture67()
  #iscIfThen75True

  pass
 else:
  iscIfThen74()
  #iscIfThen75False

  pass

def iscIfThen16():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture68()
  #iscIfThen16True

  pass
 else:
  iscIfThen75()
  #iscIfThen16False

  pass

def iscIfThen2():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture55()
  #iscIfThen2True

  pass
 else:
  iscIfThen56()
  #iscIfThen2False

  pass

def iscIfThen90():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture69()
  #iscIfThen90True

  pass
 else:
  iscIfThen16()
  #iscIfThen90False

  pass

def iscSetCanvasPicture76():
 thisiscApp1.iscWindow38die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture76Done


def iscIfThen74():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture66()
  #iscIfThen74True

  pass
 else:
  iscIfThen73()
  #iscIfThen74False

  pass

def iscSetCanvasPicture78():
 thisiscApp1.iscWindow38die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture78Done


def iscSetCanvasPicture77():
 thisiscApp1.iscWindow38die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture77Done


def iscSetCanvasPicture79():
 thisiscApp1.iscWindow38die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture79Done


def iscSetCanvasPicture80():
 thisiscApp1.iscWindow38die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture80Done


def iscSetCanvasPicture81():
 thisiscApp1.iscWindow38die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture81Done


def iscSetCanvasPicture82():
 thisiscApp1.iscWindow38die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture82Done


def iscSetCanvasPicture83():
 thisiscApp1.iscWindow38die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture83Done


def iscSetCanvasPicture47():
 thisiscApp1.iscWindow38die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture47Done


def iscIfThen91():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture76()
  #iscIfThen91True

  pass
 else:
  iscSetLabel48()
  #iscIfThen91False

  pass

def iscIfThen92():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture78()
  #iscIfThen92True

  pass
 else:
  iscIfThen91()
  #iscIfThen92False

  pass

def iscIfThen89():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture77()
  #iscIfThen89True

  pass
 else:
  iscIfThen92()
  #iscIfThen89False

  pass

def iscIfThen88():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture79()
  #iscIfThen88True

  pass
 else:
  iscIfThen89()
  #iscIfThen88False

  pass

def iscIfThen87():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture80()
  #iscIfThen87True

  pass
 else:
  iscIfThen88()
  #iscIfThen87False

  pass

def iscIfThen86():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture81()
  #iscIfThen86True

  pass
 else:
  iscIfThen87()
  #iscIfThen86False

  pass

def iscIfThen85():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture82()
  #iscIfThen85True

  pass
 else:
  iscIfThen86()
  #iscIfThen85False

  pass

def iscIfThen84():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture83()
  #iscIfThen84True

  pass
 else:
  iscIfThen85()
  #iscIfThen84False

  pass

def iscIfThen17():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture47()
  #iscIfThen17True

  pass
 else:
  iscIfThen84()
  #iscIfThen17False

  pass

def iscGetDiceText44():
 if thisiscApp1.iscVtwo  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVtwo]
  thisiscApp1.iscVdie2text = d.__repr__()
  iscIfThen2()
  #iscGetDiceText44text done
 else:
  thisiscApp1.iscVdie2text = "blank"
  iscSetCanvasPicture39()
  #iscGetDiceText44blank

def iscSetCanvasPicture39():
 thisiscApp1.iscWindow38Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture39Done


def iscSetCanvasPicture40():
 thisiscApp1.iscWindow38Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture40Done


def iscGetDiceText12():
 if thisiscApp1.iscVzero  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVzero]
  thisiscApp1.iscVdie0text = d.__repr__()
  iscGetDiceText42()
  iscIfThen17()
  #iscGetDiceText12text done
 else:
  thisiscApp1.iscVdie0text = "blank"
  iscSetCanvasPicture10()
  iscSetCanvasPicture40()
  iscSetCanvasPicture39()
  #iscGetDiceText12blank

def iscSetCanvasPicture10():
 thisiscApp1.iscWindow38die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture10Done


def iscPortalDestination45():
 iscGetDiceText12()
 #iscPortalDestination45Arrived


def iscGetDiceText42():
 if thisiscApp1.iscVone  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVone]
  thisiscApp1.iscVdie1text = d.__repr__()
  iscIfThen90()
  iscGetDiceText44()
  #iscGetDiceText42text done
 else:
  thisiscApp1.iscVdie1text = "blank"
  iscSetCanvasPicture40()
  iscSetCanvasPicture39()
  #iscGetDiceText42blank

def iscGet_Hand9():
 thisiscApp1.iscVhand.fill(thisiscApp1.iscVDice_Cup)
 iscPortalDeparture7()
 #iscGet_Hand9Done

def iscPortalDeparture7():
 iscPortalDestination45()
 #iscPortalDeparture7Done


def iscScoreHand37():
 if thisiscApp1.iscVhand.score():
  iscgetHandShots35()
  #iscScoreHand37Alive
 else:
  iscSetLabel6()
  #iscScoreHand37Dead
def iscSetLabel6():
 thisiscApp1.iscWindow38Label0.set_label(thisiscApp1.iscVDeadMessage)
 #iscSetLabel6Done


def iscgetHandShots35():
 thisiscApp1.iscVhandShots=thisiscApp1.iscVhand.shots
 iscConvertNumberToText5()
 #iscgetHandShots35Done

def iscConvertNumberToText5():
 thisiscApp1.iscVtemp = str(thisiscApp1.iscVhandShots)
 iscSetLabel33()
 #iscConvertNumberToText5Done


def iscSetLabel14():
 thisiscApp1.iscWindow38Brains0.set_label(thisiscApp1.iscVtemp)
 iscPortalDeparture46()
 #iscSetLabel14Done


def iscPortalDeparture46():
 iscPortalDestination45()
 #iscPortalDeparture46Done


def iscConvertNumberToText15():
 thisiscApp1.iscVtemp = str(thisiscApp1.iscVhandBrains)
 iscSetLabel14()
 #iscConvertNumberToText15Done


def iscgetHandBrains32():
 thisiscApp1.iscVhandBrains=thisiscApp1.iscVhand.brains
 iscConvertNumberToText15()
 #iscgetHandBrains32Done

def iscSetLabel33():
 thisiscApp1.iscWindow38Shots0.set_label(thisiscApp1.iscVtemp)
 iscgetHandBrains32()
 #iscSetLabel33Done


def iscPortalDeparture28():
 iscPortalDestination45()
 #iscPortalDeparture28Done


def iscRoll_Hand30():
 thisiscApp1.iscVhand.roll()
 iscPortalDeparture28()
 #iscRoll_Hand30Rolled

def iscPortalDeparture26():
 iscPortalDestination45()
 #iscPortalDeparture26Done


def iscCloseWindow21():
 thisiscApp1.iscWindow20Player1.destroy()
 iscWindow38()
 #iscCloseWindow21Done


def iscinit_zdice25():
 thisiscApp1.iscVDice_Cup=Dice_Cup()
 thisiscApp1.iscVPlayers_Group=Players_Group()
 thisiscApp1.iscVhand=Hand()

 iscWindow20()
 #iscinit_zdice25Done
def iscGetTextField3():
 thisiscApp1.iscVCurrentPlayer = thisiscApp1.iscWindow20Pname0.get_buffer().get_text(thisiscApp1.iscWindow20Pname0.get_buffer().get_start_iter(), thisiscApp1.iscWindow20Pname0.get_buffer().get_end_iter())
 iscAddPlayer128()
 #iscGetTextField3Done


def iscWindow20():
 thisiscApp1.iscWindow20addPlayer0 = gtk.Button("Add")
 thisiscApp1.iscWindow20done0 = gtk.Button("Done")
 thisiscApp1.iscWindow20Plist0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow20Pname0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow20Label0 =gtk.Label("Enter your name")
 thisiscApp1.iscWindow20Player1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow20Player1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow20Player1.set_title("Player entry")
 thisiscApp1.iscWindow20Player1.set_default_size(640, 480)
 thisiscApp1.iscWindow20Player1.add(thisiscApp1.iscWindow20Player1Fixed)
 thisiscApp1.iscWindow20Player1Fixed.width = 640
 thisiscApp1.iscWindow20Player1Fixed.height = 480
 thisiscApp1.iscWindow20Player1.connect("delete_event", iscWindow20Closed)
 thisiscApp1.iscWindow20Player1.set_resizable(False)
 thisiscApp1.iscWindow20Player1Fixed.show()
 thisiscApp1.iscWindow20Player1Fixed.put(thisiscApp1.iscWindow20addPlayer0, 104, 129)
 thisiscApp1.iscWindow20addPlayer0.set_size_request(80, 26)
 thisiscApp1.iscWindow20addPlayer0.connect("clicked", iscWindow20addPlayerClicked)
 thisiscApp1.iscWindow20addPlayer0.show()
 thisiscApp1.iscWindow20Player1Fixed.put(thisiscApp1.iscWindow20done0, 105, 171)
 thisiscApp1.iscWindow20done0.set_size_request(80, 26)
 thisiscApp1.iscWindow20done0.connect("clicked", iscWindow20doneClicked)
 thisiscApp1.iscWindow20done0.show()
 thisiscApp1.iscWindow20Player1Fixed.put(thisiscApp1.iscWindow20Plist0, 60, 208)
 thisiscApp1.iscWindow20Plist0.set_size_request(188, 73)
 thisiscApp1.iscWindow20Plist0.show()
 thisiscApp1.iscWindow20Player1Fixed.put(thisiscApp1.iscWindow20Pname0, 38, 48)
 thisiscApp1.iscWindow20Pname0.set_size_request(250, 25)
 thisiscApp1.iscWindow20Pname0.show()
 thisiscApp1.iscWindow20Player1Fixed.put(thisiscApp1.iscWindow20Label0, 62, 20)
 thisiscApp1.iscWindow20Label0.set_size_request(109, 20)
 thisiscApp1.iscWindow20Label0.show()
 thisiscApp1.iscWindow20Player1.show()
 #iscWindow20Opened
 #iscWindow20Done


def iscWindow20Closed(self, other):
 pass
 iscPortalDeparture99()
 #iscWindow20Closed


def iscWindow20addPlayerClicked(self):
 pass
 iscGetTextField3()
 #iscWindow20addPlayerClicked


def iscWindow20doneClicked(self):
 pass
 iscCloseWindow21()
 #iscWindow20doneClicked


def iscWindow38():
 thisiscApp1.iscWindow38Die10 = gtk.Image()
 thisiscApp1.iscWindow38Die20 = gtk.Image()
 thisiscApp1.iscWindow38Roll0 = gtk.Button("Roll")
 thisiscApp1.iscWindow38test10 = gtk.Entry()
 thisiscApp1.iscWindow38test20 = gtk.Entry()
 thisiscApp1.iscWindow38die00 = gtk.Image()
 thisiscApp1.iscWindow38Label0 =gtk.Label("Hand")
 thisiscApp1.iscWindow38Test00 = gtk.Entry()
 thisiscApp1.iscWindow38Score0 = gtk.Button("Score Hand")
 thisiscApp1.iscWindow38Pass0 = gtk.Button("Pass")
 thisiscApp1.iscWindow38Brains0 =gtk.Label("Brains")
 thisiscApp1.iscWindow38Shots0 =gtk.Label("Shots")
 thisiscApp1.iscWindow38getdice0 = gtk.Button("get dice")
 thisiscApp1.iscWindow38Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow38Window1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow38Window1.set_title("Window")
 thisiscApp1.iscWindow38Window1.set_default_size(640, 480)
 thisiscApp1.iscWindow38Window1.add(thisiscApp1.iscWindow38Window1Fixed)
 thisiscApp1.iscWindow38Window1Fixed.width = 640
 thisiscApp1.iscWindow38Window1Fixed.height = 480
 thisiscApp1.iscWindow38Window1.connect("delete_event", iscWindow38Closed)
 thisiscApp1.iscWindow38Window1.set_resizable(False)
 thisiscApp1.iscWindow38Window1Fixed.show()
 iscWindow38Die10EventBox = gtk.EventBox()
 iscWindow38Die10EventBox.set_size_request(60, 60)
 iscWindow38Die10EventBox.connect("button_press_event", iscWindow38Die1Clicked)
 thisiscApp1.iscWindow38Die10.set_size_request(60, 60)
 iscWindow38Die10EventBox.add(thisiscApp1.iscWindow38Die10)
 thisiscApp1.iscWindow38Window1Fixed.put(iscWindow38Die10EventBox, 140, 150)
 thisiscApp1.iscWindow38Die10.show()
 iscWindow38Die10EventBox.show()
 iscWindow38Die20EventBox = gtk.EventBox()
 iscWindow38Die20EventBox.set_size_request(60, 60)
 iscWindow38Die20EventBox.connect("button_press_event", iscWindow38Die2Clicked)
 thisiscApp1.iscWindow38Die20.set_size_request(60, 60)
 iscWindow38Die20EventBox.add(thisiscApp1.iscWindow38Die20)
 thisiscApp1.iscWindow38Window1Fixed.put(iscWindow38Die20EventBox, 230, 150)
 thisiscApp1.iscWindow38Die20.show()
 iscWindow38Die20EventBox.show()
 thisiscApp1.iscWindow38Window1Fixed.put(thisiscApp1.iscWindow38Roll0, 29, 237)
 thisiscApp1.iscWindow38Roll0.set_size_request(80, 26)
 thisiscApp1.iscWindow38Roll0.connect("clicked", iscWindow38RollClicked)
 thisiscApp1.iscWindow38Roll0.show()
 thisiscApp1.iscWindow38Window1Fixed.put(thisiscApp1.iscWindow38test10, 228, 249)
 thisiscApp1.iscWindow38test10.set_text("test box")
 thisiscApp1.iscWindow38test10.set_size_request(132, 27)
 thisiscApp1.iscWindow38test10.connect("changed", iscWindow38test1Changed)
 thisiscApp1.iscWindow38test10.show()
 thisiscApp1.iscWindow38Window1Fixed.put(thisiscApp1.iscWindow38test20, 231, 282)
 thisiscApp1.iscWindow38test20.set_text("TextBox")
 thisiscApp1.iscWindow38test20.set_size_request(132, 25)
 thisiscApp1.iscWindow38test20.connect("changed", iscWindow38test2Changed)
 thisiscApp1.iscWindow38test20.show()
 iscWindow38die00EventBox = gtk.EventBox()
 iscWindow38die00EventBox.set_size_request(60, 60)
 iscWindow38die00EventBox.connect("button_press_event", iscWindow38die0Clicked)
 thisiscApp1.iscWindow38die00.set_size_request(60, 60)
 iscWindow38die00EventBox.add(thisiscApp1.iscWindow38die00)
 thisiscApp1.iscWindow38Window1Fixed.put(iscWindow38die00EventBox, 50, 150)
 thisiscApp1.iscWindow38die00.show()
 iscWindow38die00EventBox.show()
 thisiscApp1.iscWindow38Window1Fixed.put(thisiscApp1.iscWindow38Label0, 145, 120)
 thisiscApp1.iscWindow38Label0.set_size_request(45, 18)
 thisiscApp1.iscWindow38Label0.show()
 thisiscApp1.iscWindow38Window1Fixed.put(thisiscApp1.iscWindow38Test00, 228, 219)
 thisiscApp1.iscWindow38Test00.set_text("Textbox0")
 thisiscApp1.iscWindow38Test00.set_size_request(130, 25)
 thisiscApp1.iscWindow38Test00.connect("changed", iscWindow38Test0Changed)
 thisiscApp1.iscWindow38Test00.show()
 thisiscApp1.iscWindow38Window1Fixed.put(thisiscApp1.iscWindow38Score0, 27, 279)
 thisiscApp1.iscWindow38Score0.set_size_request(80, 26)
 thisiscApp1.iscWindow38Score0.connect("clicked", iscWindow38ScoreClicked)
 thisiscApp1.iscWindow38Score0.show()
 thisiscApp1.iscWindow38Window1Fixed.put(thisiscApp1.iscWindow38Pass0, 125, 239)
 thisiscApp1.iscWindow38Pass0.set_size_request(80, 26)
 thisiscApp1.iscWindow38Pass0.connect("clicked", iscWindow38PassClicked)
 thisiscApp1.iscWindow38Pass0.show()
 thisiscApp1.iscWindow38Window1Fixed.put(thisiscApp1.iscWindow38Brains0, 52, 120)
 thisiscApp1.iscWindow38Brains0.set_size_request(55, 20)
 thisiscApp1.iscWindow38Brains0.show()
 thisiscApp1.iscWindow38Window1Fixed.put(thisiscApp1.iscWindow38Shots0, 233, 120)
 thisiscApp1.iscWindow38Shots0.set_size_request(57, 18)
 thisiscApp1.iscWindow38Shots0.show()
 thisiscApp1.iscWindow38Window1Fixed.put(thisiscApp1.iscWindow38getdice0, 120, 274)
 thisiscApp1.iscWindow38getdice0.set_size_request(80, 26)
 thisiscApp1.iscWindow38getdice0.connect("clicked", iscWindow38getdiceClicked)
 thisiscApp1.iscWindow38getdice0.show()
 thisiscApp1.iscWindow38Window1.show()
 iscPortalDeparture26()
 #iscWindow38Opened
 #iscWindow38Done


def iscWindow38Closed(self, other):
 pass
 iscPortalDeparture100()
 #iscWindow38Closed


def iscWindow38Die1Clicked(widget, event):
 pass
 #iscWindow38Die1Clicked


def iscWindow38Die2Clicked(widget, event):
 pass
 #iscWindow38Die2Clicked


def iscWindow38RollClicked(self):
 pass
 iscRoll_Hand30()
 #iscWindow38RollClicked


def iscWindow38test1Changed(self):
 pass
 #iscWindow38test1Changed


def iscWindow38test2Changed(self):
 pass
 #iscWindow38test2Changed


def iscWindow38die0Clicked(widget, event):
 pass
 #iscWindow38die0Clicked


def iscWindow38Test0Changed(self):
 pass
 #iscWindow38Test0Changed


def iscWindow38ScoreClicked(self):
 pass
 iscScoreHand37()
 #iscWindow38ScoreClicked


def iscWindow38PassClicked(self):
 pass
 #iscWindow38PassClicked


def iscWindow38getdiceClicked(self):
 pass
 iscGet_Hand9()
 #iscWindow38getdiceClicked


def iscPortalDestination101():
 iscAppQuit27()
 #iscPortalDestination101Arrived


def iscPortalDeparture100():
 iscPortalDestination101()
 #iscPortalDeparture100Done


def iscPortalDeparture99():
 iscPortalDestination101()
 #iscPortalDeparture99Done


def iscAppQuit27():
 thisiscApp1.destroy(None,None)
 #iscAppQuit27Done


def iscSetTextField4():
 thisiscApp1.iscWindow20Pname0.get_buffer().set_text(thisiscApp1.iscVempty_str)
 iscplayerlist19()
 #iscSetTextField4Done


def iscplayerlist19():
 thisiscApp1.iscVtemp=thisiscApp1.iscVPlayers_Group.__repr__()
 thisiscApp1.iscVNumberPlayers=len(thisiscApp1.iscVPlayers_Group.player_group)
 iscSetTextField13()
 #iscplayerlist19Done

def iscSetTextField13():
 thisiscApp1.iscWindow20Plist0.get_buffer().set_text(thisiscApp1.iscVtemp)
 #iscSetTextField13Done


def iscAddPlayer128():
 thisiscApp1.iscVPlayers_Group.add_player(thisiscApp1.iscVtemp)
 iscSetTextField4()
 #iscAddPlayer128Done

#EndOfFunctions

thisiscApp1 = iscApp1()

iscinit_zdice25()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()