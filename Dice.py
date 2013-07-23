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
 iscVonethousand = 1000
 iscVPlayerup = "Player up is ->"
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
 iscVtemp_num = 0
 iscWindow48Player1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow48Player1Fixed = gtk.Fixed()
 iscWindow48addPlayer0 = gtk.Button("Add")
 iscWindow48done0 = gtk.Button("Done")
 iscWindow48Plist0 = gtk.TextView(buffer=None)
 iscWindow48Pname0 = gtk.TextView(buffer=None)
 iscWindow48Label0 =gtk.Label("Enter your name")
 iscWindow48Shuffle0 = gtk.Button("Shuffle")
 iscWindow48firstup0 = gtk.Entry()
 iscWindow48Firstup0 =gtk.Label("First up")

 iscWindow113main1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow113main1Fixed = gtk.Fixed()
 iscWindow113Die10 = gtk.Image()
 iscWindow113Die20 = gtk.Image()
 iscWindow113Roll0 = gtk.Button("Roll")
 iscWindow113test10 = gtk.Entry()
 iscWindow113test20 = gtk.Entry()
 iscWindow113die00 = gtk.Image()
 iscWindow113Label0 =gtk.Label("Hand")
 iscWindow113playerup0 = gtk.Entry()
 iscWindow113Score0 = gtk.Button("Score Hand")
 iscWindow113Pass0 = gtk.Button("Pass")
 iscWindow113Brains0 =gtk.Label("Brains")
 iscWindow113Shots0 =gtk.Label("Shots")
 iscWindow113getdice0 = gtk.Button("get dice")
 iscWindow113dialog0 = gtk.Entry()
 iscWindow113maindialog0 = gtk.Entry()
 iscWindow113Playerup2 =gtk.Label("Player up ->")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()



#EndOfClass

def iscAddPlayer5():
 thisiscApp1.iscVPlayers_Group.add(thisiscApp1.iscVCurrentPlayer)
 iscSetTextField3()
 #iscAddPlayer5Done

def iscShufflePlayers7():
 thisiscApp1.iscVPlayers_Group.shuffle()
 iscplayerlist2()
 #iscShufflePlayers7Done

def iscPortalDeparture13():
 iscPortalDestination45()
 #iscPortalDeparture13Done


def iscPortalDeparture15():
 iscPortalDestination45()
 #iscPortalDeparture15Done


def iscSetLabel16():
 thisiscApp1.iscWindow113Brains0.set_label(thisiscApp1.iscVtemp)
 iscPortalDeparture15()
 #iscSetLabel16Done


def iscConvertNumberToText17():
 thisiscApp1.iscVtemp = str(thisiscApp1.iscVhandBrains)
 iscSetLabel16()
 #iscConvertNumberToText17Done


def iscSetTextBox20():
 thisiscApp1.iscWindow113maindialog0.set_text(thisiscApp1.iscVtemp)
 iscnext_Player174()
 #iscSetTextBox20Done


def iscplayerlist22():
 thisiscApp1.iscVtemp=thisiscApp1.iscVPlayers_Group.__repr__()
 thisiscApp1.iscVNumberPlayers=len(thisiscApp1.iscVPlayers_Group.group)
 iscSetTextBox20()
 #iscplayerlist22Done

def iscPortalDeparture23():
 iscPortalDestination45()
 #iscPortalDeparture23Done


def iscRoll_Hand25():
 thisiscApp1.iscVhand.roll()
 iscPortalDeparture23()
 #iscRoll_Hand25Rolled

def iscConvertNumberToText26():
 thisiscApp1.iscVtemp = str(thisiscApp1.iscVhandShots)
 iscSetLabel27()
 #iscConvertNumberToText26Done


def iscSetLabel27():
 thisiscApp1.iscWindow113Shots0.set_label(thisiscApp1.iscVtemp)
 iscgetHandBrains29()
 #iscSetLabel27Done


