from graphicsscript import *
import math
import time
from random import *
import random

win = GraphWin("turingMachine", 800, 500)

class tape:                              ### tape, 120 bits long with draw methods
    def __init__(self, list):
        self.list = list

    def draw(self):
        i = 0
        for bit in self.list:
            s = Rectangle(Point(20*(i%40) + 4, 52 + math.floor(i/40)*20), Point(20*(i%40+1), 68 + math.floor(i/40)*20))
            if bit == 1:
                s.setFill("black")
                s.draw(win)
            else:
                s.draw(win)
            
            i += 1

    def writeBit(self, i, new):
        self.list[i] = new
        s = Rectangle(Point(20*(i%40) + 4, 52 + math.floor(i/40)*20), Point(20*(i%40+1), 68 + math.floor(i/40)*20))
        if new == 1:
            s.setFill("black")
            s.draw(win)
        else:
            s.setFill("white")
            s.draw(win)

    def readBit(self, i):
        return self.list[i]

                    
def randTape(length):                   ### creates random tape
    li = []
    for i in range(length):
        li.append(randint(0,1))
    print li
    return tape(li)

def randProgram(maxLength):            ### creates random t machine
    prog = []
    size = randint(1, maxLength)
    for i in range(size):
        prog.append([])
        for j in range(6):
            prog[i].append([])
            if j != 2 and j != 5:
                prog[i][j] = randint(0,1)
            else:
                prog[i][j] = randint(0, size - 1)
    return prog



def execute(program, tape, position):        ### executes turing machine
   
    pos = position
    mode = 0
    cursor = Rectangle(Point(20*(pos%40)+2, 50 + math.floor(pos/40)*20), Point(20*(pos%40+1)+2, 70 + math.floor(pos/40)*20))
    killed = False
    pause = False
    
    while True and killed == False:
        pos = pos%800
    
        cursor.undraw()
        cursor = Rectangle(Point(20*(pos%40)+2, 50 + math.floor(pos/40)*20), Point(20*(pos%40+1)+2, 70 + math.floor(pos/40)*20))
        cursor.setOutline("red")
        cursor.draw(win)
        read = tape.readBit(pos)
        
        if read == 0:
            tape.writeBit(pos, program[mode][0])
            pos = pos + (program[mode][1]*2 - 1)
            mode = program[mode][2]
        elif read == 1:
            tape.writeBit(pos, program[mode][3])
            pos = pos + (program[mode][4]*2 - 1)
            mode = program[mode][5]

        if win.checkKey() == "n":
            killed = True
            cursor.undraw()
            print "next"
            return pos
        if win.checkMouse() != None:
            print "paused"
            paused = True
            while paused == True:
                key = win.getKey()
                if key == "p":
                    print "unpaused"
                    paused = False
                elif key == "k":
                    print "killed"
                    killed = True
                    paused = False






firstTape = randTape(800)
firstTape.draw()
position = 420
running = True

while running == True:
    program = randProgram(15)
    print program
    position = execute(program, firstTape, position)
    if position == "killed":
        running = False

                              

win.getMouse()


