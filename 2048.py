import numpy as np
#from getkey import getkey, keys
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd
import csv
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
#Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


#pieuvre
""" value_mvt = [cpt_right/cpt,cpt_up/cpt,cpt_left/cpt,cpt_down/cpt]
angles = [n/float(nb_cat) * 2 * np.pi for n in range(nb_cat)]
angles += angles [:1]
ax = plt.subplot(111, polar = True)
plt.xticks(angles[:-1], cat)
ax.set_rlabel_position(0)
plt.yticks([0.25, 0.5, 0.75, 1], ["25%", "50%", "75%", "100%"], color="grey", size=6)    # size : taille caracteres legende
plt.ylim(0, 1)
value_mvt += value_mvt[:1]
ax.plot(angles, value_mvt, linewidth=1, linestyle="solid")
ax.fill(angles, value_mvt, 'b', alpha=0.9)                                    # alpha : parametre de profondeur de couleur
plt.title ("Mouvements de la partie")
plt.show()
 """
#histo
""" fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
etiquettes = ["RIGHT","UP","LEFT","DOWN"]
valeurs = [cpt_right,cpt_up,cpt_left,cpt_down]
#Affichage des données
ax.bar(etiquettes, valeurs, color=["red", "blue", "green", "grey"], edgecolor="black")
plt.title ("Histogramme des mouvements")
plt.ylabel ("Nombre de mouvements")
plt.xlabel ("Nature du mouvement")
plt.show() """

# Structure du fichier CSV :
# - gagnant (booléen True False)
# - score : résultat final de la partie
# - compteur : nb de mvtds la partie
# - cpt-right : nb de fois ou fleche droite activée
# - cpt-up : nb de fois ou fleche up activée
# - cpt-left : nb de fois ou fleche left activée
# - cpt-down : nb de fois ou fleche down activée
# On créé un camembert à 2 tranches : % de parties gagnées ou perdues sur la base de la zone gagnant du fichier csv
#with open("C:/Users/saphi/OneDrive/Documents/jeu2048.csv","a",newline="") as fichiercsv:
#    writer=csv.writer(fichiercsv)
#    writer.writerow([False,890,40,2,3,10,25])



def decal_line (grid,line,col):
    for i in range (line,3):
        w = i
        if grid [i, col] == 0 and w <= 3:
            while w < 3 and grid [w,col] == 0:
                w = w + 1    
            grid [i,col] = grid [w,col]
            grid [w,col] = 0
    return (grid)

def moove_up (grid): # ajout 2 par 2 et decal 
    for col in range (0,4): 
        for line in range (0,3):
            if grid [line,col] == 0:
                decal_line (grid,line, col)
            if grid [line,col] != 0 and grid [line+1,col] == 0:
                decal_line(grid, line+1, col)   
            if grid [line,col] == grid [line+1,col] and grid [line,col] != 0 and line < 3:
                grid [line,col] += grid [line+1, col]
                grid [line+1,col] = 0
    #print (grid, 'apres additions suite mvt UP', "\n")
    return (grid)
#moove = "right"

def rollUp(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, perdu, score):
    print ("up")
    moove_up (grid)
    perdu=laLoose(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, score)
    cpt_up +=1
    cpt +=1
    grid = add_new(grid)
    score += grid.sum()
    afficherValeur(n,grid)

def rollDown(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, perdu, score):
    print ("down")
    grid = np.rot90 (grid,2)
    moove_up (grid)
    perdu=laLoose(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, score)
    grid = np.rot90 (grid,2)
    cpt_down += 1
    cpt +=1
    grid = add_new(grid)
    score += grid.sum()
    afficherValeur(n,grid)

def rollRight(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, perdu, score):
    print("right")
    grid = np.rot90 (grid,1)
    moove_up (grid)
    perdu=laLoose(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, score)
    grid = np.rot90 (grid,3)
    cpt_right +=1
    cpt +=1
    grid = add_new(grid)
    score += grid.sum()
    afficherValeur(n,grid)

def rollLeft(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, perdu, score):
    print(grid)
    grid = np.rot90 (grid,3)
    moove_up (grid)
    perdu=laLoose(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, score)
    grid = np.rot90 (grid)
    print(grid)
    cpt_left +=1
    cpt +=1
    grid = add_new(grid)
    score += grid.sum()
    afficherValeur(n,grid)
    
