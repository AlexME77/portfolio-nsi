from tkinter import *
import random


def verif():
    global nombre, saisie
    try:
        valeur=int(saisie.get())
        if not 1<=valeur<=100:
            label.config(text="Entrer un nombre entre 1 et 100")
        elif valeur>nombre:
            label.config(text="Plus petit")
        elif valeur<nombre:
            label.config(text="Plus grand")
        elif valeur==nombre:
            label.config(text="T'as gagné")
        
    except ValueError:
        label.config(text="Entrer un nombre")

fenetre = Tk()
fenetre.geometry("400x300")
fenetre.title("Nombre secret")

nombre=random.randint(1, 100)
print(nombre)

texte = Label(fenetre, text='Quel est le nombre ?', height=3)
texte.pack()

affichage = StringVar()



label = Label(fenetre, text="", width=30, fg='red', bg='grey')
label.pack()



saisie = StringVar()

entree = Entry(fenetre, textvariable=saisie, width=30)
entree.pack()


bouton_afficher = Button(fenetre, text='Tester', command=verif)
bouton_afficher.pack()

fermer = Button(fenetre, text="Quitter le jeu", command=fenetre.destroy)
fermer.pack(side=BOTTOM)

fenetre.mainloop()