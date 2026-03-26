# Importe les classes du module tkinter
from tkinter import *

# Crée la fenêtre principale de l'application
fenetre = Tk()
# Fixe le titre de la fenêtre
fenetre.title("Coucou")
# Fixe les dimensions de la fenêtre à 400 pixels de largeur et 300 pixels de hauteur
fenetre.geometry("400x300+300+500")
# Lance le gestionnaire d'événements
fenetre.mainloop()