def iscgetHandBrains29():
 thisiscApp1.iscVhandBrains=thisiscApp1.iscVhand.brains
 iscConvertNumberToText17()
 #iscgetHandBrains29Done

def iscAppQuit30():
 thisiscApp1.destroy(None,None)
 #iscAppQuit30Done


def iscBank_Brains39():
 thisiscApp1.iscVCurrentPlayer.brain_count += thisiscApp1.iscVhandBrains
 iscplayerlist22()
 #iscBank_Brains39Done

def iscPortalDeparture42():
 iscPortalDestination45()
 #iscPortalDeparture42Done


def iscGet_Hand44():
 thisiscApp1.iscVhand.fill(thisiscApp1.iscVDice_Cup)
 iscPortalDeparture42()
 #iscGet_Hand44Done

def iscPortalDestination45():
 iscGetDiceText52()
 #iscPortalDestination45Arrived


def iscGetTextField46():
 thisiscApp1.iscVCurrentPlayer = thisiscApp1.iscWindow48Pname0.get_buffer().get_text(thisiscApp1.iscWindow48Pname0.get_buffer().get_start_iter(), thisiscApp1.iscWindow48Pname0.get_buffer().get_end_iter())
 iscAddPlayer5()
 #iscGetTextField46Done


def iscCloseWindow47():
 thisiscApp1.iscWindow48Player1.destroy()
 iscWindow113()
 #iscCloseWindow47Done


def iscWindow48():
 thisiscApp1.iscWindow48addPlayer0 = gtk.Button("Add")
 thisiscApp1.iscWindow48done0 = gtk.Button("Done")
 thisiscApp1.iscWindow48Plist0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow48Pname0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow48Label0 =gtk.Label("Enter your name")
 thisiscApp1.iscWindow48Shuffle0 = gtk.Button("Shuffle")
 thisiscApp1.iscWindow48firstup0 = gtk.Entry()
 thisiscApp1.iscWindow48Firstup0 =gtk.Label("First up")
 thisiscApp1.iscWindow48Player1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow48Player1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow48Player1.set_title("Player entry")
 thisiscApp1.iscWindow48Player1.set_default_size(707, 471)
 thisiscApp1.iscWindow48Player1.add(thisiscApp1.iscWindow48Player1Fixed)
 thisiscApp1.iscWindow48Player1Fixed.width = 707
 thisiscApp1.iscWindow48Player1Fixed.height = 471
 thisiscApp1.iscWindow48Player1.connect("delete_event", iscWindow48Closed)
 thisiscApp1.iscWindow48Player1.set_resizable(False)
 thisiscApp1.iscWindow48Player1Fixed.show()
 thisiscApp1.iscWindow48Player1Fixed.put(thisiscApp1.iscWindow48addPlayer0, 37, 84)
 thisiscApp1.iscWindow48addPlayer0.set_size_request(80, 26)
 thisiscApp1.iscWindow48addPlayer0.connect("clicked", iscWindow48addPlayerClicked)
 thisiscApp1.iscWindow48addPlayer0.show()
 thisiscApp1.iscWindow48Player1Fixed.put(thisiscApp1.iscWindow48done0, 243, 247)
 thisiscApp1.iscWindow48done0.set_size_request(80, 26)
 thisiscApp1.iscWindow48done0.connect("clicked", iscWindow48doneClicked)
 thisiscApp1.iscWindow48done0.show()
 thisiscApp1.iscWindow48Player1Fixed.put(thisiscApp1.iscWindow48Plist0, 14, 127)
 thisiscApp1.iscWindow48Plist0.set_size_request(189, 147)
 thisiscApp1.iscWindow48Plist0.show()
 thisiscApp1.iscWindow48Player1Fixed.put(thisiscApp1.iscWindow48Pname0, 38, 48)
 thisiscApp1.iscWindow48Pname0.set_size_request(250, 25)
 thisiscApp1.iscWindow48Pname0.show()
 thisiscApp1.iscWindow48Player1Fixed.put(thisiscApp1.iscWindow48Label0, 42, 22)
 thisiscApp1.iscWindow48Label0.set_size_request(109, 20)
 thisiscApp1.iscWindow48Label0.show()
 thisiscApp1.iscWindow48Player1Fixed.put(thisiscApp1.iscWindow48Shuffle0, 243, 202)
 thisiscApp1.iscWindow48Shuffle0.set_size_request(80, 26)
 thisiscApp1.iscWindow48Shuffle0.connect("clicked", iscWindow48ShuffleClicked)
 thisiscApp1.iscWindow48Shuffle0.show()
 thisiscApp1.iscWindow48Player1Fixed.put(thisiscApp1.iscWindow48firstup0, 243, 164)
 thisiscApp1.iscWindow48firstup0.set_text("")
 thisiscApp1.iscWindow48firstup0.set_size_request(80, 22)
 thisiscApp1.iscWindow48firstup0.connect("changed", iscWindow48firstupChanged)
 thisiscApp1.iscWindow48firstup0.show()
 thisiscApp1.iscWindow48Player1Fixed.put(thisiscApp1.iscWindow48Firstup0, 246, 133)
 thisiscApp1.iscWindow48Firstup0.set_size_request(55, 18)
 thisiscApp1.iscWindow48Firstup0.show()
 thisiscApp1.iscWindow48Player1.show()
 #iscWindow48Opened
 #iscWindow48Done