def laLoose(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, score):
    perdu = True
    for col in range (0,4): 
        for line in range (0,3):   
            if grid [line,col] == grid [line+1,col]:
                perdu = False
    if perdu == True:
        with open("C:/Users/saphi/OneDrive/Documents/jeu2048.csv","a",newline="") as fichiercsv:
            writer=csv.writer(fichiercsv)
            writer.writerow([False,890,40,2,3,10,25])

    return perdu

def afficherValeur(n,grid):
    for ligne in range(n):
        for colonne in range(n):
            valeur = grid[ligne,colonne]
            Label(frm2048, text='%s' % valeur, borderwidth=15, background='#D9D9D9').grid(row=ligne, column=colonne)
            #Label(frm2048, text='%s' % 1, borderwidth=15, background="green").grid(row=ligne, column=colonne)

def add_new (grid):
    grid2 = grid
    NewMatrix = grid2
    result = (np.where(grid2==0))
    listCoordinates= list(zip(result[0], result[1]))
    element_list = np.random.randint (0,len(listCoordinates), dtype = int)
    v = np.random.choice ([2,4], p = [0.8,0.2])
    grid [listCoordinates [element_list-1]] = v
    return (grid2)

def testBtn():
    print("test")

#print (grid, "aprè mvt ", moove, "\n")
#print (np.all (grid[1,:]== 1),"analyse de la ligne1", "\n")
#print (np.all (grid[:,0]== 0),"analyse de la colonne 0" "\n")
#grid2 = np.zeros ((n,n), dtype = int)
#print (np.all (grid2[:,:]== 0),"analyse de toute la matrice a valeur 0" "\n")
#print (np.diag (grid), "\n")

def init_grid (n):
    grid = np.zeros ((n,n), dtype = int)
    row = np.random.choice ([0,1,2,3],2, replace = False)
    col = np.random.choice ([0,1,2,3],2)
    value = np.random.choice ([2,4],2, replace = True, p = [0.8,0.2])
    grid [row[0],col[0]] = value[0]
    grid [row[1],col[1]] = value[1]
    print (row , type(row))
    print (col, type(col))
    print (value, type (value))
    print (grid)
    return grid

n = 4
grid = init_grid(n)
#print (grid, "grid initiale", "\n") # supp 0+cumul+decal vers le haut à partir de l, ttes colonnes, via fonctions
line = 0
cpt_right = 0
cpt_left = 0
cpt_up = 0
cpt_down = 0
cpt = 0
cat = ["RIGHT", "LEFT", "UP", "DOWN"]
nb_cat = len(cat)
perdu = False
score = 0

interface = Tk()
interface.geometry ("600x400")
titre = interface.title("2048")

#definition des frames
frm2048 = Frame(interface, width = 300, height=400)
frm2048.pack(side=RIGHT, expand=True, padx=10,pady=10)
#frm20482 = Frame(frm2048, width = 300, height=150)
#frm20482.pack(fill="both", expand=True, padx=10,pady=10)

afficherValeur(n,grid)

frmBtn = Frame(interface, background='#D9D9D9', width = 300, height=600)
frmBtn.pack(side=LEFT, expand=True, padx=10,pady=10)
frmBtn1 = Frame(frmBtn, background='#D9D9D9', width = 400)
frmBtn1.pack(padx=5,pady=5, side=TOP)
frmBtn2 = Frame(frmBtn, width = 300)
frmBtn2.pack(padx=5,pady=5, side=BOTTOM)
frmBtn3 = Frame(frmBtn, width = 300)
frmBtn3.pack(padx=5,pady=5, side=BOTTOM)

lblScore = Label(frmBtn1, width = 10, height=1, text='Score').grid(row=0,column=0)
lblScore1 = Label(frmBtn1, width = 20, height=1, textvariable='0000').grid(row=0,column=1, columnspan=2)
lblBest = Label(frmBtn1, width = 10, height=1, text='BEST').grid(row=1,column=0)
lblBest1 = Label(frmBtn1, width = 20, height=1, textvariable='0000').grid(row=1,column=1, columnspan=2)

lblScore1 = Label(frmBtn1,bg='#D9D9D9', width = 5, height=0, textvariable='0000').grid(row=2,column=2)

