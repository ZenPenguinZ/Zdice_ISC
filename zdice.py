#!/usr/bin/python
# Filename: zdice.py

from random import shuffle
from random import randrange

class Player(object):
    """ defines an individual player"""
    WINNING_BRAIN_COUNT = 13
    def __init__(self, name, brain_count = 0):
        self.name = name
        self.brain_count = brain_count
    def __repr__(self):
        logging.warning("player.__repr__" + str(len(self.name)))
        return "test" #self.name
    def has_won(self):
        if self.brain_count >= self.WINNING_BRAIN_COUNT:
            return True
        else:
            return False
    def bank_brains(self, brains):
        self.brain_count += brains


class Players_Group(object):
    """Defines the group of players in a round robbin linked list"""
    player_group = []
    def __init__(self, player_group=None):
        if player_group is None:
            player_group = []
            self.player_group = player_group
    def __repr__(self):
        temp = []
        for i in self.player_group:
            temp.append(i.name)
        return "\n".join(temp)
    def add(self, name):
        self.player_group.append(Player(name))
    def shuffle(self):
        shuffle(self.player_group)
	def next(self, current_player_index):
		if len(self.player_group) >= current_player_index:
			current_player_index = 0
		else:
			current_player_index += 1
		return self.player_group[current_player_index]


class Die(object):
    """takes a color attr and defines a die
	color is on of "green" "yellow" "red" 
	Die.side is a tuple of NUMBER_SIDES length made up of action 'words', "brains" "shot" "run"
	Die.roll_die randomizes the Die.side_up number
	bool methods for is_color and is_action"""

    NUMBER_SIDES = 6
    BRAINS = "brains"
    SHOT = "shot"
    RUN = "run"
    GREEN =    (BRAINS,SHOT,RUN,BRAINS,RUN,BRAINS)
    YELLOW = (BRAINS,RUN,SHOT,BRAINS,RUN,SHOT)
    RED =         (SHOT,RUN,SHOT,BRAINS,SHOT,RUN)
    assert len(GREEN) ==  NUMBER_SIDES and  len(RED) ==  NUMBER_SIDES and  len(YELLOW) ==  NUMBER_SIDES
    def __init__(self, sides , side_up = 0):
        if sides == "green":
            self.sides = self.GREEN
        elif sides == "yellow":
            self.sides = self.YELLOW
        elif sides == "red":
            self.sides = self.RED
        else:
            self.sides = "error"
            print "Failed to init Die"
        self.side_up = side_up
    def __repr__(self):
        if self.is_green():
            return "Green %s" % self.sides[self.side_up]
        elif self.is_yellow():
            return "Yellow %s" % self.sides[self.side_up]
        elif self.is_red():
            return "Red %s" % self.sides[self.side_up]
        else:
            return "error"
    def roll_die(self):
        self.side_up = randrange(self.NUMBER_SIDES)
#is Color series, returns true if match
    def is_green(self):
        return self.sides == self.GREEN
    def is_yellow(self):
        return self.sides == self.YELLOW
    def is_red(self):
        return self.sides == self.RED
#is Action series,  returns true if match
    def is_brains(self):
        return self.sides[self.side_up] == self.BRAINS
    def is_shot(self):
        return self.sides[self.side_up] == self.SHOT
    def is_run(self):
        return self.sides[self.side_up] == self.RUN

class Dice_Cup(object):
    """Cup of dice to draw from"""
    NUMBER_RED = 3
    NUMBER_GREEN = 6
    NUMBER_YELLOW = 4
    POOL_SIZE = 13
    cup = []
    assert NUMBER_RED + NUMBER_GREEN + NUMBER_YELLOW  == POOL_SIZE
    def __init__(self):
        for x in range(self.NUMBER_RED):
             self.cup.append(Die("red"))
        for x in range(self.NUMBER_GREEN):
            self.cup.append(Die("green"))
        for x in range(self.NUMBER_YELLOW):
            self.cup.append(Die("yellow"))
        self.shuffle()
    def __repr__(self):
        result = []
        for d in self.cup:
              result.append(str(d))
        return "\n ".join(result)
    def shuffle(self):
        return shuffle(self.cup)
    def get_die(self):
        if len(self.cup) < 1:
            print "refreshing cup"
            self.__init__()
        self.shuffle()
        return self.cup.pop()

class Hand(object):
    HAND_SIZE = 3
    def __init__(self, shots = 0, brains = 0):
        self.shots = shots
        self.brains = brains
        self.dice = []
    def __repr__(self):
        result = []
        for d in self.dice:
            result.append(d.__repr__())
        return "|".join(result) + "\n"
    def fill(self, dice_cup):
        if len(self.dice) == self.HAND_SIZE:
            return self.dice
        for x in range(len(self.dice),self.HAND_SIZE):
            self.dice.append(dice_cup.get_die())
    def roll(self):
        for d in self.dice:
            d.roll_die()
    def score(self):
        for i in range(len(self.dice)):
            temp_die = self.dice.pop(0)  #pop first(left) die in hand
            if temp_die.is_brains():
                self.brains += 1
            if temp_die.is_shot():
                self.shots += 1
                if self.shots >= 3:
                    return False  #your Dead, turn over
            if temp_die.is_run():
                self.dice.append(temp_die) #append back to last(right) die in hand
        return True #you survived
        
