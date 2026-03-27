# Auteur : Alexandre MAI--EMERY

import matplotlib.pyplot as plot
import math

def nb_suiv(s):
    '''
    Renvoie le nombre suivant de celui representé par s en appliquant le procédé de lecture.
    
    s: Chaine de caractères représentant le nombre actuel
    return: Chaine de caractères représentant le nombre suivant'''
    nouveau="" # Initialisation de la nouvelle chaîne qui contiendra le terme suivant
    i=0 # Initialisation de l'index pour parcourir la chaîne s
    while i<len(s): # Boucle pour parcourir toute la chaîne s
        occurence = 1 # Initialisation du compteur d'occurrences pour le caractère actuel
        while i < len(s) - 1 and s[i] == s[i + 1]: # Boucle pour compter les occurrences consécutives du même caractère
            i += 1 # On avance l'index pour continuer à compter
            occurence += 1 # On incrémente le compteur d'occurrences
        nouveau += str(occurence) + s[i] # On ajoute le nombre d'occurrences et le caractère à la nouvelle chaîne
        i += 1 # On avance l'index pour passer au caractère suivant
    return nouveau # On renvoie la nouvelle chaîne représentant le terme suivant

def nb_suiv_N(s, N):
    '''
    Renvoie le terme obtenu après N applications de la suite de Conway
    
    s: Chaine de caractères représentant le terme initial
    N: Nombre d'applications de la fonction nb_suiv
    return: Chaine de caractères représentant le terme après N applications
    '''
    if N == 0: # Condition de fin de récursivité
        return s # On renvoie le terme initial
    return nb_suiv_N(nb_suiv(s), N - 1) # Appel récursif en appliquant la fonction nb_suiv et en diminuant N de 1

def anagramme(mot):
    '''
    Renvoie la liste de tous les anagrammes du mot donné en argument.
    
    mot: Chaine de caractères représentant le mot dont on veut les anagrammes
    return: Liste de chaînes de caractères représentant les anagrammes du mot
    '''
    if len(mot) == 0: # Condition de fin de récursivité
        return [""] # On renvoie une liste contenant la chaîne vide pour que la concaténation fonctionne
    anagrammes = [] # Liste pour stocker les anagrammes qui seront générés et renvoyés
    for i in range(len(mot)): # Boucle pour chaque parcourir chaque lettre du mot
        lettre = mot[i] # On sélectionne la lettre à la position i de la chaîne
        reste = mot[:i] + mot[i+1:] # On crée une nouvelle chaîne sans la lettre sélectionnée
        for anagramme_reste in anagramme(reste): # Appel récursif pour obtenir les anagrammes du reste du mot
            anagrammes.append(lettre + anagramme_reste) # On concatène la lettre sélectionnée avec chaque anagramme du reste et on l'ajoute à la liste
    return anagrammes # On renvoie la liste complète des anagrammes générés

