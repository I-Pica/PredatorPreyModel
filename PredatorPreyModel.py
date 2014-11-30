__author__ = 'IldefonsoPica'

import math
import random

EMPTY = 0; PREY = 1; PRED = 2
PREYLOC = [[0,0]]; PREDLOC = [[1,1]]

# class Cell:
#     def __init__(self, state, location):
#         self.state = state
#         self.loc = location
#         self.x = location[0]
#         self.y = location[1]

class Prey:
    def __init__(self, energy, location):
        self.energy = energy
        self.loc = location
        self.x = location[0]
        self.y = location[1]

class Predator:
    def __init__(self, energy, location):
        self.energy = energy
        self.loc = location
        self.x = location[0]
        self.y = location[1]

class Field:
    def __init__(self, height, width,
                 preySize, predSize, preyLoc, predLoc,
                 preyEnergy, predEnergy):
        self.nUpdates = 0
        self.height = height
        self.width = width
        self.preySize = preySize        # The number of prey in the field
        self.predSize = predSize        # The number of predators in the field

        if preySize > 0:
            self.preyList = []
            for p in range(preySize):
                prey = Prey(preyEnergy, preyLoc[p])
                self.preyList.append(prey)  # Add prey animal to prey list

        if predSize > 0:
            self.predList = []
            for p in range(predSize):
                pred = Predator(predEnergy, predLoc[p])
                self.predList.append(pred)  # Add predator animal to pred list

    def update(self):
        print self.nUpdates
        step = [-1,0,1]
        if self.preySize > 0:
            for p in self.preyList:
                print 'pre-Update - Prey location: ', p.loc
                xgo = True; ygo = True
                while xgo:
                    x = random.choice(step)+p.x
                    if 0 <= x < self.width:
                        p.loc[0] = x; xgo = False
                while ygo:
                    y = random.choice(step)+p.y
                    if 0 <= y < self.height:
                        p.loc[1] = y; ygo = False
                print 'post-Update - Prey location: ', p.loc

        if self.predSize > 0:
            for p in self.predList:
                print 'pre-Update - Predator location: ', p.loc
                xgo = True; ygo = True
                while xgo:
                    x = random.choice(step)+p.x
                    if 0 <= x < self.width:
                        p.loc[0] = x; xgo = False
                while ygo:
                    y = random.choice(step)+p.y
                    if 0 <= y < self.height:
                        p.loc[1] = y; ygo = False
                print 'post-Update - Predator location: ', p.loc
        self.nUpdates += 1


        # self.nCells = height*width  # The number of cells

        # self.list = []              # Initialize list for all cells in field
        # for h in range(height):
        #     for w in range(width):
        #         cell = Cell(EMPTY, [h, w])
        #         self.list.append(cell)      # Add cell to list
