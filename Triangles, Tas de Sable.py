# Dessin d'un damier hexagonal
#from http://www.nymphomath.ch/pj/damiers/hexagones.py
from tkinter import *
import math
from random import randrange
from random import randint
from random import choice
global ListeSommet
ListeSommet=[]
def couleur():
    coul ="#"
    liste = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    for i in range(6):
        coul += choice(liste)
    return coul
def triangle(origine,c,o,coul):
    global ListeSommet
    seg = c/4
    x, y = origine[0], origine[1]
    # hexagone
    if o==1:
        coul =['brown','red','orange','yellow','green','cyan','blue',
                   'violet', 'purple'][randrange(9)]
        can.create_polygon(x, y, x, y+c, x+math.sqrt(3)/2*c, y+c/2, x, y,
        outline = 'black', width = 1, fill = str(coul))
    else:
        coul="white"
        if randint(0,10)<7:
            coul =['brown','red','orange','yellow','green','cyan','blue',
                   'violet', 'purple'][randrange(9)]
        can.create_polygon(x, y, x, y+c, x-math.sqrt(3)/2*c, y+c/2, x, y,
        outline = 'black', width = 1, fill = str(coul))

def ligne_d_triangle(x, y, c, n):
    global ListeSommet
    # dessiner une ligne d'hexagones
    i = 0

    while i < n:
        triangle((x,y),c,0,"red")
        triangle((x,y),c,1,"white")
        ListeSommet=ListeSommet+[[x+ math.sqrt(3)*c/6,y+c/2,1]]+[[x- math.sqrt(3)*c/6,y+c/2,0]] #2/3 centre !!
        x=x+math.sqrt(3)*c
        i+=1





def damier(c, nl,nc):
    n=nc
    # dessiner nl lignes d'hexagones de taille c avec dÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©calage alternÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©
    y = 0
    no_ligne = 0
    while no_ligne < nl:
        if no_ligne%2 == 0:         # une ligne sur deux, on
            y = no_ligne/2*c
            x=0
            ligne_d_triangle(x, y, c, n)                  # commencera la ligne
        else:                       # avec un dÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©calage
            y =no_ligne//2*c+c/2
            x=math.sqrt(3)*c/2
            ligne_d_triangle(x, y, c, n)
        no_ligne += 1






def Clic(event):
    global ListeSommet
    """ Gestion de l'ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©vÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©nement Clic gauche sur la zone graphique """
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    Min=pow(X-ListeSommet[0][0],2)+pow(Y-ListeSommet[0][1],2)
    Oc=ListeSommet[0][2]
    for i in range(len(ListeSommet)):
        if pow(X-ListeSommet[i][0],2)+pow(Y-ListeSommet[i][1],2)<Min:
            if Min<Min1:
                Min1=Min

            Min2
            Min3
            Xc=ListeSommet[i][0]
            Yc=ListeSommet[i][1]
            Oc=ListeSommet[i][2]
            Min=pow(X-ListeSommet[i][0],2)+pow(Y-ListeSommet[i][1],2)


    if Oc==1:
        triangle((Xc-math.sqrt(3)/6*c, Yc-0.5*c), c,1,"white") #centre ou on clic
    else:
        triangle((Xc+math.sqrt(3)/6*c, Yc-0.5*c), c,0,"white") #centre ou on clic
    can.after(500)



c = 40          # taille des carrÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©s circonscrit ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  l'hexagone
nl = 15         # nombre de lignes
nc = 15         # nombre de colonnes
fen = Tk()
can = Canvas(fen, width=c+(nc-1)*0.75*c, height=c+(nl-1)*c/2+1, bg='ivory')
can.pack(side=TOP)
damier(c,nl,nc)

can.bind('<Button-1>', Clic)
fen.mainloop()





