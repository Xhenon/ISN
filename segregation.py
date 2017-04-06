#-*-coding: utf-8 -*-
import random
from tkinter import *

class Case(object):

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Grille(object):

    def __init__(self , x , y , amountOfDifferences , happiness):
        self.tailleX = x
        self.tailleY = y
        self.empty = "-1"
        self.happiness = happiness
        self.grille = [[self.empty for y in range(self.tailleY)] for x in range(self.tailleX)]
        self.amoutOfDifferences = amountOfDifferences

    def getHappiness(self):
        return self.happiness

    def getAmountOfDifferentColors(self):
        return self.amoutOfDifferences

    def getTailleX(self):
        return self.tailleX

    def getTailleY(self):
        return self.tailleY

    def placer(self , x , y , color):   #rempmli la grille de murs
        self.grille[x][y] = color

    def getGrid(self):
        return self.grille

    def getColorFromCase(self, case):
        return self.grille[case.getX()][case.getY()]

    def getEmptyCases(self):
        ca = []
        for i in range(self.tailleX):
            for j in range(self.tailleY):
                if self.grille[i][j]==self.empty:
                    ca.append(Case(i , j))
        return ca

    def getCasesOf(self , color):
        ca= []
        for i in range(self.tailleX):
            for j in range(self.tailleY):
                if self.grille[i][j]==color:
                    ca.append(Case(i , j ))
        return ca


    def clearGrid(self):
        for i in range(self.tailleX):
            for j in range(self.tailleY):
                self.grille[i][j] = self.empty


def areCasesEqual(case1 , case2):       #return True si case1 et case2 ont les memes coordonnées
    if(case1.getX() == case2.getX() and case1.getY() == case2.getY()):
        return True
    else:
        return False

def areCasesSameX(x1 , x2):     #return True si x1 et x2 sont Ã©gaux
    if x1 == x2:
        return True
    else:
        return False

def areCasesSameY(y1 , y2):     #return True si y1 et y2 sont Ã©gaux
    if y1 == y2:
        return True
    else:
        return False

def listContainCase(list , case):       #return True si la liste contient une case avec les coordonnÃ©es spÃ©cifiÃ©es
    for i in range(len(list)):
        if(areCasesEqual(list[i], case)):
            return True
    return False

def listContainX(list , x):      #return True si la liste contient une case avec une valeur x spÃ©cifiÃ©e
    for i in range(len(list)):
        if(areCasesSameX(list[i].getX(), x)):
            return True
    return False

def listContainY(list , y):     #return True si la liste contient une case avec une valeur y spécifiée
    for i in range(len(list)):
        if(areCasesSameY(list[i].getY(), y)):
            return True
    return False

def getAdjacentTilesTo(case):      #retourne les cases adjacentes à celle indiqué
    modelList = []
    modelList.append(Case(case.getX(),-1+case.getY()))
    modelList.append(Case(-1+case.getX(),-1+case.getY()))
    modelList.append(Case(case.getX(),1+case.getY()))
    modelList.append(Case(-1+case.getX(),1+case.getY()))
    modelList.append(Case(1+case.getX(),-1+case.getY()))
    modelList.append(Case(1+case.getX(),1+case.getY()))
    modelList.append(Case(1+case.getX(),case.getY()))
    modelList.append(Case(-1+case.getX(),case.getY()))
    return modelList

def getColorFromId(id):
    if id == -1:
        return "white"
    elif id == 0:
        return "blue"
    elif id == 1:
        return "red"
    elif id == 2:
        return "green"
    elif id == 3:
        return "yellow"

def computeHappiness(case , color):
    amountSelf = 0
    amountOther= 0
    for i in range(len(getAdjacentTilesTo(case))):
        if getAdjacentTilesTo(case)[i].getX()>=0 and getAdjacentTilesTo(case)[i].getX()<grille.getTailleX() and getAdjacentTilesTo(case)[i].getY()>=0 and getAdjacentTilesTo(case)[i].getY()<grille.getTailleY():
            if grille.getGrid()[getAdjacentTilesTo(case)[i].getX()][getAdjacentTilesTo(case)[i].getY()]==color:
                amountSelf=amountSelf+1
            elif grille.getGrid()[getAdjacentTilesTo(case)[i].getX()][getAdjacentTilesTo(case)[i].getY()]!=color and grille.getGrid()[getAdjacentTilesTo(case)[i].getX()][getAdjacentTilesTo(case)[i].getY()]!="-1":
                amountOther=amountOther+1
    if amountOther+amountSelf==0:
        return 0.85
    else:
        return amountSelf/(amountOther+amountSelf)

