from tkinter import *
from random import randint

# Ajouter les lignes de code permettant de créer une fenêtre :
# - de dimension "200x100" ;
# - ayant pour titre "Dé virtuel".
fenetre = Tk()
fenetre.geometry("400x300")
fenetre.title("Lancer de dés")

# Composant d'affichage du résultat du lancé
label = Label(fenetre, text="Appuyez sur lancer", fg="RoyalBlue1")
label.pack(padx=10, pady=10)


# Fonction qui tire un nombre aléatoire entre 1 à 6.
def lancer_de():
    """ Tire un nombre aléatoire entre 1 et 6 et modifie le texte de label pour afficher le résultat"""
    label.config(text=randint(1,6))


# Bouton "lancer"
bouton_lancer = Button(fenetre, text="Lancer", command=lancer_de)
bouton_lancer.pack(side=TOP)

# Bouton "Quitter"
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton_quitter.pack(side=BOTTOM)

# Gestionnaire d'événements
fenetre.mainloop()
