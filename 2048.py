import numpy as np
#from getkey import getkey, keys
from tkinter import *

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

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

buttonHaut = Button(frmBtn1, text="Haut", command="rollUp", width = 10).grid(row=2, column=1)
buttonGauche = Button(frmBtn1, text="Gauche", command="rollLeft", width = 10).grid(row=3,column=0)
buttonDroite = Button(frmBtn1, text="Droite", command="rollRight", width = 10).grid(row=3,column=2)
buttonBas = Button(frmBtn1, text="Bas", command="rollDown", width = 10).grid(row=4, column=1)

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