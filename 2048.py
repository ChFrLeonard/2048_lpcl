import numpy as np
#from getkey import getkey, keys
from tkinter import *

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

def init_grid():
    grid = np.zeros ((nbLigne,nbCol), dtype = int)
    r = np.random.choice ([0,1,2,3],2, replace = False)
    c = np.random.choice ([0,1,2,3],2)
    v = np.random.choice ([2,4],2, replace = True, p = [0.8,0.2])
    grid [r[0],c[0]] = v[0]
    grid [r[1],c[1]] = v[1]
    return grid

def rollLeft():
    rollin(maMatrice, "left")

def rollRight():
    rollin(maMatrice, "right")

def rollUp():
    rollin(maMatrice, "up")

def rollDown():
    rollin(maMatrice, "down")

def add_new (grid):
    grid2 = grid
    NewMatrix = grid2
    result = (np.where(grid2==0))
    listCoordinates= list(zip(result[0], result[1]))
    element_list = np.random.randint (0,len(listCoordinates), dtype = int)
    v = np.random.choice ([2,4], p = [0.8,0.2])
    grid [listCoordinates [element_list-1]] = v
    return (grid2)


def rollin(grid, direction):
    nbDecal +=1
    if direction == "u":
        grid2 = np.rot90(grid,1)
        i=0
        while i < nbLigne:
            grid2[i,:] = rollin_row(grid2[i,:])
            i+=1
        grid2 = np.rot90(grid2,3)
        nbH +=1

    elif direction == "d":
        grid2 = np.rot90(grid,3)
        i=0
        while i < nbLigne:
            grid2[i,:] = rollin_row(grid2[i,:])
            i+=1
        grid2 = np.rot90(grid2,1)
        nbB +=1

    elif direction == "l":
        i=0
        while i < nbLigne:
            grid2[i,:] = rollin_row(grid2[i,:])
            i+=1

        nbG +=1
    elif direction == "r":
        grid2 = np.rot90(grid,2)
        i=0
        while i < nbLigne:
            grid2[i,:] = rollin_row(grid2[i,:])
            i+=1
        grid2 = np.rot90(grid,2)
        nbD +=1
    else:
        print("planté")

def rollin_row(row):
    i=0 #on calle tout a gauche
    while i< len(row):
        if row[i] == 0:
            posvide = i
            k = i
            while row[k] == 0 and k < len(row):
                k+=1
            row[posvide] = row[k]
            row[k] = 0
            i=posvide + 1
        else:
            i+=1

    while row[i] != 0 or i < len(row):
        if row[i] == row[i+1]:
            row[i] += row[i]
            k = i+1
            while k != 0 or k < len(row): 
                row[k] = row[k+1]
                k += 1
            if k == len(row)-1:
                row[k] = 0
        else:
            k=i
            while k < len(row):
                row[k] = row [k+1]
        i+=1
    return row

def laLoose(grid):
    perdu = True
    i=0
    while i< nbLigne:
        if grid[i] == grid[i+1]: 
            perdu = False
    return perdu

nbLigne = 4
nbCol = 4
maMatrice = init_grid()

interface = Tk()
interface.geometry ("600x400")
titre = interface.title("2048")

#definition des frames
frm2048 = Frame(interface, width = 300, height=400)
frm2048.pack(side=RIGHT, expand=True, padx=10,pady=10)
#frm20482 = Frame(frm2048, width = 300, height=150)
#frm20482.pack(fill="both", expand=True, padx=10,pady=10)

frmBtn = Frame(interface, background='#D9D9D9', width = 300, height=400)
frmBtn.pack(side=LEFT, expand=True, padx=10,pady=10)
frmBtn1 = Frame(frmBtn, background='#D9D9D9', width = 400)
frmBtn1.pack(padx=5,pady=5, side=TOP)
frmBtn2 = Frame(frmBtn, width = 300)
frmBtn2.pack(padx=5,pady=5, side=BOTTOM)

lblScore = Label(frmBtn1, width = 10, height=1, text='Score').grid(row=0,column=0)
lblScore1 = Label(frmBtn1, width = 20, height=1, textvariable='0000').grid(row=0,column=1, columnspan=2)

lblScore1 = Label(frmBtn1,bg='#D9D9D9', width = 5, height=0, textvariable='0000').grid(row=1,column=2)

buttonHaut = Button(frmBtn1, text="Haut", command=rollUp, width = 10).grid(row=2, column=1)
buttonGauche = Button(frmBtn1, text="Gauche", command=rollLeft, width = 10).grid(row=3,column=0)
buttonDroite = Button(frmBtn1, text="Droite", command=rollRight, width = 10).grid(row=3,column=2)
buttonBas = Button(frmBtn1, text="Bas", command=rollDown, width = 10).grid(row=4, column=1)

#definition du graphe
fig = Figure(figsize=(5, 4), dpi=25)
t = np.arange(0, 3, .01)
ax = fig.add_subplot()
line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
ax.set_xlabel("time [s]")
ax.set_ylabel("f(t)")

#dessin des graphes
canvas = FigureCanvasTkAgg(fig, master=frmBtn2)  # A tk.DrawingArea.
canvas.draw()
canvas1 = FigureCanvasTkAgg(fig, master=frmBtn2)  # A tk.DrawingArea.
canvas1.draw()

#buttonHaut.pack(ipadx=20,ipady=10, pady=10, padx=10, side=TOP)
#buttonGauche.pack(ipadx=20,ipady=10, padx=10, pady=10, side=LEFT)
#buttonDroite.pack(ipadx=20,ipady=10, padx=10, pady=10, side=RIGHT)
#buttonBas.pack(ipady=20, ipadx=10, pady=10, padx=10, side=BOTTOM)

#buttonHaut.grid(row=0, column=1)
#buttonGauche.grid(row=1,column=0)
#buttonDroite.grid(row=1,column=2)
#buttonBas.grid(row=2, column=1)

for ligne in range(nbLigne):
    for colonne in range(nbCol):
        valeur = maMatrice[ligne,colonne]
        Label(frm2048, text='%s' % valeur, borderwidth=15, background="green").grid(row=ligne, column=colonne)

canvas.get_tk_widget().grid(row=0,column=0)
canvas1.get_tk_widget().grid(row=0,column=1)

interface.mainloop()
#interface.bind("<Up>", rollUp) # Flèche haut

 




def decaleEtSomme(maMatrice, nbLigne, nbCol):
    i=nbLigne   #on netoie les vides
    while i >= 0:
        j= nbCol
        while j > 0:
            if maMatrice[i,j] == 0:
                posVide = j
                k=j
                while maMatrice[i,k] == 0 and k > 0:
                    k-=1
                maMatrice[i,posVide] = maMatrice[i,k]
                maMatrice[i,k] = 0
                j=posVide+1
            else:
                j-=1
        i-=1

    i=0 #une fois que toutes les valeurs sont a gauche
    while i < nbLigne:
        j=0
        while j < nbCol:    
            if maMatrice[i,j] == maMatrice[i,j+1]:   #si on est égal : on somme
                maMatrice[i,j] += maMatrice[i,j]
                k=j+1 #et on décale les suivants
                while k <nbCol:
                    if k>=0:
                        maMatrice[i,k-1] = maMatrice[i,k] 
                    if k ==  nbCol-1:
                        maMatrice[i,k-1] = 0
                    k+=1
            else: #si on est différents:
                k=j #et on décale les suivants
                while k <nbCol:
                    if k>=0:
                        maMatrice[i,k-1] = maMatrice[i,k] 
                    k+=1
            j+=1
        i+=1