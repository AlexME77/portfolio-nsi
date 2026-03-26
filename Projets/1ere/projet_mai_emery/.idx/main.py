# Consignes : charger le csv, lister, supprimer, ajouter ou modifier des données, faire une fonction par personne (ex : tous les films que j'ai pas vu, ...)
# Demander au prof pour la recherche si c'est nécessaire

import csv
import fonctions
import menu

def run():
    '''
    Fonction de lancement du programme
    '''
    # Demande à l'utilisateur de choisir une base de données
    films = menu.data()
    # Trie le tableau selon le nom
    fonctions.tri_dictionnaire_croissant(films, "nom")
    # Demande à l'utilisateur de choisir un traitement
    reponse=0
    while not 1<=reponse<=6:    
        try:
            reponse = menu.demande()
            if reponse == 1:
                menu.lister(films)
            elif reponse == 2:
                menu.infos(films)
            elif reponse == 3:
                menu.ajouter(films)
            elif reponse == 4:
                menu.modifier(films)
            elif reponse == 5:
                menu.supprimer(films)
            elif reponse == 6:
                menu.sauvegarder(films)
                exit()
            else:
                print('\nLe choix doit être compris entre 1 et 6, réessayer')
        except ValueError:
            print('\nLe choix doit être compris entre 1 et 6, réessayer')
        reponse=0

run()