def binaire(n):
    '''
    Donne la représentation binaire de l'entier n sous forme de liste de bits.

    n: Entier dont on veut la représentation binaire
    return: Liste de bits représentant n en binaire
    '''
    if n==0: # Condition de fin de récursivité
        return [] # On renvoie une liste vide pour indiquer la fin de la conversion
    else: 
        return binaire(n//2)+[n%2] # Appel récursif en divisant n par 2 et en ajoutant le bit de poids faible (n%2) à la fin de la liste

def carreDroit(n):
    '''
    Trace un carré droit de et appelle la fonction carrePenche pour tracer le carré penché à l'intérieur.

    n: Longueur du côté du carré
    return: None (fonction de tracé)
    '''
    if n < 1: # Condition de fin de récursivité (qyuand n est trop petit, donc que le carré ne peut plus être tracé)
        return
    plot.plot([-n, n, n, -n, -n], [-n, -n, n, n, -n]) # Tracé du carré droit (coordonnées des sommets)
    carrePenche(n) # Appel de la fonction pour tracer le carré penché à l'intérieur


def carrePenche(n):
    '''
    Trace un carré penché à l'intérieur du carré droit et appelle la fonction carreDroit pour tracer le carré droit à l'intérieur.

    n: Longueur du côté du carré
    return: None (fonction de tracé)
    '''
    if n < 1: # Condition de fin de récursivité (quand n est trop petit, donc que le carré ne peut plus être tracé)
        return
    plot.plot([0, n, 0, -n, 0], [-n, 0, n, 0, -n]) # Tracé du carré penché (coordonnées des sommets)
    carreDroit(n / 2) # Appel de la fonction pour tracer le carré droit à l'intérieur avec une taille réduite

def flocon(x, y, angle, longueur, n):
    '''
    Trace un segment du flocon de Koch récursivement et calcule la longueur totale et l'aire ajoutée.

    x, y: Coordonnées du point de départ du segment
    angle: Angle d'orientation du segment en radians
    longueur: Longueur du segment à tracer
    n: Niveau de récursivité (profondeur)
    return: Tuple (x_final, y_final, longueur_totale, aire_totale)
    '''
    if n == 0: # Condition de fin de récursivité
        x2 = x + longueur * math.cos(angle) # Calcul des coordonnées (abscisse) du point final du segment
        y2 = y + longueur * math.sin(angle) # Calcul des coordonnées (ordonnée) du point final du segment
        plot.plot([x, x2], [y, y2], 'k') # Tracé du segment entre le point de départ et le point final
        return x2, y2, longueur, 0 # Renvoie les coordonnées finales, la longueur du segment et une aire de 0
    longueur /= 3 # Division de la longueur par 3 pour les segments du flocon de Koch
    x, y, L1, A1 = flocon(x, y, angle, longueur, n - 1) # Appel récursif pour le premier segment
    x, y, L2, A2 = flocon(x, y, angle + math.pi / 3, longueur, n - 1) # Appel récursif pour le deuxième segment (incliné)
    x, y, L3, A3 = flocon(x, y, angle - math.pi / 3, longueur, n - 1) # Appel récursif pour le troisième segment (incliné dans l'autre sens)
    x, y, L4, A4 = flocon(x, y, angle, longueur, n - 1) # Appel récursif pour le quatrième segment (final)
    aire = (math.sqrt(3) / 4) * longueur ** 2 # Calcul de l'aire ajoutée par le triangle équilatéral formé
    longueur_totale = L1 + L2 + L3 + L4 # Calcul de la longueur totale des segments tracés
    aire_totale = A1 + A2 + A3 + A4 + aire # Calcul de l'aire totale ajoutée
    return x, y, longueur_totale, aire_totale # Renvoie les coordonnées finales, la longueur totale et l'aire totale


if __name__ == "__main__":
    # Tests des fonctions

    # Test de nb_suiv
    print(nb_suiv("1211"))

    # Test de nb_suiv_N
    print(nb_suiv_N("1", 3))

    # Test d'anagramme
    print(anagramme("abc"))

    # Test de binaire
    print(binaire(13))

    # Test de carreDroit et carrePenche
    plot.figure(figsize=(6,6))
    carreDroit(8)
    plot.title("Carrés récursifs croisés")
    plot.axis('equal')
    plot.show()

    # Test de flocon de Koch

    # Tracé du flocon de Koch
    plot.figure(figsize=(8,8))
    plot.title("Flocon de Koch")
    x, y = 0, 0       
    L = 1
    N = 5
    x, y, L1, A1 = flocon(x, y, 0, L, N)
    x, y, L2, A2 = flocon(x, y, -2 * math.pi / 3, L, N)
    x, y, L3, A3 = flocon(x, y, 2 * math.pi / 3, L, N)
    plot.axis('equal')
    plot.show()

    # Calcul de la longueur totale et de la surface du flocon
    longueur = L1 + L2 + L3
    surface = (math.sqrt(3) / 4) * L ** 2 + A1 + A2 + A3
    print("Longueur :", longueur)
    print("Surface :", surface)