def iscWindow48Closed(self, other):
 pass
 iscAppQuit30()
 #iscWindow48Closed


def iscWindow48addPlayerClicked(self):
 pass
 iscGetTextField46()
 #iscWindow48addPlayerClicked


def iscWindow48doneClicked(self):
 pass
 iscCloseWindow47()
 #iscWindow48doneClicked


def iscWindow48ShuffleClicked(self):
 pass
 iscShufflePlayers7()
 #iscWindow48ShuffleClicked


def iscWindow48firstupChanged(self):
 pass
 #iscWindow48firstupChanged


def iscGetDiceText50():
 if thisiscApp1.iscVone  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVone]
  thisiscApp1.iscVdie1text = d.__repr__()
  iscIfThen65()
  iscGetDiceText54()
  #iscGetDiceText50text done
 else:
  thisiscApp1.iscVdie1text = "blank"
  iscSetCanvasPicture93()
  iscSetCanvasPicture92()
  #iscGetDiceText50blank

def iscGetDiceText52():
 if thisiscApp1.iscVzero  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVzero]
  thisiscApp1.iscVdie0text = d.__repr__()
  iscGetDiceText50()
  iscIfThen55()
  #iscGetDiceText52text done
 else:
  thisiscApp1.iscVdie0text = "blank"
  iscSetCanvasPicture94()
  iscSetCanvasPicture93()
  iscSetCanvasPicture92()
  #iscGetDiceText52blank

def iscGetDiceText54():
 if thisiscApp1.iscVtwo  <=  (len(thisiscApp1.iscVhand.dice) - 1):
  d = thisiscApp1.iscVhand.dice[thisiscApp1.iscVtwo]
  thisiscApp1.iscVdie2text = d.__repr__()
  iscIfThen66()
  #iscGetDiceText54text done
 else:
  thisiscApp1.iscVdie2text = "blank"
  iscSetCanvasPicture92()
  #iscGetDiceText54blank

def iscIfThen55():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture82()
  #iscIfThen55True

  pass
 else:
  iscIfThen56()
  #iscIfThen55False

  pass

def iscIfThen56():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture112()
  #iscIfThen56True

  pass
 else:
  iscIfThen57()
  #iscIfThen56False

  pass

def iscIfThen57():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture111()
  #iscIfThen57True

  pass
 else:
  iscIfThen58()
  #iscIfThen57False

  pass

def iscIfThen58():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture110()
  #iscIfThen58True

  pass
 else:
  iscIfThen59()
  #iscIfThen58False

  pass

