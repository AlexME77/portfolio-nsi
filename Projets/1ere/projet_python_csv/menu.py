import csv
import fonctions

def data():
    '''
    Choix de la base de données
    '''
    # Demande à l'utilisateur s'il veut partir d'une base de données existante ou pas
    nouveau=0
    while not 1<=nouveau<=2:
        try:
            nouveau = int(input("---Choix du fichier à traiter---\n\nVeux-tu partir d'une base de données déja existante (1) ou en créer une nouvelle (2) ? : "))
            # Si l'utilisateur veut partir d'une base de données existante
            if nouveau == 1:
                erreur=True
                while erreur==True:
                    try:
                        fichier = open(str(input("\nDit moi le nom du fichier .csv que tu veux traiter : ")))
                        tab = list(csv.DictReader(fichier)) 
                        for film in tab:
                            film["duree"]=int(film["duree"])
                            film["annee de sortie"]=int(film["annee de sortie"])
                            film["note"]=float(film["note"])
                        return tab
                        erreur=False
                    except FileNotFoundError:
                        print("\nLe fichier n'a pas été trouvé, vérifie que le fichier est bien un fichier .csv, réessayer")
            # Si l'utilisateur veut en créer une nouvelle
            elif nouveau == 2:
                return []
            # Si l'utilisateur n'a pas choisi 1 ou 2
            else:
                print("\nLe choix doit être compris entre 1 et 2, réessayer\n")
        except ValueError:
            print("\nLe choix doit être compris entre 1 et 2, réessayer\n")

def demande():
    '''
    Choix du traitement
    '''
    # Demande à l'utilisateur de choisir un traitement
    return int(input('\n---Choix du traitement---\n\n 1 : Lister les films\n 2 : En savoir plus sur un film\n 3 : Ajouter un nouveau film\n 4 : Modifier une donnée sur un film\n 5 : Supprimer un film\n 6 : Enregistrer et quitter\n\nQue veux-tu faire ? : '))
    
