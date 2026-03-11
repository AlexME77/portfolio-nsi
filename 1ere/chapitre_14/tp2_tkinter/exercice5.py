from tkinter import *


def afficher():
    """
    Affecte la saisie utilisateur à affichage
    """
    global affichage, saisie
    affichage.set("Bonjour " + saisie.get() + " !")


fenetre = Tk()
fenetre.title("Salutations")

# Étiquette permettant d'afficher les instructions
texte = Label(fenetre, text='Comment vous appelez-vous ?', height=3)
texte.pack()


# Initialise affichage avec une chaine de caractère vide qui va ensuite changer automatiquement
affichage = StringVar()
# Synchronisation de label avec affichage. Va afficher dans un rectangle de 30 de largeur avec un arrière plan noir la valeur de affichage en jaune
label = Label(fenetre, textvariable=affichage, width=30, fg='yellow', bg='black')
label.pack()

# Initialise saisie avec une chaine de caractère vide qui va ensuite changer automatiquement
saisie = StringVar()
# Demande dans l'entrée et est relié à saisie
entree = Entry(fenetre, textvariable=saisie, width=30)
entree.pack()

# Bouton "Afficher"
bouton_afficher = Button(fenetre, text='Afficher', command=afficher)
bouton_afficher.pack()

# Gestionnaire d'événements
fenetre.mainloop()