def iscIfThen59():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture108()
  #iscIfThen59True

  pass
 else:
  iscIfThen60()
  #iscIfThen59False

  pass

def iscIfThen60():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture109()
  #iscIfThen60True

  pass
 else:
  iscIfThen61()
  #iscIfThen60False

  pass

def iscIfThen61():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture107()
  #iscIfThen61True

  pass
 else:
  iscIfThen62()
  #iscIfThen61False

  pass

def iscIfThen62():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture106()
  #iscIfThen62True

  pass
 else:
  iscIfThen63()
  #iscIfThen62False

  pass

def iscIfThen63():
 if thisiscApp1.iscVdie0text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture105()
  #iscIfThen63True

  pass
 else:
  iscSetLabel95()
  #iscIfThen63False

  pass

def iscIfThen64():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture101()
  #iscIfThen64True

  pass
 else:
  iscIfThen69()
  #iscIfThen64False

  pass

def iscIfThen65():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture104()
  #iscIfThen65True

  pass
 else:
  iscIfThen67()
  #iscIfThen65False

  pass

def iscIfThen66():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenBrains:
  iscSetCanvasPicture83()
  #iscIfThen66True

  pass
 else:
  iscIfThen74()
  #iscIfThen66False

  pass

def iscIfThen67():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture103()
  #iscIfThen67True

  pass
 else:
  iscIfThen68()
  #iscIfThen67False

  pass

def iscIfThen68():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture102()
  #iscIfThen68True

  pass
 else:
  iscIfThen64()
  #iscIfThen68False

  pass

def iscIfThen69():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture100()
  #iscIfThen69True

  pass
 else:
  iscIfThen70()
  #iscIfThen69False

  pass

def iscIfThen70():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture99()
  #iscIfThen70True

  pass
 else:
  iscIfThen71()
  #iscIfThen70False

  pass

def iscIfThen71():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture98()
  #iscIfThen71True

  pass
 else:
  iscIfThen72()
  #iscIfThen71False

  pass

def iscIfThen72():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture97()
  #iscIfThen72True

  pass
 else:
  iscIfThen73()
  #iscIfThen72False

  pass

def iscIfThen73():
 if thisiscApp1.iscVdie1text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture96()
  #iscIfThen73True

  pass
 else:
  iscSetLabel95()
  #iscIfThen73False

  pass

def iscIfThen74():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenrun:
  iscSetCanvasPicture84()
  #iscIfThen74True

  pass
 else:
  iscIfThen75()
  #iscIfThen74False

  pass

def iscIfThen75():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisGreenshot:
  iscSetCanvasPicture85()
  #iscIfThen75True

  pass
 else:
  iscIfThen76()
  #iscIfThen75False

  pass

def iscIfThen76():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowbrains:
  iscSetCanvasPicture86()
  #iscIfThen76True

  pass
 else:
  iscIfThen77()
  #iscIfThen76False

  pass

def iscIfThen77():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowrun:
  iscSetCanvasPicture87()
  #iscIfThen77True

  pass
 else:
  iscIfThen78()
  #iscIfThen77False

  pass

def iscIfThen78():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisYellowshot:
  iscSetCanvasPicture88()
  #iscIfThen78True

  pass
 else:
  iscIfThen79()
  #iscIfThen78False

  pass

def iscIfThen79():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedbrains:
  iscSetCanvasPicture89()
  #iscIfThen79True

  pass
 else:
  iscIfThen80()
  #iscIfThen79False

  pass

def iscIfThen80():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedshot:
  iscSetCanvasPicture90()
  #iscIfThen80True

  pass
 else:
  iscIfThen81()
  #iscIfThen80False

  pass

def iscIfThen81():
 if thisiscApp1.iscVdie2text == thisiscApp1.iscVisRedrun:
  iscSetCanvasPicture91()
  #iscIfThen81True

  pass
 else:
  iscSetLabel95()
  #iscIfThen81False

  pass

def iscSetCanvasPicture82():
 thisiscApp1.iscWindow113die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture82Done


