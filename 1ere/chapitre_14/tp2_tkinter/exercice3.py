from tkinter import *


def quitter_application():
    """Fonction utilisée comme commande à appeler au clic sur le bouton"""
    global fenetre
    fenetre.destroy()


def changer_texte():
    """Modifie le texte du composant label"""
    label.config(text="Au revoir !")


# Initialisation de l'application
fenetre = Tk()
fenetre.title("Mon application")

# Ajout d'un texte
label = Label(fenetre, text="Bonjour !")
label.pack(padx=100, pady=100)

# Ajout d'un bouton
bouton = Button(fenetre, text="Quitter", command=changer_texte)
bouton.pack(padx=10, pady=10)

# Gestionnaire d'événements
fenetre.mainloop()