def checkHappiness(case):
    if computeHappiness(case , grille.getColorFromCase(case))<grille.getHappiness():
        return False
    else:
        return True

def findGoodEmptyHouse(color):
    ca= Case(-1 , -1)
    hap = 0
    for i in range(len(grille.getEmptyCases())):
        if computeHappiness(grille.getEmptyCases()[i] , color)> hap:
            hap = computeHappiness(grille.getEmptyCases()[i] , color)
            ca = grille.getEmptyCases()[i]
    return ca

def findRandomHouse():
    return grille.getEmptyCases()[random.randint(0 , len(grille.getEmptyCases())-1)]

def update():
    for k in range(grille.getAmountOfDifferentColors()):
        ca = grille.getCasesOf(str(k))
        for i in range(len(ca)):
            if checkHappiness(ca[i])== False:
                #c = findGoodEmptyHouse(grille.getColorFromCase(ca[i]))
                c= findRandomHouse()
                can.itemconfig(ids[c.getX()][c.getY()] , fill=getColorFromId(k))
                grille.placer(c.getX() , c.getY() , str(k))
                can.itemconfig(ids[ca[i].getX()][ca[i].getY()] , fill=getColorFromId(-1))
                grille.placer(ca[i].getX() , ca[i].getY() , "-1")



def createPolygons(x , y , yfenSize):
    global ids
    lengthUnit = yfenSize/(1+2*y)
    xSize = 1
    ySize = 1
    xshift2 = 0
    xshift = 2*lengthUnit
    yshift = 2*lengthUnit
    for j in range(y):
        for i in range(x):
            ids[i][j] = can.create_polygon((xshift-lengthUnit+i*2*lengthUnit)*xSize , (yshift+lengthUnit+j*2*lengthUnit)*ySize , (xshift-lengthUnit+i*2*lengthUnit)*xSize , (yshift-lengthUnit+j*2*lengthUnit)*ySize , (xshift+lengthUnit+i*2*lengthUnit)*xSize , (yshift-lengthUnit+j*2*lengthUnit)*ySize , (xshift+lengthUnit+i*2*lengthUnit)*xSize , (yshift+lengthUnit+j*2*lengthUnit)*ySize, outline= "black", fill="white", width=lengthUnit/20)

def refresh():
    global ids , x , y , prob
    grille.clearGrid()
    for i in range(x):
        for j in range(y):
            can.itemconfig(ids[i][j] , fill="white")
    startFilling()

def startFilling():
    fillGrid(prob , 0 , 0.3  , 0.75 , 1)

def fillGrid(probWhite , *args):
    global ids
    for i in range(grille.getTailleX()):
        for j in range(grille.getTailleY()):
            f = random.uniform(0 , 1)
            if f>probWhite:
                f = random.uniform(0 ,1)
                for k in range(len(args)-1):
                    if f<=args[k+1] and f>args[k]:
                        grille.placer(i , j , str(k))
                        can.itemconfig(ids[i][j] , fill=getColorFromId(k))

def Clic(event):
    X = event.x
    Y = event.y

    update()
    update()
    update()
    update()


#---------------------------------------

global ids , x , y , prob
x = 10
y = 10
ids = [[-1 for y in range(y)] for x in range(x)]

prob = 0.4
reussite = 0



fen = Tk()
can = Canvas(fen, width=1600, height=800, bg='ivory')
can.pack(side=TOP)

createPolygons(x , y , 800)
grille = Grille(x , y , 3 , 0.6)

startFilling()



##button1 = Button(text = "Check" , command = testSiCheminExiste, anchor = W)
##button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
##button1_window = can.create_window(1050, 750, anchor=NW, window=button1)
##
button2 = Button(text = "Refresh" , command = refresh, anchor = W)
button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
button2_window = can.create_window(1050, 700, anchor=NW, window=button2)

can.bind('<Button-1>', Clic)
fen.mainloop()

##for i in range(essais):
##    fillGrid(0.4)
##    test = testSiCheminExiste()
##    grille.afficherGrille(test)
##    if test:
##        reussite += 1
##    grille.clearGrid()
##print(reussite/essais*100 , "% de réussite pour une probabilité de",prob , "avec le modèle",grille.getModel())