def iscSetCanvasPicture83():
 thisiscApp1.iscWindow113Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture83Done


def iscSetCanvasPicture84():
 thisiscApp1.iscWindow113Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture84Done


def iscSetCanvasPicture85():
 thisiscApp1.iscWindow113Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture85Done


def iscSetCanvasPicture86():
 thisiscApp1.iscWindow113Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture86Done


def iscSetCanvasPicture87():
 thisiscApp1.iscWindow113Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture87Done


def iscSetCanvasPicture88():
 thisiscApp1.iscWindow113Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture88Done


def iscSetCanvasPicture89():
 thisiscApp1.iscWindow113Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture89Done


def iscSetCanvasPicture90():
 thisiscApp1.iscWindow113Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture90Done


def iscSetCanvasPicture91():
 thisiscApp1.iscWindow113Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture91Done


def iscSetCanvasPicture92():
 thisiscApp1.iscWindow113Die20.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture92Done


def iscSetCanvasPicture93():
 thisiscApp1.iscWindow113Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture93Done


def iscSetCanvasPicture94():
 thisiscApp1.iscWindow113die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/blank.jpg") #iscSetCanvasPicture94Done


def iscSetLabel95():
 thisiscApp1.iscWindow113Label0.set_label(thisiscApp1.iscVerror)
 #iscSetLabel95Done


def iscSetCanvasPicture96():
 thisiscApp1.iscWindow113Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture96Done


def iscSetCanvasPicture97():
 thisiscApp1.iscWindow113Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture97Done


def iscSetCanvasPicture98():
 thisiscApp1.iscWindow113Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture98Done


def iscSetCanvasPicture99():
 thisiscApp1.iscWindow113Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture99Done


def iscSetCanvasPicture100():
 thisiscApp1.iscWindow113Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture100Done


def iscSetCanvasPicture101():
 thisiscApp1.iscWindow113Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture101Done


def iscSetCanvasPicture102():
 thisiscApp1.iscWindow113Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture102Done


def iscSetCanvasPicture103():
 thisiscApp1.iscWindow113Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture103Done


def iscSetCanvasPicture104():
 thisiscApp1.iscWindow113Die10.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gbrain.jpg") #iscSetCanvasPicture104Done


def iscSetCanvasPicture105():
 thisiscApp1.iscWindow113die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rshot.jpg") #iscSetCanvasPicture105Done


def iscSetCanvasPicture106():
 thisiscApp1.iscWindow113die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rfeet.jpg") #iscSetCanvasPicture106Done


def iscSetCanvasPicture107():
 thisiscApp1.iscWindow113die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/rbrain.jpg") #iscSetCanvasPicture107Done


def iscSetCanvasPicture108():
 thisiscApp1.iscWindow113die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yfeet.jpg") #iscSetCanvasPicture108Done


def iscSetCanvasPicture109():
 thisiscApp1.iscWindow113die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/yshot.jpg") #iscSetCanvasPicture109Done


def iscSetCanvasPicture110():
 thisiscApp1.iscWindow113die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/ybrain.jpg") #iscSetCanvasPicture110Done


def iscSetCanvasPicture111():
 thisiscApp1.iscWindow113die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gshot.jpg") #iscSetCanvasPicture111Done


def iscSetCanvasPicture112():
 thisiscApp1.iscWindow113die00.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/gfeet.jpg") #iscSetCanvasPicture112Done


def iscScoreHand115():
 if thisiscApp1.iscVhand.score():
  iscgetHandShots19()
  #iscScoreHand115Alive
 else:
  iscSetTextBox37()
  #iscScoreHand115Dead
def iscgetCurrentPlayer35():
 thisiscApp1.iscVCurrentPlayer=thisiscApp1.iscVPlayers_Group.group[thisiscApp1.iscVzero]
 iscgetPname33()
 #iscgetCurrentPlayer35Done

