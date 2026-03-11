# Importe les classes du module tkinter
from tkinter import *
# Crée la fenêtre principale de l'application
fenetre = Tk()
# Crée la fenêtre principale de l'application
fenetre.title("Salut")
# Affiche du texte en bleu
label = Label(fenetre, text="Bonjour à tous !", fg="blue")
# Taille de la fenêtre par rapport au texte
label.pack(padx=100, pady=100)
# Ajoute un bouton avec du texte qui ferme la fenêtre
bouton = Button(fenetre, text="Au revoir...", command=fenetre.destroy)
# Position du bouton par rapport à la fenêtre
bouton.pack(side=BOTTOM)
# Lance le gestionnaire d'événements
fenetre.mainloop()