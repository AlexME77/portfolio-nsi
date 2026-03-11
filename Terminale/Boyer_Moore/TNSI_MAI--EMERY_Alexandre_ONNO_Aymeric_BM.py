import timeit

def rechStupide(texte, motif):
    for i in range(len(texte)-len(motif)):
        isPres = True
        for j in range(len(motif)):
            if(texte[i+j] == motif[j]):
                isPres = True and isPres
            else:
                isPres = False and isPres
        if(isPres):
            return True
    return isPres
    
def calculADroite(motif):
    """
    Renvoie un dictionnaire avec pour clé la lettre et pour valeur le décalage

    Arguments : motif: str (le motif recherché)
    Returns aDroite: dict (dictionnaire des positions des lettres dans le motif)
    """
    aDroite = {} # Création du dictionnaire
    for i in range(len(motif)-1, -1, -1): # On parcourt le motif de droite à gauche (de la fin au début)
        if motif[i] not in aDroite.keys(): # Si la lettre n'est pas déjà dans le dictionnaire
            aDroite[motif[i]] = i # On ajoute la lettre avec sa position
    return aDroite # On renvoie le dictionnaire

def droite(c, aDroite):
    '''
    Renvoie la position de la lettre c dans le dictionnaire aDroite
    
    Arguments : c: str (lettre à chercher)
                aDroite: dict (dictionnaire des positions)
    Returns : position: int (position de la lettre dans le dictionnaire ou -1 si elle n'y est pas)
    '''
    if c in aDroite.keys(): # Si la lettre est dans le dictionnaire
        return aDroite[c] # On renvoie sa position
    else: # Si la lettre n'est pas dans le dictionnaire
        return -1 # On renvoie -1

def decalage(j, c, motif):
    """Calcule le décalage à effectuer en fonction de la lettre c et de sa position j dans le motif

    Arguments : j: int (position de la lettre dans le motif)
                c: str (lettre du texte qui ne correspond pas)
                motif: str (le motif recherché)
    Returns : d: int (le décalage à effectuer)
    """
    if c not in motif: # Si la lettre n'est pas dans le motif
        return j + 1 # On décale de j + 1
    else: # Si la lettre est dans le motif
        for i in range(len(motif)-1, -1, -1): # On parcourt le motif de droite à gauche
            if motif[i] == c: # Si on trouve la lettre
                d = j - i # On calcule le décalage
                if d > 0: # Si le décalage est positif
                    return d # On renvoie le décalage
                else: # Si le décalage est négatif ou nul
                    return 1 # On décale de 1

def cherche_BoyerMoore(texte, motif):
    """
    Recherche un mot dans un texte avec l'algo de boyer-moore

    Arguments : texte: str (le texte dans lequel on effectue la recherche)
                motif: str (le motif recherché)

    Returns : bool (renvoie True si le mot est trouvé, False sinon)
    """
    i = 0 # Compteur de la position dans le texte
    while i <= len(texte) - len(motif): # Tant que la position est valide et ne dépasse pas la fin du texte (on crée la boucle de recherche)
        j = len(motif) - 1 # Position dans le motif (à partir de la fin du motif)
        while j >= 0 and texte[i + j] == motif[j]: # Tant que les lettres correspondent et que j est valide (on crée la boucle de comparaison)
            j -= 1 # On recule dans le motif (on compare la lettre précédente car la lettre actuelle correspond)
        if j < 0: # Si on a trouvé le mot (entièrement comparé et donc que j est négatif)
            return True # On renvoie True car le mot a été trouvé
        else: # Si on n'a pas trouvé le mot
            d = decalage(j, texte[i + j], motif) # Calcul du décalage à effectuer pour la prochaine comparaison
            i += d # On décale la position dans le texte pour la prochaine comparaison
    return False # On renvoie False si le mot n'a pas été trouvé à la fin de la recherche

def cherche_BoyerMoore_verb(texte, motif):
    """
    Recherche un mot dans un texte avec l'algo de boyer-moore et compte le nombre de comparaisons effectuées

    Arguments : texte: str (le texte dans lequel on effectue la recherche)
                motif: str (le motif recherché)
    Returns : tuple (position du mot dans le texte ou False, nombre de comparaisons effectuées)
    """
    i = 0 # Compteur de la position dans le texte
    compteur = 0 # Compteur du nombre du nombre de comparaison
    while i <= len(texte) - len(motif): # Tant que la position est valide et ne dépasse pas la fin du texte (on crée la boucle de recherche)
        compteur+=1 # On incrémente le compteur de comparaison
        j = len(motif) - 1 # Position dans le motif (à partir de la fin du motif)
        while j >= 0 and texte[i + j] == motif[j]: # Tant que les lettres correspondent et que j est valide (on crée la boucle de comparaison)
            j -= 1 # On recule dans le motif (on compare la lettre précédente car la lettre actuelle correspond)
        if j < 0: # Si on a trouvé le mot (entièrement comparé et donc que j est négatif)
            return i, compteur # On renvoie True car le mot a été trouvé
        else: # Si on n'a pas trouvé le mot
            d = decalage(j, texte[i + j], motif) # Calcul du décalage à effectuer pour la prochaine comparaison
            i += d # On décale la position dans le texte pour la prochaine comparaison
    return False # On renvoie False si le mot n'a pas été trouvé à la fin de la recherche

if __name__ == "__main__":
    texte = "Lorem ipsum ljdqnf msdnfm  jqfnmqj mjdlfn KQFNMLNC  lmksvdn mlkv psum ljdqnf msdnfm  jqfnmqj mjdlfn KQFNMLNC ùmkn:lkjn kln "
    motif = "ùmkn:lkjn kln"

    print(calculADroite(motif))
    print(droite("k", calculADroite(motif)))
    print(cherche_BoyerMoore_verb(texte, motif))

    tic = timeit.default_timer()
    print(rechStupide(texte,motif))
    print(timeit.default_timer()-tic)

    tic = timeit.default_timer()
    print(cherche_BoyerMoore(texte, motif))
    print(timeit.default_timer()-tic)