#-*-coding: utf-8 -*-

class Case(object):

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y



#-----méthodes-----

tailleX, tailleY = 4 , 4    #nombre de colones et lignes
grille = [[0 for x in range(tailleX)] for y in range(tailleY)]  #grille du jeu
model = "hexagone"      #correspond au type de case utilisée

def afficherTableau():  #affiche le tableau
    lignes = []
    s = ""
    for j in range(tailleY):
        for i in range(tailleX):
            s = s + str(grille[i][j])
        print(s)
        s = ""
    print()

def placerPoint(x , y , joueur):    #place un point de valeur joueur aux coordonnées x y
    grille[x][y] = joueur


def caseExist(x , y):
    if x<0 or x >= tailleX or y<0 or y >= tailleY:
        return False
    else:
        return True

def getAdjacentTilesTo(x , y):      #retourne les cases adjacentes à  celle indiquÃƒÆ’Ã‚Â©e
    cases = []
    modelList = []
    if model == "hexagone":
        modelList.append(Case(-1,1))
        modelList.append(Case(0,1))
        modelList.append(Case(-1,0))
        modelList.append(Case(1,0))
        modelList.append(Case(0,-1))
        modelList.append(Case(0,1))
    for i in range(len(modelList)):
        c = modelList[i]

        if(caseExist(c.)


    return cases


#-------------début du programme-------------

for i in range(tailleY):
    for j in range(tailleY):
        grille[i][j]=0

afficherTableau()

entree = ""
inp = ""
entree = input("Entrer une commande")
inp = entree.split(" ")
c = Case(1 , 2)
print(c.getX())
while (inp[0] != "exit"):       #boucle principale
    if inp[0] == "placer" and len(inp) == 4:
        placerPoint(int(inp[1]), int(inp[2]) , int(inp[3]))

    elif inp[0] == "aff":
        afficherTableau()

    entree = input("Entrer une commande")
    inp = entree.split(" ")



