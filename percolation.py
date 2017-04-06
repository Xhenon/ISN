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

    def __init__(self , x , y , model):
        self.tailleX = x
        self.full = " "
        self.empty = "x"
        self.tailleY = y
        self.model = model
        self.grille = [[self.empty for y in range(self.tailleY)] for x in range(self.tailleX)]

    def getTailleX(self):
        return self.tailleX

    def getTailleY(self):
        return self.tailleY

    def placer(self , x , y):   #rempmli la grille de murs
        self.grille[x][y] = self.full

    def getGrid(self):
        return self.grille

    def getEmptyCases(self):
        ca = []
        for i in range(self.tailleX):
            for j in range(self.tailleY):
                if self.grille[i][j]==self.empty:
                    ca.append(Case(i , j))
        return ca

    def getFilledCases(self):
        ca = []
        for i in range(self.tailleX):
            for j in range(self.tailleY):
                if self.grille[i][j]==self.full:
                    ca.append(Case(i , j))
        return ca


    def clearGrid(self):
        for i in range(self.tailleX):
            for j in range(self.tailleY):
                self.grille[i][j] = self.empty

    def getModel(self):
        return self.model


    def afficherGrille(self , bol):
        lignes = []
        s = ""

        for j in range(self.tailleY):
            for i in range(self.tailleX):
                s = s + str(self.grille[i][j])
            print(s)
            s=""
        print("chemin trouvé =",bol)
        print()

def testSiCheminExiste():
    global ids
    casesATester = []   #=openList
    casesTestees = []   #=closedList
    casesDeDepart = []
    finished = False
    for i in range(len(grille.getEmptyCases())):     #pour toutes les cases vides
        if grille.getEmptyCases()[i].getY()==0:  #si elle se trouve sur le bord supérieur, on l'ajoute à la liste
            casesDeDepart.append(grille.getEmptyCases()[i])

    for i in range(len(casesDeDepart)):       #pour toutes les cases de départ
        if len(casesTestees) != 0 :  #dans le cas ou la liste des cases testées n'est pas vide, on s'assure que la case que l'on va ajouter à la liste des cases à tester n'a pas deja été traitée
            if not listContainCase(casesTestees, casesDeDepart[i]):
                casesATester.append(casesDeDepart[i])

        else:       #dans le cas ou la liste des cases testées est vide, c'est à dire au début de l'algorithme
            casesATester.append(casesDeDepart[i])
        while len(casesATester) !=0:        #tant que la liste des cases Ã  tester n'est pas vide, on cherche des voisins
            for i in range(len(getAdjacentTilesTo(casesATester[0]))):
                if not listContainCase(casesTestees, getAdjacentTilesTo(casesATester[0])[i]) and not listContainCase(casesATester, getAdjacentTilesTo(casesATester[0])[i]) and listContainCase(grille.getEmptyCases() , getAdjacentTilesTo(casesATester[0])[i]):
                    casesATester.append(getAdjacentTilesTo(casesATester[0])[i])
            casesTestees.append(casesATester[0])
            casesATester.pop(0)
        if listContainY(casesTestees , 0) and listContainY(casesTestees , grille.getTailleY()-1):
            for i in range(len(casesTestees)):
                can.itemconfig(ids[casesTestees[i].getX()][casesTestees[i].getY()] , fill="blue")
            finished = True
        for i in range(len(casesTestees)):
            can.itemconfig(ids[casesTestees[i].getX()][casesTestees[i].getY()] , fill="blue")
    if finished:
        return True
    else:
        return False

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

def listContainY(list , y):     #return True si la liste contient une case avec une valeur y spÃ©cifiÃ©e
    for i in range(len(list)):
        if(areCasesSameY(list[i].getY(), y)):
            return True
    return False

def drawGraph(x , y , lengthX , lengthY , nbPoint , values, bornInf , bornSup):
    can.create_line()


def getAdjacentTilesTo(case):      #retourne les cases adjacentes Ã   celle indiquÃ©e
    cases = []
    modelList = []
    if grille.getModel() == "hexagone":
        modelList.append(Case(0,-1))
        modelList.append(Case(1,-1))
        modelList.append(Case(-1,0))
        modelList.append(Case(1,0))
        modelList.append(Case(0,1))
        modelList.append(Case(-1,1))
    elif grille.getModel() == "square":
        modelList.append(Case(0,-1))
        modelList.append(Case(1,0))
        modelList.append(Case(-1,0))
        modelList.append(Case(0,1))
    elif grille.getModel() == "triangle":
        if case.getX()/2== int(case.getX()/2):
            modelList.append(Case(-1,0))
            modelList.append(Case(1,-1))
            modelList.append(Case(1,0))
        else:
            modelList.append(Case(-1,0))
            modelList.append(Case(-1,1))
            modelList.append(Case(1,0))
    for i in range(len(modelList)):
        if(modelList[i].getX()+case.getX() >=0 and modelList[i].getY()+case.getY() >=0 and modelList[i].getX()+case.getX()<grille.getTailleX() and modelList[i].getY()+case.getY()<grille.getTailleY()):
            cases.append(Case(modelList[i].getX()+case.getX() , modelList[i].getY()+case.getY()))
    return cases