def iscSetTextField3():
 thisiscApp1.iscWindow48Pname0.get_buffer().set_text(thisiscApp1.iscVempty_str)
 iscplayerlist2()
 #iscSetTextField3Done


def iscSetTextBox14():
 thisiscApp1.iscWindow113maindialog0.set_text(thisiscApp1.iscVtemp)
 iscPortalDeparture13()
 #iscSetTextBox14Done


def iscinit_zdice41():
 thisiscApp1.iscVDice_Cup=Dice_Cup()
 thisiscApp1.iscVPlayers_Group=Players_Group()
 thisiscApp1.iscVhand=Hand()

 iscWindow48()
 #iscinit_zdice41Done
def iscSetTextField36():
 thisiscApp1.iscWindow48Plist0.get_buffer().set_text(thisiscApp1.iscVtemp)
 iscgetCurrentPlayer35()
 #iscSetTextField36Done


def iscgetPname33():
 thisiscApp1.iscVtemp = thisiscApp1.iscVCurrentPlayer.name
 thisiscApp1.iscVhandBrains = thisiscApp1.iscVCurrentPlayer.brain_count
 iscSetTextBox31()
 #iscgetPname33Done

def iscSetTextBox31():
 thisiscApp1.iscWindow48firstup0.set_text(thisiscApp1.iscVtemp)
 #iscSetTextBox31Done


def iscnext_Player174():
 thisiscApp1.iscVCurrentPlayer = thisiscApp1.iscVPlayers_Group.next_player(thisiscApp1.iscVCurrentPlayer)
 iscgetPname10()
 #iscnext_Player174Done

def iscplayerlist2():
 thisiscApp1.iscVtemp=thisiscApp1.iscVPlayers_Group.__repr__()
 thisiscApp1.iscVNumberPlayers=len(thisiscApp1.iscVPlayers_Group.group)
 iscSetTextField36()
 #iscplayerlist2Done

def iscgetPname10():
 thisiscApp1.iscVtemp = thisiscApp1.iscVCurrentPlayer.name
 thisiscApp1.iscVtemp_num = thisiscApp1.iscVCurrentPlayer.brain_count
 iscSetTextBox194()
 #iscgetPname10Done

def iscSetTextBox194():
 thisiscApp1.iscWindow113playerup0.set_text(thisiscApp1.iscVtemp)
 iscSetTextBox237()
 #iscSetTextBox194Done


def iscgetHandShots19():
 thisiscApp1.iscVhandShots=thisiscApp1.iscVhand.shots
 iscConvertNumberToText26()
 #iscgetHandShots19Done

def iscinit_Hand_cup236():
 thisiscApp1.iscVhand= Hand()
 thisiscApp1.iscVDice_Cup = Dice_Cup()
 iscgetHandShots19()
 #iscinit_Hand_cup236Done

