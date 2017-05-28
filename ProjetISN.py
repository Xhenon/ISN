#-*-coding: utf-8 -*-
from tkinter import *
from math import *
import socket
from threading import Thread
from time import sleep

class Grille(object):

    def __init__(self , x , y , radius , model):
        self.turn ="1"
        self.tailleX = x
        self.tailleY = y
        self.finish = False
        self.model = model
        ca = Case(0 , 0)
        self.radius = radius
        self.grille = [["0" for x in range(self.tailleX)] for y in range(self.tailleY)]
        self.cases = [[ca for x in range(self.tailleX)] for y in range(self.tailleY)]

    def placer(self , case , joueur):
        self.grille[case.getX()][case.getY()] = joueur

    def setFinish(self, finish):
        self.finish = finish

    def isFinished(self):
        return self.finish

    def setCase(self, x , y , case):
        self.cases[x][y]= case

    def getRadius(self):
        return self.radius

    def getGrid(self):
        return self.grille

    def clearGrid(self):
        for i in range(self.tailleX):
            for j in range(self.tailleY):
                self.grille[i][j] = "0"

    def getCases(self): #retourne les coordonnées en pixel des hexagones/cercles sur l'écran
        return self.cases

    def getModel(self):
        return self.model

    def getTurn(self):
        return self.turn

    def nextTurn(self):
        if self.turn == "1":
            self.turn = "2"
        else:
            self.turn = "1"

    def getJoueur1Cases(self):
        cases = []
        for i in range(self.tailleX):
            for j in range(self.tailleY):
                if self.grille[i][j]=='1':
                    cases.append(Case(i , j))
        return cases

    def getJoueur2Cases(self):
        cases = []
        for i in range(self.tailleX):
            for j in range(self.tailleY):
                if self.grille[i][j]=='2':
                    cases.append(Case(i , j))
        return cases

    def getTailleX(self):
        return self.tailleX

    def getTailleY(self):
        return self.tailleY

    def afficherGrille(self):
        lignes = []
        s = ""
        for j in range(self.tailleY):
            for i in range(self.tailleX):
                s = s + str(self.grille[i][j])
            print(s)
            s=""
        print()

    def getOtherPlayer(self, joueur):
        if(joueur == "1"):
            return "2"
        else:
            return "1"

class Case(object):

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


#-----méthodes-----

#-----Méthodes pour connections en lignes
def recieve():
    global joueur , showFT , firstTurn , originalPlayer
    while True:
        data = ''
        data = s.recv(1024).decode()
        d= data.split(" ")
        if d[0]== "j":
            joueur = d[1]
            originalPlayer = d[1]
            print("Client affecté au joueur "+ joueur)
        elif data == "fin":
            s.close()
        elif d[0] == "placer1":
            addCircle(int(d[1]) , int(d[2]) , "1")
            grille.nextTurn()
            unGagnant()
        elif d[0] == "placer2":
            addCircle(int(d[1]) , int(d[2]) , "2")
            grille.nextTurn()
            unGagnant()
        elif d[0] == "placer1f":
            addCircle(int(d[1]) , int(d[2]) , "1")
            grille.nextTurn()
            firstTurn = False
            showSwapButton()
        elif data == "swap":
            joueur = grille.getOtherPlayer(joueur)
            showFT = False
            print("call")
        elif d[0] == "giveup":
            print("Le joueur", grille.getOtherPlayer(d[1]), "a gagné")
            grille.setFinish(True)
            can.itemconfig(texte, text="Le joueur " +grille.getOtherPlayer(d[1])+" a gagné")
            clearCircles()

def send(arg):
    s.send(arg.encode())
    #sleep(1)

def onClosing():
    send("closing")
    fen.destroy()
    sys.exit(0)
#------------------

def giveUp():
    send("giveup")

def caseExist(x , y):
    if x<0 or x >= grille.getTailleX() or y<0 or y >= grille.getTailleY():
        return False
    else:
        return True

