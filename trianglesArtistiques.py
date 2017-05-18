#-*-coding: utf-8 -*-

from tkinter import *
from math import sqrt
from PIL import Image
import random
import matplotlib.colors as colorsmod
from threading import Thread

global triangleList

class Case(object):
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class TriangleList(object):
    def __init__(self, x , y , length , changeTime):
        self.tailleX = x
        self.tailleY = y
        self.length = length
        self.ids = [["-1" for x in range(self.tailleY)] for y in range(self.tailleX)]
        triangle = Triangle(Case(0 , 0) , Case(0 , 0) , Case(0 , 0) , "#FF0FFF" , "-1" , -1)
        self.triangles = [[triangle for x in range(self.tailleY)] for y in range(self.tailleX)]
        self.firstCall = True
        self.firstPhase = True
        self.changeTime = changeTime
        self.index = 0

    def getTrianglesIDS(self):
        return self.ids

    def getTriangles(self):
        return self.triangles

    def createTriangle(self , i , j , color , bol):
        if bol:
            self.ids[i][j] = str(can.create_polygon((i/2+0.5)*self.length , j*sqrt(self.length*self.length-self.length*self.length/4) , i/2*self.length , (j+1)*sqrt(self.length*self.length-self.length*self.length/4) , (i/2+1)*self.length , (j+1)*sqrt(self.length*self.length-self.length*self.length/4) , fill=rgb2hex(color[0] , color[1] , color[2])))
            self.triangles[i][j] = Triangle(Case((i/2+0.5)*self.length , j*sqrt(self.length*self.length-self.length*self.length/4)) , Case(i/2*self.length , (j+1)*sqrt(self.length*self.length-self.length*self.length/4)) , Case((i/2+1)*self.length , (j+1)*sqrt(self.length*self.length-self.length*self.length/4)) , color , self.ids[i][j] , 0)
        else:
            self.ids[i][j] = str(can.create_polygon(i/2*self.length , j*sqrt(self.length*self.length-self.length*self.length/4) , (i/2+0.5)*self.length , (j+1)*sqrt(self.length*self.length-self.length*self.length/4) , (i/2+1)*self.length , j*sqrt(self.length*self.length-self.length*self.length/4) , fill=rgb2hex(color[0] , color[1] , color[2])))
            self.triangles[i][j] = Triangle(Case(i/2*self.length , j*sqrt(self.length*self.length-self.length*self.length/4)) , Case((i/2+0.5)*self.length , (j+1)*sqrt(self.length*self.length-self.length*self.length/4)) , Case((i/2+1)*self.length , j*sqrt(self.length*self.length-self.length*self.length/4)) , color , self.ids[i][j] , 1)

    def setTriangleColor(self , case , color):
        self.triangles[case.getX()][case.getY()].setColor(color)
        can.itemconfig(self.triangles[case.getX()][case.getY()].getID() , fill=color)

    def deleteAll(self):
        for i in range(self.tailleX):
            for j in range(self.tailleY):
                can.delete(self.ids[i][j])

    def getTailleX(self):
        return self.tailleX

    def getTailleY(self):
        return self.tailleY

    def updateColors(self):
        if self.firstPhase:
            if self.firstCall:
                print("---nouvelle boucle---")
                self.firstCall = False
                for i in range(self.tailleX):
                    for j in range(self.tailleY):
                        if len(self.triangles[i][j].getNeighbors())>=1:
                            k = random.randint(0 , len(self.triangles[i][j].getNeighbors())-1)
                        else:
                            k=0
                        l = random.random()
                        self.triangles[i][j].setGoal(self.triangles[i][j].getNeighbors()[k] , changeTime , l/1)
            for i in range(self.tailleX):
                    for j in range(self.tailleY):
                        self.triangles[i][j].setColor([self.triangles[i][j].getStep()[0]+self.triangles[i][j].getColor()[0] , self.triangles[i][j].getStep()[1]+self.triangles[i][j].getColor()[1] , self.triangles[i][j].getStep()[2]+self.triangles[i][j].getColor()[2]])
                        can.itemconfig(self.ids[i][j] , fill=rgb2hex(int(self.triangles[i][j].getColor()[0]) , int(self.triangles[i][j].getColor()[1]) , int(self.triangles[i][j].getColor()[2])))
            self.index+=1
            if self.index>=self.changeTime:
                self.index = 0
                self.firstPhase = False
                self.firstCall = True
        else:
            if self.firstCall:
                self.firstCall = False
                for i in range(self.tailleX):
                    for j in range(self.tailleY):
                        l = random.random()
                        self.triangles[i][j].setGoal(self.triangles[i][j].getReference() , changeTime , l/1)

            for i in range(self.tailleX):
                    for j in range(self.tailleY):
                        self.triangles[i][j].setColor([self.triangles[i][j].getStep()[0]+self.triangles[i][j].getColor()[0] , self.triangles[i][j].getStep()[1]+self.triangles[i][j].getColor()[1] , self.triangles[i][j].getStep()[2]+self.triangles[i][j].getColor()[2]])
                        can.itemconfig(self.ids[i][j] , fill=rgb2hex(int(self.triangles[i][j].getColor()[0]) , int(self.triangles[i][j].getColor()[1]) , int(self.triangles[i][j].getColor()[2])))
            self.index+=1
            if self.index>=self.changeTime:
                self.index = 0
                self.firstPhase = True
                self.firstCall = True