def iscWindow113():
 thisiscApp1.iscWindow113Die10 = gtk.Image()
 thisiscApp1.iscWindow113Die20 = gtk.Image()
 thisiscApp1.iscWindow113Roll0 = gtk.Button("Roll")
 thisiscApp1.iscWindow113test10 = gtk.Entry()
 thisiscApp1.iscWindow113test20 = gtk.Entry()
 thisiscApp1.iscWindow113die00 = gtk.Image()
 thisiscApp1.iscWindow113Label0 =gtk.Label("Hand")
 thisiscApp1.iscWindow113playerup0 = gtk.Entry()
 thisiscApp1.iscWindow113Score0 = gtk.Button("Score Hand")
 thisiscApp1.iscWindow113Pass0 = gtk.Button("Pass")
 thisiscApp1.iscWindow113Brains0 =gtk.Label("Brains")
 thisiscApp1.iscWindow113Shots0 =gtk.Label("Shots")
 thisiscApp1.iscWindow113getdice0 = gtk.Button("get dice")
 thisiscApp1.iscWindow113dialog0 = gtk.Entry()
 thisiscApp1.iscWindow113maindialog0 = gtk.Entry()
 thisiscApp1.iscWindow113Playerup2 =gtk.Label("Player up ->")
 thisiscApp1.iscWindow113main1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow113main1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow113main1.set_title("Z_dice")
 thisiscApp1.iscWindow113main1.set_default_size(640, 480)
 thisiscApp1.iscWindow113main1.add(thisiscApp1.iscWindow113main1Fixed)
 thisiscApp1.iscWindow113main1Fixed.width = 640
 thisiscApp1.iscWindow113main1Fixed.height = 480
 thisiscApp1.iscWindow113main1.connect("delete_event", iscWindow113Closed)
 thisiscApp1.iscWindow113main1.set_resizable(False)
 thisiscApp1.iscWindow113main1Fixed.show()
 iscWindow113Die10EventBox = gtk.EventBox()
 iscWindow113Die10EventBox.set_size_request(60, 60)
 iscWindow113Die10EventBox.connect("button_press_event", iscWindow113Die1Clicked)
 thisiscApp1.iscWindow113Die10.set_size_request(60, 60)
 iscWindow113Die10EventBox.add(thisiscApp1.iscWindow113Die10)
 thisiscApp1.iscWindow113main1Fixed.put(iscWindow113Die10EventBox, 140, 150)
 thisiscApp1.iscWindow113Die10.show()
 iscWindow113Die10EventBox.show()
 iscWindow113Die20EventBox = gtk.EventBox()
 iscWindow113Die20EventBox.set_size_request(60, 60)
 iscWindow113Die20EventBox.connect("button_press_event", iscWindow113Die2Clicked)
 thisiscApp1.iscWindow113Die20.set_size_request(60, 60)
 iscWindow113Die20EventBox.add(thisiscApp1.iscWindow113Die20)
 thisiscApp1.iscWindow113main1Fixed.put(iscWindow113Die20EventBox, 230, 150)
 thisiscApp1.iscWindow113Die20.show()
 iscWindow113Die20EventBox.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113Roll0, 32, 256)
 thisiscApp1.iscWindow113Roll0.set_size_request(80, 26)
 thisiscApp1.iscWindow113Roll0.connect("clicked", iscWindow113RollClicked)
 thisiscApp1.iscWindow113Roll0.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113test10, 229, 249)
 thisiscApp1.iscWindow113test10.set_text("")
 thisiscApp1.iscWindow113test10.set_size_request(132, 27)
 thisiscApp1.iscWindow113test10.connect("changed", iscWindow113test1Changed)
 thisiscApp1.iscWindow113test10.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113test20, 229, 284)
 thisiscApp1.iscWindow113test20.set_text("")
 thisiscApp1.iscWindow113test20.set_size_request(132, 25)
 thisiscApp1.iscWindow113test20.connect("changed", iscWindow113test2Changed)
 thisiscApp1.iscWindow113test20.show()
 iscWindow113die00EventBox = gtk.EventBox()
 iscWindow113die00EventBox.set_size_request(60, 60)
 iscWindow113die00EventBox.connect("button_press_event", iscWindow113die0Clicked)
 thisiscApp1.iscWindow113die00.set_size_request(60, 60)
 iscWindow113die00EventBox.add(thisiscApp1.iscWindow113die00)
 thisiscApp1.iscWindow113main1Fixed.put(iscWindow113die00EventBox, 50, 150)
 thisiscApp1.iscWindow113die00.show()
 iscWindow113die00EventBox.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113Label0, 145, 120)
 thisiscApp1.iscWindow113Label0.set_size_request(45, 18)
 thisiscApp1.iscWindow113Label0.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113playerup0, 228, 219)
 thisiscApp1.iscWindow113playerup0.set_text("")
 thisiscApp1.iscWindow113playerup0.set_size_request(130, 25)
 thisiscApp1.iscWindow113playerup0.connect("changed", iscWindow113playerupChanged)
 thisiscApp1.iscWindow113playerup0.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113Score0, 29, 291)
 thisiscApp1.iscWindow113Score0.set_size_request(80, 26)
 thisiscApp1.iscWindow113Score0.connect("clicked", iscWindow113ScoreClicked)
 thisiscApp1.iscWindow113Score0.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113Pass0, 130, 281)
 thisiscApp1.iscWindow113Pass0.set_size_request(80, 26)
 thisiscApp1.iscWindow113Pass0.connect("clicked", iscWindow113PassClicked)
 thisiscApp1.iscWindow113Pass0.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113Brains0, 52, 120)
 thisiscApp1.iscWindow113Brains0.set_size_request(55, 20)
 thisiscApp1.iscWindow113Brains0.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113Shots0, 233, 120)
 thisiscApp1.iscWindow113Shots0.set_size_request(57, 18)
 thisiscApp1.iscWindow113Shots0.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113getdice0, 31, 222)
 thisiscApp1.iscWindow113getdice0.set_size_request(80, 26)
 thisiscApp1.iscWindow113getdice0.connect("clicked", iscWindow113getdiceClicked)
 thisiscApp1.iscWindow113getdice0.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113dialog0, 61, -105)
 thisiscApp1.iscWindow113dialog0.set_text("dialog")
 thisiscApp1.iscWindow113dialog0.set_size_request(234, 62)
 thisiscApp1.iscWindow113dialog0.connect("changed", iscWindow113dialogChanged)
 thisiscApp1.iscWindow113dialog0.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113maindialog0, 52, 12)
 thisiscApp1.iscWindow113maindialog0.set_text("TextBox")
 thisiscApp1.iscWindow113maindialog0.set_size_request(240, 92)
 thisiscApp1.iscWindow113maindialog0.connect("changed", iscWindow113maindialogChanged)
 thisiscApp1.iscWindow113maindialog0.show()
 thisiscApp1.iscWindow113main1Fixed.put(thisiscApp1.iscWindow113Playerup2, 143, 221)
 thisiscApp1.iscWindow113Playerup2.set_size_request(78, 20)
 thisiscApp1.iscWindow113Playerup2.show()
 thisiscApp1.iscWindow113main1.show()
 iscgetPname10()
 #iscWindow113Opened
 #iscWindow113Done