def getAdjacentTilesTo(case):      #retourne les cases adjacentes à  celle indiquée
    cases = []
    modelList = []
    if grille.getModel() == "hexagone":
        modelList.append(Case(0,-1))
        modelList.append(Case(1,-1))
        modelList.append(Case(-1,0))
        modelList.append(Case(1,0))
        modelList.append(Case(0,1))
        modelList.append(Case(-1,1))

    for i in range(len(modelList)):
        if(modelList[i].getX()+case.getX() >=0 and modelList[i].getY()+case.getY() >=0 and modelList[i].getX()+case.getX()<grille.getTailleX() and modelList[i].getY()+case.getY()<grille.getTailleY()):
            cases.append(Case(modelList[i].getX()+case.getX() , modelList[i].getY()+case.getY()))
    return cases

def onlyBelongTo(cases , joueur):
    c = []
    if joueur == "1":
        for i in range (len(cases)):
            for j in range(len(grille.getJoueur1Cases())):
                if areCasesEqual(cases[i] , grille.getJoueur1Cases()[j]):
                    c.append(cases[i])
    if joueur == "2":
        for i in range (len(cases)):
            for j in range(len(grille.getJoueur2Cases())):
                if areCasesEqual(cases[i] , grille.getJoueur2Cases()[j]):
                    c.append(cases[i])
    return c

def unGagnant():
    if testSiCheminExiste('1'):
        print("Le joueur 1 a gagné")
        grille.setFinish(True)
        can.itemconfig(texte, text="Joueur 1 a gagné")
        clearCircles()
    elif testSiCheminExiste('2'):
        print("Le joueur 2 a gagné")
        grille.setFinish(True)
        can.itemconfig(texte, text="Joueur 2 a gagné")
        clearCircles()

def testSiCheminExiste(joueur):
    casesATester = []
    casesTestees = []
    casesDeDepart = []
    finished = False
    if joueur == '1':
        for i in range(len(grille.getJoueur1Cases())):     #pour toutes les cases appartenant au joueur 1, on cherche les cases collées aux bords (casesDeDepart)
            if grille.getJoueur1Cases()[i].getX()==0 :
                casesDeDepart.append(grille.getJoueur1Cases()[i])

        for i in range(len(casesDeDepart)):       #pour toutes les cases de départ, si elles n'appartiennent pas deja aux cases testées:
            if not finished:
                if len(casesTestees) != 0:
                    if not listContainCase(casesTestees, casesDeDepart[i]):
                        casesATester.append(casesDeDepart[i])

                else:       #dans le cas ou la liste des cases à tester est vide:
                    casesATester.append(casesDeDepart[i])
                while len(casesATester) !=0:        #tant que la liste des cases à tester n'est pas vide, on cherche des voisins
                            for i in range(len(onlyBelongTo(getAdjacentTilesTo(casesATester[0]) , "1"))):
                                if not listContainCase(casesTestees, onlyBelongTo(getAdjacentTilesTo(casesATester[0]) , "1")[i]) and not listContainCase(casesATester, onlyBelongTo(getAdjacentTilesTo(casesATester[0]) , "1")[i]) and listContainCase(grille.getJoueur1Cases() , onlyBelongTo(getAdjacentTilesTo(casesATester[0]) , "1")[i]):
                                    casesATester.append(onlyBelongTo(getAdjacentTilesTo(casesATester[0]) , "1")[i])
                            casesTestees.append(casesATester[0])
                            casesATester.pop(0)
                if listContainX(casesTestees , 0) and listContainX(casesTestees , grille.getTailleX()-1):
                    finished = True
                    return True
        return False

    elif joueur == '2':
        for i in range(len(grille.getJoueur2Cases())):     #pour toutes les cases appartenant au joueur 2, on cherche les cases collées aux bords (casesDeDepart)
            if grille.getJoueur2Cases()[i].getY()==0:
                casesDeDepart.append(grille.getJoueur2Cases()[i])

        for i in range(len(casesDeDepart)):       #pour toutes les cases de départ, si elles n'appartiennent pas deja aux cases testées:
            if not finished:
                if len(casesTestees) != 0:
                    if not listContainCase(casesTestees, casesDeDepart[i]):
                        casesATester.append(casesDeDepart[i])

                else:       #dans le cas ou la liste des cases à tester est vide:
                    casesATester.append(casesDeDepart[i])
                while len(casesATester) !=0:        #tant que la liste des cases à tester n'est pas vide, on cherche des voisins
                            for i in range(len(onlyBelongTo(getAdjacentTilesTo(casesATester[0]) , "2"))):
                                if not listContainCase(casesTestees, onlyBelongTo(getAdjacentTilesTo(casesATester[0]) , "2")[i]) and not listContainCase(casesATester, onlyBelongTo(getAdjacentTilesTo(casesATester[0]) , "2")[i]) and listContainCase(grille.getJoueur1Cases() , onlyBelongTo(getAdjacentTilesTo(casesATester[0]) , "2")[i]):
                                    casesATester.append(onlyBelongTo(getAdjacentTilesTo(casesATester[0]) , "2")[i])
                            casesTestees.append(casesATester[0])
                            casesATester.pop(0)
                if listContainY(casesTestees , 0) and listContainY(casesTestees , grille.getTailleY()-1):
                    finished = True
                    return True
        return False

