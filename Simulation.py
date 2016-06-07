
from Tkinter import *
import random
import time
from math import *
import Robot




robots_arr = []
window = Tk()
root = Tk()
Frame = Frame(root, width = 100, height = 100)
Frame.pack(expand = YES, fill = BOTH)
Frame.pack(side = TOP)
canvas = Canvas(width = 1000, height = 750, bg = 'white')



def moveOneTime():
   canvas.create_rectangle(330, 330,600 , 500, width = 2, fill = 'gray')
   canvas.create_rectangle(300, 600,700 , 700, width = 3, fill = 'black')
   nearEpsilon = 8
   epsilonRMS = 8
   randomMsgSender()
   for r in robots_arr:
            r.MoveRobot()
#            OutFromGray() ###########
            nearRealDist(r,nearEpsilon,epsilonRMS,r.oneRobotMove)



def moveFiftyTimes():
    for i in range(1,50):
        moveOneTime()

btn1 = Button(Frame, text = "move one step only", command = moveOneTime)
btn2 = Button(Frame, text = "move fifty step",command = moveFiftyTimes)


btn1.pack(side = TOP)
btn2.pack(side = TOP)


root.title("Ex3 GUI")
canvas.create_rectangle(300, 600,700 , 700, width = 3, fill = 'black')
canvas.create_rectangle(330, 330,600 , 500, width = 2, fill = 'gray')


for loc in range(0,100):
    random.seed(100-loc)
    x = random.random()*1000
    y = random.random()*750
    while ((x >= 115 and x <= 215 and y >= 115 and y <= 215)or (x >= 295 and x <= 705 and y >= 595 and y <= 705)):
            x = random.random() * 1000
            y = random.random() * 750
    if(loc < 30):
          robots_arr.insert(loc ,Robot.Robot(loc ,x ,y ,canvas ,True ,robots_arr))
          robots_arr[loc].tmpx = x
          robots_arr[loc].tmpy = y
    else:
          robots_arr.insert(loc ,Robot.Robot(loc ,x ,y ,canvas ,False ,robots_arr))



canvas.pack(expand = YES, fill = BOTH)



class MSG:
    def __init__(self, IdMsg, idSrc, xSrc,ySrc, btr):
        self.timeMSG = time.time()
        self.IdMsg = IdMsg
        self.idSrc = idSrc
        self.xSrc = xSrc
        self.ySrc = ySrc
        self.btr = btr


    def updateMSG(self, btr2):
        self.timeMSG = time.time()
        self.btr = btr2


def oklidiDist(x1 ,y1 ,x2 ,y2):
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))



def fileOfAllMsg(massage):
    counter = 0
    file=open("RM.txt", "a")
    file.write('idMsg'+'  '+'  '+'idSrc'+'  '+'xSrc'+'  '+'ySrc')
    file.write('\n')
    file.write('\n')
    counter = counter+1 
    file.write((str)(massage.IdMsg))
    file.write('  ')
    file.write((str)(massage.idSrc))
    file.write('  ')
    file.write((str)(massage.xSrc))
    file.write('  ')
    file.write((str)(massage.ySrc))
    file.write('  ')
    file.write('\n')
    file.close()