def iscWindow113Closed(self, other):
 pass
 iscAppQuit30()
 #iscWindow113Closed


def iscWindow113Die1Clicked(widget, event):
 pass
 #iscWindow113Die1Clicked


def iscWindow113Die2Clicked(widget, event):
 pass
 #iscWindow113Die2Clicked


def iscWindow113RollClicked(self):
 pass
 iscRoll_Hand25()
 #iscWindow113RollClicked


def iscWindow113test1Changed(self):
 pass
 #iscWindow113test1Changed


def iscWindow113test2Changed(self):
 pass
 #iscWindow113test2Changed


def iscWindow113die0Clicked(widget, event):
 pass
 #iscWindow113die0Clicked


def iscWindow113playerupChanged(self):
 pass
 #iscWindow113playerupChanged


def iscWindow113ScoreClicked(self):
 pass
 iscScoreHand115()
 #iscWindow113ScoreClicked


def iscWindow113PassClicked(self):
 pass
 iscBank_Brains39()
 #iscWindow113PassClicked


def iscWindow113getdiceClicked(self):
 pass
 iscGet_Hand44()
 #iscWindow113getdiceClicked


def iscWindow113dialogChanged(self):
 pass
 #iscWindow113dialogChanged


def iscWindow113maindialogChanged(self):
 pass
 #iscWindow113maindialogChanged


def iscSetTextBox37():
 thisiscApp1.iscWindow113test10.set_text(thisiscApp1.iscVDeadMessage)
 iscnext_Player174()
 #iscSetTextBox37Done


def iscSetTextBox237():
 thisiscApp1.iscWindow113test10.set_text(thisiscApp1.iscVempty_str)
 iscinit_Hand_cup236()
 #iscSetTextBox237Done


#EndOfFunctions

thisiscApp1 = iscApp1()

iscinit_zdice41()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()