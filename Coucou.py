def voisin(grille,tailleX,tailleY):
    for x,y in ((-1,0),(1,0),(0,-1),(0,1)) :
        if 0<= tailleX-x<10 & 0<= tailleY-y<10:
            if grille[tailleX-x,tailleY-y]==1:
                return True
            if grille[tailleX-x,tailleY-y]==2:
                return True
    return False
def Victoire_1():
    for v in range(tailleX):
        if grille[tailleX-x,tailleY-y]==1:
            return True
        else:
            return False



def Victoire_2():
    gg





def voisin(tableau,col,lig) :
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)) : #On parcourt les voisins
        if 0<=col+dx<50 & 0<=lig+dy<50:
            if tableau[col+dx,lig+dy]==2 :
                return True #On retourne VRAI si voisin rouge
    return False #On retourne FAUX dans la cas contraire
