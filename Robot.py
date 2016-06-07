
from Tkinter import *
import random
import time
from math import *




class Robot:
    x = 0
    y = 0
    Id = 0
    battery = 100
    whiteArea = None
    tmpx = 250
    tmpy = 250
    counterMSG = 0
    canvas = None
    robots = []
    staticRobots = [] 
    oneRobotMove = 5


    
    def __init__(self, Id, x, y, canvas, isStatic, robots):
        start_time = time.time()
        self.Id = Id
        self.x = x
        self.y = y
        self.isStatic = isStatic
        start_time = time.time()
        self.canvas = canvas
        self.robots = robots
        self.oneRobotMove = 5
        self.staticRobots = []
        
        if(isStatic):
             canvas.create_oval(x - 3, y - 3, x + 3, y + 3, width = 0, fill = 'red')
             canvas.create_text(x, y)
        else:
             canvas.create_oval(x - 3, y - 3, x + 3, y + 3, width = 0, fill = 'green')
             canvas.create_text(x, y)


        if ((x >= 330 and x <= 600 and y >= 330 and y <= 500)):
            self.whiteArea = False
        else:
            self.whiteArea = True


    def batteryInfo(self):
        if (self.whiteArea and self.battery < 100):
            self.battery = self.battery + 1
        elif ((not self.whiteArea) and self.battery > 0):
            self.battery = self.battery - 1


    def MoveRobot(self):
        if (self.isStatic):
            self.canvas.create_oval(self.x - 3, self.y - 3, self.x + 3, self.y + 3, width = 0, fill = 'red')
            self.canvas.create_text(self.x, self.y)
            return

        if (self.x >= 330 and self.x <= 600 and self.y >= 330 and self.y <= 500):
            self.canvas.create_oval(self.x - 7, self.y - 7, self.x + 7, self.y + 7, width = 0, fill = 'green')
        else:
            self.canvas.create_oval(self.x - 7, self.y - 7, self.x + 7, self.y + 7, width = 0, fill = 'white')

        
        while (True):
            MoveTo = random.random()
            if (MoveTo < 0.25):  
                tmpx = self.x + 5
                tmpy = self.y
            elif (MoveTo < 0.50): 
                tmpx = self.x - 5
                tmpy = self.y
            elif (MoveTo < 0.75):  
                tmpy = self.y + 5
                tmpx = self.x
            else:               
                tmpy = self.y - 5
                tmpx = self.x

            if (checkTrans(tmpx,tmpy, self.robots)):  
                self.x = tmpx
                self.y = tmpy
                break

        self.canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, width = 0,fill = 'green')  
        self.canvas.create_text(self.x, self.y)

        self.batteryInfo









def checkTrans(tmpx, tmpy, robots):
    if (tmpx > 1000 or tmpx < 0): 
            return False

    if (tmpy > 750 or tmpy < 0):
            return False
    elif ((tmpx >= 115 and tmpx <= 215 and tmpy >= 115 and tmpy <= 215) or (
                                tmpx >= 295 and tmpx <= 705 and tmpy >= 595 and tmpy <= 705)):  # if its in a black area
            return False
    for i in robots:
         if (i.x - 5 < tmpx and i.x + 5 > tmpx and i.y - 5 < tmpy and i.y + 5 > tmpy):
            return False
    else:
            return True

        