class Triangle(object):
    def __init__(self, case1 , case2 , case3 , color , id, orientation):
        self.cases = []
        self.cases.append(case1)
        self.cases.append(case2)
        self.cases.append(case3)
        self.color = color
        self.id = id
        self.orientation = orientation #orientation = 0 = droit, 1 = retourné
        self.neighbors = []
        self.goal = "000000"
        self.neededCalls = 0
        self.reference = [self.color[0] , self.color[1], self.color[2]]
        self.step = [0 , 0 , 0]



    def setGoal(self , goal , neededCalls , precision):
        self.goal = goal
        self.neededCalls = neededCalls
        self.step[0] = (self.goal[0]-self.color[0])*precision/self.neededCalls
        self.step[1] = (self.goal[1]-self.color[1])*precision/self.neededCalls
        self.step[2] = (self.goal[2]-self.color[2])*precision/self.neededCalls

    def getReference(self):
        return self.reference

    def getNeededCalls(self):
        return self.neededCalls

    def getStep(self):
        return self.step

    def getGoal(self):
        return self.goal

    def getCases(self):
        return self.cases

    def getOrientation(self):
        return self.orientation

    def setOrientation(self , orientation):
        self.orientation = orientation

    def setSommet(self, index, case):
        self.cases[index] = case

    def setColor(self , color):
        self.color= color

    def getID(self):
        return self.id

    def addNeighbor(self, color):
        self.neighbors.append(color)

    def getNeighbors(self):
        return self.neighbors

    def getColor(self):
        return self.color

def rgb2hex(r,g,b):
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex

def onClosing():
    global run
    run = False
    fen.destroy()
    sys.exit(0)