buttonHaut = Button(frmBtn1, text="Haut", command=rollUp(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, perdu, score), width = 10).grid(row=3, column=1)
buttonGauche = Button(frmBtn1, text="Gauche", command=rollLeft(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, perdu, score), width = 10).grid(row=4,column=0)
buttonDroite = Button(frmBtn1, text="Droite", command=rollRight(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, perdu, score), width = 10).grid(row=4,column=2)
buttonBas = Button(frmBtn1, text="Bas", command=rollDown(grid, cpt_left, cpt_right, cpt_up, cpt_down, cpt, perdu, score), width = 10).grid(row=5, column=1)
#buttonBas = Button(frmBtn1, text="Bas", command=testBtn, width = 10).grid(row=5, column=1)

#definition du graphe
#fig = Figure(figsize=(5, 4), dpi=25)
#t = np.arange(0, 3, .01)
#ax = fig.add_subplot()
#line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
#ax.set_xlabel("time [s]")
#ax.set_ylabel("f(t)")

#spider
if cpt > 0:
    value_mvt = [cpt_right/cpt,cpt_up/cpt,cpt_left/cpt,cpt_down/cpt]
else:
    value_mvt = [0,0,0,0]
angles = [n/float(nb_cat) * 2 * np.pi for n in range(nb_cat)]
angles += angles [:1]
fig = plt.figure(figsize=(5, 4), dpi=25)
ax = plt.subplot(111, polar = True)
plt.xticks(angles[:-1], cat)
ax.set_rlabel_position(0)
plt.yticks([0.25, 0.5, 0.75, 1], ["25%", "50%", "75%", "100%"], color="grey", size=6)    # size : taille caracteres legende
plt.ylim(0, 1)
value_mvt += value_mvt[:1]
ax.plot(angles, value_mvt, linewidth=1, linestyle="solid")
ax.fill(angles, value_mvt, 'b', alpha=0.9)                                    # alpha : parametre de profondeur de couleur
plt.title ("Mouvements de la partie")
#plt.show()

#dessin des graphes
canvas = FigureCanvasTkAgg(fig, master=frmBtn2)  # A tk.DrawingArea.
canvas.draw()

#histo
fig = plt.figure(figsize=(5, 4), dpi=25)
ax = fig.add_axes([0,0,1,1])
etiquettes = ["RIGHT","UP","LEFT","DOWN"]
valeurs = [cpt_right,cpt_up,cpt_left,cpt_down]
#Affichage des données
ax.bar(etiquettes, valeurs, color=["red", "blue", "green", "grey"], edgecolor="black")
plt.title ("Histogramme des mouvements")
plt.ylabel ("Nombre de mouvements")
plt.xlabel ("Nature du mouvement")
#plt.show()

canvas1 = FigureCanvasTkAgg(fig, master=frmBtn2)  # A tk.DrawingArea.
canvas1.draw()

### Figure CAMEMBERT selon résultats de plusieurs parties stockées dans fichier CSV (avec ajout d'un enregistrement au fichier CSV a la fin de chaque partie
data = pd.read_csv("C:/Users/saphi/OneDrive/Documents/jeu2048.csv")

""" proportion_gagne = data ['gagnant'].value_counts()
label = proportion_gagne.index
label = ["Parties perdues : dommage !", "Parties gagnées : YES !!!"]
fig = plt.figure(figsize=(5, 4), dpi=25)
plt.pie (proportion_gagne,labels = label)
plt.title ("Mon premier camembert - Proportion de parties gagnées")
plt.legend() """
#plt.show()

""" canvas2 = FigureCanvasTkAgg(fig, master=frmBtn2)  # A tk.DrawingArea.
canvas2.draw()
 """
#buttonHaut.pack(ipadx=20,ipady=10, pady=10, padx=10, side=TOP)
#buttonGauche.pack(ipadx=20,ipady=10, padx=10, pady=10, side=LEFT)
#buttonDroite.pack(ipadx=20,ipady=10, padx=10, pady=10, side=RIGHT)
#buttonBas.pack(ipady=20, ipadx=10, pady=10, padx=10, side=BOTTOM)

#buttonHaut.grid(row=0, column=1)
#buttonGauche.grid(row=1,column=0)
#buttonDroite.grid(row=1,column=2)
#buttonBas.grid(row=2, column=1)

canvas.get_tk_widget().grid(row=0,column=0)
canvas1.get_tk_widget().grid(row=0,column=1)
#canvas2.get_tk_widget().grid(row=1,column=0)
#canvas3.get_tk_widget().grid(row=1,column=1)

interface.mainloop()

#interface.bind("<Up>", rollUp) # Flèche haut