def swap():
    global joueur
    send("swap")
    joueur = grille.getOtherPlayer(joueur)
    removeSwapButton()

def showSwapButton():
    global swapButton
    global swapWindow
    swapButton = Button(text = "Echanger" , command = swap, anchor = W)
    swapButton.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    swapWindow = can.create_window(1050, 300, anchor=NW, window=swapButton)

def removeSwapButton():
    global swapButton
    global swapWindow
    can.delete(swapButton)
    can.delete(swapWindow)
    showFT = False

def giveUp():
    send("giveup")

def addCircle(x , y , joueur):
    global circles
    grille.placer(Case(x, y) , joueur)
    if joueur=="1":
        i = can.create_circle(grille.getCases()[x][y].getX() , grille.getCases()[x][y].getY() , 32 , fill="blue")
    else:
        i = can.create_circle(grille.getCases()[x][y].getX() , grille.getCases()[x][y].getY() , 32 , fill="red")
    circles.append(i)

def clearCircles():
    global circles , firstTurn , showFT , originalPlayer , joueur
    for i in range(len(circles)):
        can.delete(circles[i])
    circles[:] = []
    grille.clearGrid()
    grille.setFinish(False)
    firstTurn = True
    showFT = True
    originalPlayer = grille.getOtherPlayer(originalPlayer)
    joueur = str(originalPlayer)
    if grille.getTurn()=="2":
        grille.nextTurn()

def displayCases(caseList):
    for i in range(len(caseList)):
        print(caseList[i].getX() , caseList[i].getY())

def areCasesEqual(case1 , case2):       #return True si case1 et case2 ont les memes coordonnées
    if(case1.getX() == case2.getX() and case1.getY() == case2.getY()):
        return True
    else:
        return False

def areCasesSameX(x1 , x2):     #return True si x1 et x2 sont égaux
    if x1 == x2:
        return True
    else:
        return False

def areCasesSameY(y1 , y2):     #return True si y1 et y2 sont égaux
    if y1 == y2:
        return True
    else:
        return False

def listContainCase(list , case):       #return True si la liste contient une case avec les coordonnées spécifiées
    for i in range(len(list)):
        if(areCasesEqual(list[i], case)):
            return True
    return False

def listContainX(list , x):      #return True si la liste contient une case avec une valeur x spécifiée
    for i in range(len(list)):
        if(areCasesSameX(list[i].getX(), x)):
            return True
    return False