def importToTriangle(url , x , y):
    global triangleList

    evenIndex = True
    oldY =0

    im = Image.open(url)
    pix = im.load()

    yim = int(im.size[1]/y)
    xim = int(im.size[0]/x)

    if x%2==0:
        for j in range(y):
            for i in range(x):
                if oldY!=j:
                    if evenIndex:
                        evenIndex = False
                    else:
                        evenIndex = True
                if evenIndex:
                    triangleList.createTriangle(i , j , [pix[i*xim,j*yim][0] , pix[i*xim,j*yim][1] , pix[i*xim,j*yim][2]] , evenIndex)
                    evenIndex=False
                else:
                    triangleList.createTriangle(i , j , [pix[i*xim,j*yim][0] , pix[i*xim,j*yim][1] , pix[i*xim,j*yim][2]] , evenIndex)
                    evenIndex=True
                oldY = j
    else:
        for j in range(y):
            for i in range(x):
                if evenIndex:
                    triangleList.createTriangle(i , j , [pix[i*xim,j*yim][0] , pix[i*xim,j*yim][1] , pix[i*xim,j*yim][2]] , evenIndex)
                    evenIndex=False
                else:
                    triangleList.createTriangle(i , j , [pix[i*xim,j*yim][0] , pix[i*xim,j*yim][1] , pix[i*xim,j*yim][2]] , evenIndex)
                    evenIndex=True

    for j in range(y):
        for i in range(x):

            if i-1>=0:
                triangleList.getTriangles()[i][j].addNeighbor(triangleList.getTriangles()[i-1][j].getColor())
            if i+1<x:
                triangleList.getTriangles()[i][j].addNeighbor(triangleList.getTriangles()[i+1][j].getColor())

            if triangleList.getTriangles()[i][j].getOrientation()==0:
                if j +1<y:
                    triangleList.getTriangles()[i][j].addNeighbor(triangleList.getTriangles()[i][j+1].getColor())
            else:
                if j-1>=0:
                    triangleList.getTriangles()[i][j].addNeighbor(triangleList.getTriangles()[i][j-1].getColor())

def createTriangle(x , y , l):
    global triangleList
    evenIndex = True

    oldY =0
    if x%2==0:
        for j in range(y):
            for i in range(x):
                if oldY!=j:
                    if evenIndex:
                        evenIndex = False
                    else:
                        evenIndex = True
                if evenIndex:
                    triangleList.createTriangle(i , j , "#FFFFFF" , evenIndex)
                    evenIndex=False
                else:
                    triangleList.createTriangle(i , j , "#000000" , evenIndex)
                    evenIndex=True
                oldY = j
    else:
        for j in range(y):
            for i in range(x):
                if evenIndex:
                    triangleList.createTriangle(i , j , "#FFFFFF" , evenIndex)
                    evenIndex=False
                else:
                    triangleList.createTriangle(i , j , "#000000" , evenIndex)
                    evenIndex=True

def getCloserTriangle(x, y):
    case, dist = -1 , 500000
    for i in range(triangleList.getTailleX()):
        for j in range(triangleList.getTailleY()):
            if pow(triangleList.getTriangles()[i][j].getCases()[0].getX()-x , 2)+pow(triangleList.getTriangles()[i][j].getCases()[0].getY()-y , 2)+pow(triangleList.getTriangles()[i][j].getCases()[1].getX()-x , 2)+pow(triangleList.getTriangles()[i][j].getCases()[1].getY()-y , 2)+pow(triangleList.getTriangles()[i][j].getCases()[2].getX()-x , 2)+pow(triangleList.getTriangles()[i][j].getCases()[2].getY()-y , 2)<dist:
                dist =pow(triangleList.getTriangles()[i][j].getCases()[0].getX()-x , 2)+pow(triangleList.getTriangles()[i][j].getCases()[0].getY()-y , 2)+pow(triangleList.getTriangles()[i][j].getCases()[1].getX()-x , 2)+pow(triangleList.getTriangles()[i][j].getCases()[1].getY()-y , 2)+pow(triangleList.getTriangles()[i][j].getCases()[2].getX()-x , 2)+pow(triangleList.getTriangles()[i][j].getCases()[2].getY()-y , 2)
                case = Case(i , j)
    return case

global run
run = True
w , h = 1600 , 1000
y  = 80
l = sqrt(4*(h/y)*(h/y)/3)
#im = Image.open("C:/Users/Clement/Desktop/lol3.png")
#pix = im.load()
#x = im.size[0]
x = int(2*w/l-1)
changeTime = 10
print("dimensions:" , x , y)
triangleList = TriangleList(x , y , l , changeTime)

fen = Tk()
can = Canvas(fen, width= w, height=h, bg='ivory')
can.pack(side=TOP)
fen.protocol("WM_DELETE_WINDOW", onClosing)

importToTriangle("E:/Projet ISN/ray.jpg" , x , y)

while run:
    triangleList.updateColors()
    fen.update()