def nearRealDist(robot ,nearEpsilon ,epsilonRMS ,oneMove):
    tx = robot.tmpx
    ty = robot.tmpy

    trms=RMS(tx ,ty ,robot.Id)
    if(trms == 0):
        return
   
    if(trms > RMS(tx, ty + oneMove, robot.Id) and
       Robot.checkTrans(tx, ty + oneMove, robots_arr)):
       ty = ty + oneMove
       trms=RMS(tx, ty + oneMove, robot.Id)

    elif (trms > RMS(tx, ty - oneMove, robot.Id) and
          Robot.checkTrans(tx, ty - oneMove, robots_arr)):  
       ty = ty - oneMove
       trms = RMS(tx, ty - oneMove,robot.Id)
       
    elif (trms > RMS(tx + oneMove, ty, robot.Id)and
          Robot.checkTrans(tx + oneMove, ty, robots_arr)):  
       tx = tx + oneMove
       trms = RMS(tx + oneMove, ty, robot.Id)
       
    elif(trms>RMS(tx - oneMove, ty, robot.Id) and
         Robot.checkTrans(tx - oneMove, ty, robots_arr)):
       tx = tx - oneMove
       trms = RMS(tx - oneMove, ty, robot.Id)
       
    else:
       robots_arr[robot.Id].oneRobotMove = robots_arr[robot.Id].oneRobotMove + 5
       
    robots_arr[robot.Id].tmpy = ty
    robots_arr[robot.Id].tmpx = tx


    if((fabs(tx-robots_arr[robot.Id].x) <= nearEpsilon) and
       (fabs(ty-robots_arr[robot.Id].y) <= nearEpsilon)and
        epsilonRMS > trms and not robot.isStatic):
        i = (int)(robot.Id)
        robots_arr[i].tmpy = ty
        robots_arr[i].tmpx = tx
        robots_arr.insert(i,Robot.Robot(robot.Id, robot.tmpx, robot.tmpy,canvas,True,robots_arr))
        robots_arr.remove(robot)
       
        return



def possMsg(massage):
    RobotS = massage.idSrc
    i = robots_arr[RobotS-1]
    x = massage.xSrc
    y = massage.ySrc
    for rbt in robots_arr:
        if (rbt.isStatic == False):  
            dist= sqrt ((rbt.x-x)*(rbt.x-x) + (rbt.y-y)*(rbt.y-y))  
            massage.updateMSG(dist)
            if (dist <= 50):  
                rbt.staticRobots.append(massage)
            elif (dist > 50 and dist <= 500):  
                rand = random.random
                if (dist <= 140):
                    if (rand <= 1):
                        rbt.staticRobots.append(massage)
                elif (dist <= 230):
                    if (rand <= 0.8):
                        rbt.staticRobots.append(massage)
                elif (dist <= 320):
                    if (rand <= 0.6):
                        rbt.staticRobots.append(massage)
                elif (dist <= 410):
                    if (rand <= 0.4):
                        rbt.staticRobots.append(massage)
                elif (dist <= 500):
                    if (rand <= 0.2):
                        rbt.staticRobots.append(massage)



def RMS(tx,ty,idR):
    sum = 0
    numTr = 0
    if (len(robots_arr[idR].staticRobots) <= 2):
        return 0
    for tr in robots_arr[idR].staticRobots:
            numTr = numTr + 1
            geassToTree = oklidiDist(tr.xSrc ,tr.ySrc ,tx ,ty)
            realDist = oklidiDist(tr.xSrc ,tr.ySrc ,robots_arr[idR].x ,robots_arr[idR].y)
            newDist = (realDist - geassToTree) * (realDist - geassToTree)
            sum = sum + newDist
    avg = sum/numTr
    return sqrt(avg)


#def OutFromGray():
#    for i in robots_arr:
#        if ((i.x >= 330 and i.x <= 600 and i.y >= 330 and i.y <= 500) and  i.isStatic==False):
#            canvas.create_oval(i.x - 7, i.y - 7, i.x + 7, i.y + 7, width=0, fill='green') #delete robot
#            i.y=i.y-20 
#            canvas.create_oval(i.x - 5, i.y - 5, i.x + 5, i.y + 5, width=0, fill='red')
#            canvas.create_text(i.x,i.y)


def randomMsgSender():
    i = 0
    while (i < 100):
       
        rndRbtSnd = random.randint(0, 99)
        
        while(robots_arr[rndRbtSnd].isStatic == False):
            rndRbtSnd = random.randint(0, 99)
        r = robots_arr[rndRbtSnd]

        msg = MSG( (r.Id * 1000) + r.counterMSG, r.Id, r.x, r.y, 0)
        r.counterMSG = r.counterMSG + 1
        fileOfAllMsg(msg)
        possMsg(msg)
        i = i + 1



canvas.pack(expand = YES, fill = BOTH)
Frame.pack(expand = YES, fill = BOTH)
window.title('Ex3')
window.mainloop()