def listContainY(list , y):     #return True si la liste contient une case avec une valeur y spécifiée
    for i in range(len(list)):
        if(areCasesSameY(list[i].getY(), y)):
            return True
    return False

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle


def Clic(event):
    global joueur , firstTurn
    X = event.x
    Y = event.y
    for i in range(len(grille.getCases())):
        for j in range(len(grille.getCases()[0])):
            if sqrt((X-grille.getCases()[i][j].getX())**2+(Y-grille.getCases()[i][j].getY())**2)<grille.getRadius():
                if grille.getGrid()[i][j]=="0" and not grille.isFinished():
                    print(grille.getTurn())
                    if grille.getTurn()==joueur:
                        if joueur == "1":
                            if firstTurn == True:
                                addCircle(i , j , "1")
                                firstTurn = False
                                a = "placer1f " + str(i) + " " + str(j)
                                send(a)
                            else:
                                addCircle(i , j , "1")
                                a ="placer1 " + str(i) + " " + str(j)
                                send(a)

                        elif joueur == "2":
                            if showFT:
                                removeSwapButton()
                            addCircle(i , j , "2")
                            a ="placer2 " + str(i) + " " + str(j)
                            send(a)
                        grille.nextTurn()

##                    else:
##                        can.create_circle(grille.getCases()[i][j].getX() , grille.getCases()[i][j].getY() , grille.getRadius() , fill="red")
##                        grille.placer(Case(i, j) , '2')
##                        grille.nextTurn()

                    unGagnant()

def fillBoard(x , y, shiftX, shiftY):
    xshift2 = 0
    for j in range(y):
        for i in range(x):
            can.create_circle(i*70+shiftX+xshift2, j*60+shiftY , 32 , fill="grey")
            grille.setCase(i, j, Case(i*70+shiftX+xshift2, j*60+shiftY))
        xshift2+=32

def bordRougeBleu(x,y):
    can.create_rectangle(0,0,20,800,fill="blue")
    can.create_rectangle(1180,0,1200,800,fill="blue")
    can.create_rectangle(0,0,1200,20,fill="red")
    can.create_rectangle(0,800,1200,780,fill="red")

#-------------début du programme-------------

x,y = 11,11
global joueur, swapButton , swapWindow , firstTurn , showFT , originalPlayer
firstTurn , showFT = True , True
joueur = "0"

fen = Tk()
can = Canvas(fen, width=1200, height=800, bg='ivory')
can.pack(side=TOP)

grille = Grille(x , y , 32 , "hexagone")                #1= horizontal , 2 = vertical
global circles
circles = []

fillBoard(x , y , 60 , 60)
bordRougeBleu(x , y)
texte = can.create_text(1050 , 50 , font=('Helvetica' , 20) ,text="")

##addCircle(1 , 1 , "2")
##addCircle(1 , 3 , "2")
##print(len(onlyBelongTo(getAdjacentTilesTo(Case(1 , 2)) , "2")))

#ip = input("adresse ip: ")
ip="172.16.202.7"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.gethostname()
port =25565
s.connect((ip,port))

fen.protocol("WM_DELETE_WINDOW", onClosing)

thread1 = Thread(target = recieve)
thread1.start()

send("connection")

button1 = Button(text = "Abandonner" , command = giveUp, anchor = W)
button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
button1_window = can.create_window(1050, 250, anchor=NW, window=button1)

can.bind('<Button-1>', Clic)
fen.mainloop()




##frame = Frame(can, bg='grey', width=400, height=40)
##frame.pack(fill='x')
##button1 = Button(frame, text='Add Rect')
##button1.pack(side='left', padx=10)


##i = w.create_line(xy, fill="red")
##
##w.coords(i, new_xy) # change coordinates
#w.itemconfig(i, fill="blue") # change color
##
##w.delete(i) # remove
##
##w.delete(ALL) # remove all items