#-*-coding: utf-8 -*-

class Grille(object):

    def __init__(self , x , y , model):
        self.tailleX = x
        self.tailleY = y
        self.model = model
        self.grille = [[0 for x in range(self.tailleX)] for y in range(self.tailleY)]

    def placer(self , case , joueur):
        self.grille[case.getX()][case.getY()] = joueur

    def getGrid(self):
        return self.grille

    def getModel(self):
        return self.model

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

class Case(object):

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

#-----méthodes-----


def caseExist(x , y):
    if x<0 or x >= grille.getTailleX() or y<0 or y >= grille.getTailleY():
        return False
    else:
        return True

def getAdjacentTilesTo(case):      #retourne les cases adjacentes à  celle indiquée
    cases = []
    modelList = []
    if grille.getModel() == "hexagone":
        modelList.append(Case(-1,-1))
        modelList.append(Case(0,-1))
        modelList.append(Case(-1,0))
        modelList.append(Case(1,0))
        modelList.append(Case(0,1))
        modelList.append(Case(1,1))

    for i in range(len(modelList)):
        if(modelList[i].getX()+case.getX() >=0 and modelList[i].getY()+case.getY() >=0 and modelList[i].getX()+case.getX()<grille.getTailleX() and modelList[i].getY()+case.getY()<grille.getTailleY()):
            cases.append(Case(modelList[i].getX()+case.getX() , modelList[i].getY()+case.getY()))
    return cases

def unGagnant():
    if not testSiCheminExiste('1'):
        if not testSiCheminExiste('2'):
            return False
    return True

def testSiCheminExiste(joueur):
    casesATester = []
    casesTestees = []
    casesDeDepart = []
    finished = False
    if joueur == '1':
        for i in range(len(grille.getJoueur1Cases())):     #pour toutes les cases appartenant au joueur 1, on cherche les cases collées aux bords (casesDeDepart)
            if grille.getJoueur1Cases()[i].getX()==0 or grille.getJoueur1Cases()[i].getX()==grille.getTailleX()-1:
                casesDeDepart.append(grille.getJoueur1Cases()[i])

        for i in range(len(casesDeDepart)):       #pour toutes les cases de départ, si elles n'appartiennent pas deja aux cases testées:
            if not finished:
                if len(casesTestees) != 0:
                    if not listContainCase(casesTestees, casesDeDepart[0]):
                        casesATester.append(casesDeDepart[0])
                        while len(casesATester) !=0:        #tant que la liste des cases à tester n'est pas vide, on cherche des voisins
                            for i in range(len(getAdjacentTilesTo(casesATester[0]))):
                                if not listContainCase(casesTestees, getAdjacentTilesTo(casesATester[0])[i]) and not listContainCase(casesATester, getAdjacentTilesTo(casesATester[0])[i]) and listContainCase(grille.getJoueur1Cases() , getAdjacentTilesTo(casesATester[0])[i]):
                                    casesATester.append(getAdjacentTilesTo(casesATester[0])[i])
                            casesTestees.append(casesATester[0])
                            casesATester.pop(0)

                else:       #dans le cas ou la liste des cases à tester est vide:
                    casesATester.append(casesDeDepart[0])
                    while len(casesATester) !=0:        #tant que la liste des cases à tester n'est pas vide, on cherche des voisins
                        for i in range(len(getAdjacentTilesTo(casesATester[0]))):
                            if not listContainCase(casesTestees, getAdjacentTilesTo(casesATester[0])[i]) and not listContainCase(casesATester, getAdjacentTilesTo(casesATester[0])[i]) and listContainCase(grille.getJoueur1Cases() , getAdjacentTilesTo(casesATester[0])[i]):
                                casesATester.append(getAdjacentTilesTo(casesATester[0])[i])
                        casesTestees.append(casesATester[0])
                        casesATester.pop(0)
                if listContainX(casesTestees , 0) and listContainX(casesTestees , grille.getTailleX()-1):
                    finished = True
                    return True
        return False

    elif joueur == '2':
        for i in range(len(grille.getJoueur2Cases())):     #pour toutes les cases appartenant au joueur 2, on cherche les cases collées aux bords (casesDeDepart)
            if grille.getJoueur2Cases()[i].getY()==0 or grille.getJoueur2Cases()[i].getY()==grille.getTailleY()-1:
                casesDeDepart.append(grille.getJoueur2Cases()[i])

        for i in range(len(casesDeDepart)):       #pour toutes les cases de départ, si elles n'appartiennent pas deja aux cases testées:
            if not finished:
                if len(casesTestees) != 0:
                    if not listContainCase(casesTestees, casesDeDepart[0]):
                        casesATester.append(casesDeDepart[0])
                        while len(casesATester) !=0:        #tant que la liste des cases à tester n'est pas vide, on cherche des voisins
                            for i in range(len(getAdjacentTilesTo(casesATester[0]))):
                                if not listContainCase(casesTestees, getAdjacentTilesTo(casesATester[0])[i]) and not listContainCase(casesATester, getAdjacentTilesTo(casesATester[0])[i]) and listContainCase(grille.getJoueur2Cases() , getAdjacentTilesTo(casesATester[0])[i]):
                                    casesATester.append(getAdjacentTilesTo(casesATester[0])[i])
                            casesTestees.append(casesATester[0])
                            casesATester.pop(0)

                else:       #dans le cas ou la liste des cases à tester est vide:
                    casesATester.append(casesDeDepart[0])
                    while len(casesATester) !=0:        #tant que la liste des cases à tester n'est pas vide, on cherche des voisins
                        for i in range(len(getAdjacentTilesTo(casesATester[0]))):
                            if not listContainCase(casesTestees, getAdjacentTilesTo(casesATester[0])[i]) and not listContainCase(casesATester, getAdjacentTilesTo(casesATester[0])[i]) and listContainCase(grille.getJoueur2Cases() , getAdjacentTilesTo(casesATester[0])[i]):
                                casesATester.append(getAdjacentTilesTo(casesATester[0])[i])
                        casesTestees.append(casesATester[0])
                        casesATester.pop(0)
                if listContainY(casesTestees , 0) and listContainY(casesTestees , grille.getTailleY()-1):
                    finished = True
                    return True
        return False

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

#-------------début du programme-------------

grille = Grille(4 , 4 , "hexagone")

grille.placer(Case(0 , 0) , '2')
grille.placer(Case(1 , 1) , '2')
grille.placer(Case(2 , 2) , '2')
grille.placer(Case(3 , 3) , '2')

grille.afficherGrille()

entree = input("Entrer une commande")
inp = entree.split()


while (inp[0] != "exit"):       #boucle principale
    if inp[0] == "placer" and len(inp) == 4:
        grille.placer(Case(int(inp[1]), int(inp[2])) , inp[3])
        print("partie pour un des deux joueurs :", unGagnant())
        grille.afficherGrille()

    elif inp[0] == "aff":
        grille.afficherGrille()

    entree = input("Entrer une commande")
    inp = entree.split()