def createPolygons(x , y , model , yfenSize):
    global ids
    lengthUnit = yfenSize/(1+2*y)
    xSize = 1
    ySize = 1
    xshift2 = 0
    xshift = 2*lengthUnit
    yshift = 2*lengthUnit
    if model == "hexagone":
        for j in range(y):
            for i in range(x):
                ids[i][j] = can.create_polygon((xshift+i*1.74*lengthUnit+xshift2)*xSize , (yshift+1*lengthUnit+j*1.5*lengthUnit)*ySize , (xshift-0.87*lengthUnit+i*1.74*lengthUnit+xshift2)*xSize , (yshift+0.5*lengthUnit++j*1.5*lengthUnit)*ySize , (xshift-0.87*lengthUnit+i*1.74*lengthUnit+xshift2)*xSize , (yshift-0.5*lengthUnit+j*1.5*lengthUnit)*ySize , (xshift+i*1.74*lengthUnit+xshift2)*xSize , (yshift-1*lengthUnit+j*1.5*lengthUnit)*ySize , (xshift+0.87*lengthUnit+i*1.74*lengthUnit+xshift2)*xSize , (yshift-0.5*lengthUnit+j*1.5*lengthUnit)*ySize , (xshift+0.87*lengthUnit+i*1.74*lengthUnit+xshift2)*xSize , (yshift+0.5*lengthUnit+j*1.5*lengthUnit)*ySize ,outline= "black", fill="white", width=lengthUnit/12.5)
            xshift2 +=lengthUnit*0.87
    elif model == "square":
        for j in range(y):
            for i in range(x):
                ids[i][j] = can.create_polygon((xshift-lengthUnit+i*2*lengthUnit)*xSize , (yshift+lengthUnit+j*2*lengthUnit)*ySize , (xshift-lengthUnit+i*2*lengthUnit)*xSize , (yshift-lengthUnit+j*2*lengthUnit)*ySize , (xshift+lengthUnit+i*2*lengthUnit)*xSize , (yshift-lengthUnit+j*2*lengthUnit)*ySize , (xshift+lengthUnit+i*2*lengthUnit)*xSize , (yshift+lengthUnit+j*2*lengthUnit)*ySize, outline= "black", fill="white", width=lengthUnit/20)
    elif model == "triangle":
        for j in range(y):
            for i in range(int(x/2)):
                ids[i*2][j] = can.create_polygon((xshift-lengthUnit+i*2*lengthUnit)*xSize , (yshift+lengthUnit+j*2*lengthUnit)*ySize , (xshift-lengthUnit+i*2*lengthUnit)*xSize , (yshift-lengthUnit+j*2*lengthUnit)*ySize , (xshift+lengthUnit+i*2*lengthUnit*xSize) , (yshift -lengthUnit+j*2*lengthUnit)*ySize , outline= "black", fill="white", width=lengthUnit/12.5)
                ids[i*2+1][j] = can.create_polygon((xshift-lengthUnit+i*2*lengthUnit)*xSize , (yshift+lengthUnit+j*2*lengthUnit)*ySize , (xshift+lengthUnit+i*2*lengthUnit*xSize) , (yshift -lengthUnit+j*2*lengthUnit)*ySize , (xshift+lengthUnit+i*2*lengthUnit)*xSize , (yshift+lengthUnit+j*2*lengthUnit)*ySize, outline= "black", fill="white", width=lengthUnit/12.5)

def refresh():
    global ids , x , y , prob
    grille.clearGrid()
    for i in range(x):
        for j in range(y):
            can.itemconfig(ids[i][j] , fill="white")
    fillGrid(prob)

def fillGrid(proba):
    global ids
    for i in range(grille.getTailleX()):
        for j in range(grille.getTailleY()):
            f = random.uniform(0 , 1)
            if f<=proba:
                grille.placer(i , j)
                can.itemconfig(ids[i][j] , fill="black")

def Clic(event):
    X = event.x
    Y = event.y


#---------------------------------------

global ids , x , y , prob
x = 10
y = 10
model = "square"
ids = [[-1 for y in range(y)] for x in range(x)]
grille = Grille(x , y , model)
prob = 0.6
essais = 2
reussite = 0

fen = Tk()
can = Canvas(fen, width=1600, height=800, bg='ivory')
can.pack(side=TOP)

createPolygons(x , y , model , 800)

fillGrid(prob)

button1 = Button(text = "Check" , command = testSiCheminExiste, anchor = W)
button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
button1_window = can.create_window(1050, 750, anchor=NW, window=button1)

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