def lister(tab, tri=None):
    """
    Liste les films selon un critère donné (nom, genre, réalisateur, durée, année de sortie, note, vu)

    tab -- tableau de dictionnaires contenant les films sur lequel on veut lister
    tri -- critère de tri (nom, genre, réalisateur, durée, année de sortie, note, vu). 
    """
    # Vérifie si le tableau est vide
    if len(tab)==0:
        print("\nVous n'avez aucunes données pour le moment, ajouter en pour pouvoir faire des traitements")
    else:
        if tri is None:
            while True:
                try:
                    # Affiche la liste des descripteurs pour savoir le critère de tri
                    cle=list(tab[0].keys())
                    print("\n---Liste des descripteurs---\n")
                    for indice in range(len(cle)):
                        print(indice+1, ":", cle[indice].capitalize())
                    # Demande à l'utilisateur de choisir un critère de tri
                    tri=int(input("\nSelon quel critère veux-tu lister les films ? : "))
                    if 1 <= tri <= 7:
                        break
                    # Si le critère de tri est invalide, affiche un message d'erreur et recommence
                    else:
                        print('Le choix doit être compris entre 1 et 6, réessayer')
                # Si la saisie de l'utilisateur n'est pas un nombre entier, affiche un message d'erreur et recommence
                except ValueError:
                    print('\nLe choix doit être compris entre 1 et 6, réessayer')
        # Trie le tableau selon le critère de tri
        if tri==1:
            print("\n---Liste des films---\n")
            for indice in range(len(tab)):
                print(indice+1, ":", tab[indice]["nom"])
        elif tri==2:
            liste_genre=[]
            genre=0
            while not 1<=genre<=len(liste_genre):
                try:
                    # Parcourt le tableau pour trouver la liste de tous les genres
                    for indice in range(len(tab)):
                        if tab[indice]["genre"] not in liste_genre:
                            liste_genre.append(tab[indice]["genre"])
                    # Affiche la liste des genres pour savoir quel genre de film on veut voir
                    print("\n---Liste des genre---\n")
                    for indice in range(len(liste_genre)):
                        print(indice+1, ":", liste_genre[indice])
                    # Demande à l'utilisateur de choisir un genre
                    genre=int(input("\nQuelle genre de film veux-tu voir ? : "))
                    # Convertion du nombre en genre
                    choix=None
                    for indice in range(len(liste_genre)):
                        if genre==indice+1:
                            choix=liste_genre[indice]
                    # Si le genre n'est pas valide, affiche un message d'erreur et recommence
                    if choix==None:
                        print("\nLe choix doit être compris entre 1 et", len(liste_genre), "réessayer")
                    else:
                        # Affiche la liste des films du genre choisi
                        print('\n---Liste des films du genre :', choix+'---\n')
                        for indice in range(len(tab)):
                            if tab[indice]["genre"]==choix:
                                print(indice+1, ":", tab[indice]["nom"])
                # Si la saisie de l'utilisateur n'est pas un nombre entier, affiche un message d'erreur et recommence
                except ValueError:
                    print("\nLe choix doit être compris entre 1 et", len(liste_genre), "réessayer")
        elif tri==3:
            real=0
            liste_real=[]
            while not 1<=real<=len(liste_real):
                try:
                    # Parcourt le tableau pour trouver la liste de tous les réalisateurs
                    for indice in range(len(tab)):
                        if tab[indice]["realisateur"] not in liste_real:
                            liste_real.append(tab[indice]["realisateur"])
                    # Affiche la liste des réalisateurs pour savoir quel réalisateur de film on veut voir
                    print("\n---Liste des réalisateurs---\n")
                    for indice in range(len(liste_real)):
                        print(indice+1, ":", liste_real[indice])
                    # Demande à l'utilisateur de choisir un réalisateur
                    real=int(input("\nLes films de quel réalisateur veux-tu voir ? : "))
                    # Convertion du nombre en réalisateur
                    choix=None
                    for indice in range(len(liste_real)):
                        if real==indice+1:
                            choix=liste_real[indice]
                    # Si le réalisateur n'est pas valide, affiche un message d'erreur et recommence
                    if choix==None:
                        print("Le choix doit être compris entre 1 et", len(liste_real), "réessayer")
                    else:
                        # Affiche la liste des films du réalisateur choisi
                        print('\n---Liste des films du réalisateur :', choix+'---\n')
                        for indice in range(len(tab)):
                            if tab[indice]["realisateur"]==choix:
                                print(indice+1, ":", tab[indice]["nom"])
                # Si la saisie de l'utilisateur n'est pas un nombre entier, affiche un message d'erreur et recommence
                except ValueError:
                    print("\nLe choix doit être compris entre 1 et", len(liste_real), "réessayer")
        elif tri==4:
            tab_copie=tab
            # Trie le tableau selon la durée
            fonctions.tri_dictionnaire_croissant(tab_copie, "duree")
            # Affiche la liste des films triés selon la durée
            print("\n---Liste des films---\n")
            print("Voici la liste des films triés du plus court au plus long\n")
            for indice in range(len(tab_copie)):
                print(indice+1, ":", tab_copie[indice]["nom"], "("+str(int(tab_copie[indice]["duree"])//60),"h",str(int(tab_copie[indice]["duree"])-(int(tab_copie[indice]["duree"])//60)*60)+")")
        elif tri==5:
            tab_copie=tab
            # Trie le tableau selon l'année de sortie
            fonctions.tri_dictionnaire_decroissant(tab_copie, "annee de sortie")
            # Affiche la liste des films triés selon l'année de sortie
            print("\n---Liste des films---\n")
            print("Voici la liste des films trié du plus récent au plus vieux\n")
            for indice in range(len(tab_copie)):
                print(indice+1, ":", tab_copie[indice]["nom"], "("+str(tab_copie[indice]["annee de sortie"])+")")
        elif tri==6:
            tab_copie=tab
            # Trie le tableau selon la note
            fonctions.tri_dictionnaire_decroissant(tab_copie, "note")
            # Affiche la liste des films triés selon la note
            print("\n---Liste des films---\n")
            print("Voici la liste des films trié du mieux noté au moins bien noté selon AlloCiné\n")
            for indice in range(len(tab_copie)):
                print(indice+1, ":", tab_copie[indice]["nom"])
        elif tri==7:
            tab_copie=tab
            vu=0
            while not 1<=vu<=2:
                try:
                    # Demande à l'utilisateur de choisir si il veut voir les films que il a déjà vu ou non
                    vu=int(input("\nVeux-tu que je liste les films que tu as déjà vu (1) ou ceux que tu n'as pas encore vu (2) ? : "))
                    # Affiche la liste des films selon le choix de l'utilisateur
                    if vu==1:
                        print("\n---Liste des films---\n")
                        print("Voici la liste des films que tu as vu : \n")
                        for indice in range(len(tab)):
                            if tab[indice]["vu"]=="Oui":
                                print(indice+1, ":", tab[indice]["nom"])
                    elif vu==2:
                        print("\n---Liste des films---\n")
                        print("Voici la liste des films que tu n'as pas vu : \n")
                        for indice in range(len(tab)):
                            if tab[indice]["vu"]=="Non":
                                print(indice+1, ":", tab[indice]["nom"])
                    # Si le choix de l'utilisateur n'est pas valide, affiche un message d'erreur et recommence
                    else:
                        print("\nLe choix doit être compris entre 1 et 2, réessayer")
                # Si la saisie de l'utilisateur n'est pas un nombre entier, affiche un message d'erreur et recommence
                except ValueError:
                    print("\nLe choix doit être compris entre 1 et 2, réessayer")
        # Si le critère de tri n'est pas valide, affiche un message d'erreur et recommence
        else:
            print('\nLe choix doit être compris entre 1 et 6, réessayer')
            
def infos(tab):
    '''
    Affiche les infos d'un film

    tab -- tableau de dictionnaires contenant les films sur lequel on veut lister
    '''
    # Si le tableau est vide
    if len(tab)==0:
        print("\nVous n'avez aucunes données pour le moment, ajouter en pour pouvoir faire des traitements")
    # Si le tableau n'est pas vide
    else:
        # Choix du traitement
        traitement=0
        while not 1<=traitement<=2:
            try:
                traitement=int(input('\n---Choix du traitement---\n\n 1 : Lister les films\n 2 : Rechercher avec un mot clé\n\nQue veux-tu faire ? : '))
                if traitement==1:
                    reponse=0
                    while not 1<=reponse<=len(tab):
                        try:
                            # Affiche la liste des films
                            lister(tab, tri=1)
                            # Demande à l'utilisateur de choisir un film
                            reponse = int(input("\nSur quelle film voulez vous en savoir plus ? : "))
                            # Si le choix est valide
                            if 1<=reponse<=len(tab):
                                film = tab[reponse - 1]
                                # Affichage des infos du film
                                print("\n---"+film["nom"]+"---\n")
                                for cle, valeur in film.items():
                                    if  cle == 'duree':
                                        print(cle, ":", int(valeur)//60,"h",int(valeur)-(int(valeur)//60)*60)
                                    elif cle == 'note':
                                        print(cle, ':', str(valeur)+'/5')
                                    else:
                                        print(cle, ":", valeur)
                            # Si le choix n'est pas valide
                            else:
                                print("\nle choix doit être compris entre 1 et", len(tab), "réessayer")
                        except ValueError:
                            print("\nle choix doit être compris entre 1 et", len(tab), "réessayer")
                elif traitement==2:
                    # Demande à l'utilisateur de choisir un mot clé
                    recherche = str(input("\n---Recherche---\n\nQuel film veux-tu rechercher ? : "))
                    # Parcourt le tableau pour trouver les films qui contiennent le mot clé
                    liste_recherche=[]
                    for valeur in tab:
                        if recherche in valeur["nom"]:
                            liste_recherche.append(valeur)
                    if len(liste_recherche)==0:
                        print("\nAucun film ne correspond à votre recherche")
                    else:
                        # Affiche la liste des films qui contiennent le mot clé
                        print("\n---Résultat de la recherche---\n")
                        for indice in range(len(liste_recherche)):
                            print(indice+1, ":", liste_recherche[indice]["nom"])
                        reponse=0
                        while not 1<=reponse<=len(liste_recherche):
                            try:
                                # Demande à l'utilisateur de choisir un film parmis ceux qui ont le mot clé
                                reponse = int(input("\nSur quelle film voulez vous en savoir plus ? : "))
                                # Si le choix est valide
                                if 1<=reponse<=len(liste_recherche):
                                    film = liste_recherche[reponse - 1]
                                    # Affichage des infos du film
                                    print("\n---"+film["nom"]+"---\n")
                                    for cle, valeur in film.items():
                                        if  cle == 'duree':
                                            print(cle, ":", int(valeur)//60,"h",int(valeur)-(int(valeur)//60)*60)
                                        elif cle == 'note':
                                            print(cle, ':', str(valeur)+'/5')
                                        else:
                                            print(cle, ":", valeur)
                                # Si le choix n'est pas valide
                                else:
                                    print("\nle choix doit être compris entre 1 et", len(tab), "réessayer")
                            except ValueError:
                                print("\nle choix doit être compris entre 1 et", len(tab), "réessayer")
                else:
                    print("\nLe choix doit être compris entre 1 et 2, réessayer")
            except ValueError:
                print("\nLe choix doit être compris entre 1 et 2, réessayer")
    
def ajouter(tab):
    '''
    Ajoute un film au tableau

    tab -- tableau de dictionnaires contenant les films sur lequel on veut ajouter
    '''
    # Création d'un nouveau film
    tab.append({})
    # Demande à l'utilisateur le nom du film
    tab[len(tab)-1]['nom']=str(input('\n---Nom du film---\n\nQuelle est le nom du film que tu veux ajouter ? : ')).capitalize()
    # Demande à l'utilisateur le genre du film
    tab[len(tab)-1]['genre']=str(input('\n---Genre du film---\n\nQuelle est le genre du film que tu veux ajouter ? : '))#Faire quelque chose pour que ca propose les genre déja existant et en utiliser une xistant si tu veux ouen créer un
    # Demande à l'utilisateur le réalisateur du film
    tab[len(tab)-1]['realisateur']=str(input('\n---Réalisateur du film---\n\nQuelle est le réalisateur du film que tu veux ajouter ? : '))#pareil
    # Demande à l'utilisateur la durée du film
    duree=0
    while duree==0:
        try:
            duree=int(input('\n---Durée du film---\n\nQuelle est la durée du film que tu veux ajouter en minutes ? : '))
            tab[len(tab)-1]['duree']=duree
        # Si la durée n'est pas un nombre entier
        except ValueError:
            print('\nLa durée doit être un nombre entier, réessayer')
    # Demande à l'utilisateur l'année de sortie du film
    annee=0
    while annee==0:
        try:
            annee=int(input('\n---Année de sortie du film---\n\nQuelle est l\'année de sortie du film que tu veux ajouter ? : '))
            tab[len(tab)-1]['annee de sortie']=annee
        # Si l'année de sortie n'est pas un nombre entier
        except ValueError:
            print('\nL\'année de sortie doit être un nombre entier, réessayer')
    # Vérifie que la note est comprise entre 0.0 et 5.0
    note=10
    while not 0.0<=note<=5.0:
        try:
            # Demande à l'utilisateur la note du film
            note=float(input('\n---Note du film---\n\nQuelle est la note sur 5 sur AlloCiné du film que tu veux ajouter ? (Il faut mettre un point pour faire une virgule): '))
            # Si la note est valide
            if 0.0<=note<=5.0:
                tab[len(tab)-1]['note']=note
            # Si la note n'est pas valide
            else:
                print('\nLa note doit être comprise entre 0 et 5, réessayer')
        except ValueError:
            print('\nLa note doit être comprise entre 0 et 5, réessayer')
    # Est ce que le film a été vu ?
    vu=None
    while vu!="Oui" and vu!="Non":
        # Demande à l'utilisateur si le film a été vu
        vu=str(input('\n---Vu ?---\n\nAs-tu vu le film que tu veux ajouter ? (Oui/Non) : '))
        # Si la réponse n'est pas valide
        if vu!="Oui" and vu!="Non":
            print('\nLa réponse doit être Oui ou Non, réessayer')
    # Ajoute la réponse dans le tableau
    tab[len(tab)-1]['vu']=vu
    fonctions.tri_dictionnaire_croissant(tab, "nom")

def modifier(tab):
    '''
    Modifie une donnée d'un film

    tab -- tableau de dictionnaires contenant les films sur lequel on veut modifier
    '''
    # Si le tableau est vide
    if len(tab)==0:
        print("\nVous n'avez aucunes données pour le moment, ajouter en pour pouvoir faire des traitements")
    # Si le tableau n'est pas vide
    else:
        reponse=0
        while not 1<=reponse<=len(tab):
            try:
                lister(tab, tri=1)
                # Demande à l'utilisateur de choisir un film
                reponse = int(input("\nQuelle film voulez vous modifier ? : "))
                # Si le choix est valide
                if 1<=reponse<=len(tab):
                    # Choix de l'information à modifier
                    info=0
                    while not 1<=info<=7:
                        try:
                            # Affichage des informations
                            cle=list(tab[0].keys())
                            print("\n---Liste des descripteurs---\n")
                            for indice in range(len(cle)):
                                print(indice+1, ":", cle[indice].capitalize())
                            # Demande à l'utilisateur de choisir une information
                            info=int(input("\nQuelle information voulez vous modifier sur le film ? : "))
                            # Si l'utilisateur veut modifier le nom
                            if info == 1:
                                # Demande à l'utilisateur le nouveau nom
                                tab[reponse-1]['nom'] = str(input("\nQuel est le nouveau nom du film ? : ")).capitalize()  
                                fonctions.tri_dictionnaire_croissant(tab, "nom")
                            # Si l'utilisateur veut modifier le genre
                            elif info == 2:
                                # Demande à l'utilisateur le nouveau genre
                                tab[reponse-1]['genre'] = str(input("\nQuel est le nouveau genre du film ? : "))
                            # Si l'utilisateur veut modifier le réalisateur
                            elif info == 3:
                                # Demande à l'utilisateur le nouveau réalisateur
                                tab[reponse-1]['realisateur'] = str(input("\nQuel est le nouveau réalisateur du film ? : "))
                            # Si l'utilisateur veut modifier la durée
                            elif info == 4:
                                duree=0
                                while duree==0:
                                    try:
                                        # Demande à l'utilisateur la nouvelle durée
                                        duree=int(input("\nQuelle est la nouvelle durée du film ? (en minutes) : "))  
                                        tab[reponse-1]['duree']=duree
                                    # Si la durée n'est pas un nombre entier
                                    except ValueError:
                                        print('\nLa durée doit être un nombre entier, réessayer')
                            # Si l'utilisateur veut modifier l'année de sortie
                            elif info == 5:
                                annee=0
                                while annee==0:
                                    try:
                                        # Demande à l'utilisateur l'année de sortie
                                        annee=int(input("\nQuelle est la nouvelle année de sortie du film ? : "))
                                        tab[reponse-1]['annee de sortie']=annee
                                    # Si l'année de sortie n'est pas un nombre entier
                                    except ValueError:
                                        print('\nL\'année de sortie doit être un nombre entier, réessayer')
                            # Si l'utilisateur veut modifier la note
                            elif info == 6:
                                note=10
                                # Vérifie que la note est comprise entre 0.0 et 5.0
                                while not 0.0<=note<=5.0:
                                    try:
                                        # Demande à l'utilisateur la nouvelle note
                                        note=float(input("\nQuelle est la nouvelle note du film ? (entre 0 et 5) : "))
                                        if 0.0<=note<=5.0:
                                            tab[reponse-1]['note']=note
                                        # Si la note n'est pas valide
                                        else:
                                            print('\nLa note doit être comprise entre 0 et 5, réessayer')
                                    except ValueError:
                                        print('\nLa note doit être comprise entre 0 et 5, réessayer')
                            # Si l'utilisateur veut modifier si le film a été vu
                            elif info == 7:
                                vu=None
                                while vu!="Oui" and vu!="Non":
                                    # Demande à l'utilisateur si le film a été vu
                                    vu=str(input("\nAs-tu vu le film ? (Oui/Non) : "))
                                    # Si la réponse est valide
                                    if vu=="Oui" or vu=="Non":
                                        tab[reponse-1]['vu']=vu
                                    # Si la réponse n'est pas valide
                                    else:
                                        print('\nLa réponse doit être Oui ou Non, réessayer')
                            else:    
                                print('\nLe choix doit être compris entre 1 et 7, réessayer')
                        except ValueError:
                            print('\nLe choix doit être compris entre 1 et 7, réessayer')
                else:
                    print("\nle choix doit être compris entre 1 et", len(tab), "réessayer")
            except ValueError:
                print("\nle choix doit être compris entre 1 et", len(tab), "réessayer")

def supprimer(tab):
    """
    Supprime un film du tableau

    tab -- tableau de dictionnaires contenant les films sur lequel on veut supprimer
    """
    # Vérifie si le tableau est vide
    if len(tab)==0:
        print("\nVous n'avez aucunes données pour le moment, ajouter en pour pouvoir faire des traitements")
    else:
        reponse=0
        while not 1<=reponse<=len(tab):
            try:
                # Demande à l'utilisateur de choisir un film
                lister(tab, tri=1)
                reponse = int(input("\nQuelle film voulez vous supprimer ? : "))
                if 1<=reponse<=len(tab):
                    # Supprime le film
                    print("\nLe film", tab[reponse-1]["nom"], "a bien été supprimé")
                    del tab[reponse-1]
                # Si le choix n'est pas valide 
                else:
                    print("\nle choix doit être compris entre 1 et", len(tab), "réessayer")
            except ValueError:
                print("\nle choix doit être compris entre 1 et", len(tab), "réessayer")

def sauvegarder(tab):
    """
    Sauvegarde le tableau dans un fichier

    tab -- tableau de dictionnaires contenant les films sur lequel on veut sauvegarder
    """
    nom=""
    # Vérifie si le nom du fichier est valide
    while nom.endswith(".csv")==False:
        # Demande le nom du fichier à l'utilisateur
        print("\n---Sauvegarde---\n")
        nom = str(input("Donne moi le nom que tu veux donner au fichier .csv (sans oublier l'extension .csv à la fin !!!) : "))
        if nom.endswith('.csv')==False:
            print("\nLe fichier doit être un fichier .csv, réessayer")
        else:
            # Enregistre le tableau dans le fichier
            fichier = open(nom, "w")
            w = csv.DictWriter(fichier, fieldnames=['nom','genre','realisateur','duree','annee de sortie','note','vu'])
            w.writeheader()
            w.writerows(tab)
            fichier.close()
    # Remerciements
    print("\nMerci d'avoir utilisé notre gestionnaire de film ! En espérant que cela vous a plu")