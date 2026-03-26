def generer_plateau():
    """
    Génère un plateau de jeu vide.
    Renvoie un tableau doublement indexé de taille 3x3 ne contenant que des zéros.
    """
    return [[0]*3 for _ in range(3)]

def case_plateau(valeur):
    """
    Convertit la valeur entière d'une case en son symbole d'affichage.

    Paramètre :
        valeur - La valeur de la case (0 pour vide, 1 pour X, 2 pour O)
    """
    if valeur == 0:
        valeur = " "
    elif valeur == 1:
        valeur = "X"
    elif valeur == 2:
        valeur = "O"
    return valeur


def afficher_plateau(plateau):
    """
    Affiche le plateau de jeu dans la console.

    Paramètre :
        plateau - Le plateau de jeu sous forme d'un tableau doublement indexé.
    """
    affichage = ""
    for i_ligne in range(len(plateau)):
        # Construit la chaine d'affichage des pions d'une ligne du plateau.
        affichage += ' ' + '|'.join([case_plateau(case) for case in plateau[i_ligne]]) + '\n'

        # Construit la ligne horizontale de séparation.
        if i_ligne < 2:
            affichage += ('—' * 7) + '\n'

    print(affichage)


def demander_coup_joueur(joueur):
    """
    Demande au joueur de saisir son coup sous la forme '{ligne}{colonne}'.
    La saisie "11" signifie que le joueur joue dans la première case en haut à gauche du plateau de jeu (plateau[0][0]).

    La fonction renvoie un tuple des coordonnées (ligne, colonne) du coup choisi.
    La saisie "32" (ligne 3, colonne 2) entraine le renvoi du tuple (2, 1).

    Paramètre :
        joueur - Numéro du joueur (1 ou 2)
    """
    saisie = input("Joueur " + case_plateau(joueur) + " : ")
    return traiter_saisie_joueur(saisie)


def traiter_saisie_joueur(saisie):
    """
    Renvoie la convertion de la saisie du joueur un tuple des coordonnées (ligne, colonne).

    Paramètre :
        saisie - La chaîne saisie par le joueur (format : '{ligne}{colonne}')
    """
    convertion = int(saisie[0])-1, int(saisie[1])-1
    return convertion


def jouer_coup_joueur(plateau, joueur, coup):
    """
    Place le symbole du joueur sur le plateau aux coordonnées spécifiées.

    Paramètres :
        plateau - Plateau de jeu sous forme d'un tableau doublement indexé
        joueur - Numéro du joueur
        coup - Tuple des coordonnées (ligne, colonne) où placer le symbole
    """
    while (0<=coup[0]<=2 and 0<=coup[1]<=2 and plateau[coup[0]][coup[1]] == 0) == False:
        coup = demander_coup_joueur(joueur)
    plateau[coup[0]][coup[1]] = joueur
     
def tester_victoire(plateau, joueur):
    """
    Vérifie si le joueur spécifié a gagné la partie.
    Renvoie True si joueur a gagné, False sinon.

    Paramètres :
        plateau - Le plateau de jeu sous forme d'un tableau doublement indexé
        joueur - Le numéro du joueur à tester (1 ou 2)
    """
    for i in range(3):
        if plateau[i][0]==plateau[i][1]==plateau[i][2]==joueur:
            return True
        elif plateau[0][i]==plateau[1][i]==plateau[2][i]==joueur:
            return True
        elif plateau[0][0] == plateau[1][1] == plateau[2][2]==joueur:
            return True
        elif plateau[2][0]==plateau[1][1]==plateau[0][2]==joueur:
            return True
    return False


def tester_match_nul(plateau):
    """
    Vérifie si la partie est un match nul.
    Renvoie True si le match est nul, False sinon.

    Paramètre :
        plateau - Le plateau de jeu sous forme d'un tableau doublement indexé
    """
    for i in range(3):
        if 0 in plateau[i]:
            return False
    return True

def afficher_victoire(joueur):
    """
    Affiche le message de victoire pour le joueur spécifié.

    Paramètre :
        joueur - Numéro du joueur gagnant (1 ou 2)
    """
    print("Le joueur " + case_plateau(joueur) + " a gagné !")


def afficher_nul():
    """ Affiche le message de match nul. """
    print("Match nul !")


def lancer_jeu():
    """ Lance une partie de morpion. """
    plateau = generer_plateau()
    joueur = 1
    victoire = False
    match_nul = False
    
    while victoire == False and match_nul == False:
        afficher_plateau(plateau)
        coup = demander_coup_joueur(joueur)
        jouer_coup_joueur(plateau, joueur, coup)
        
        if tester_victoire(plateau, joueur) == True:
            victoire = True
        elif tester_match_nul(plateau) == True:
            match_nul = True
        else:
            if joueur == 1:
                joueur = 2
            elif joueur == 2:
                joueur = 1
    afficher_plateau(plateau)
    
    if victoire == True:
        afficher_victoire(joueur)
    else:
        afficher_nul()

def rejouer():
    """
    Demande au joueur de saisir un "Oui" ou un "Non" si il veut rejouer une partie ou non.
    """
    saisie = input("Tu veux refaire une partie ? saisir 'oui' ou 'non' : ")
    if saisie == "oui":
        lancer_jeu()
        
def afficher_score(score):
    """
    Affiche le score de chacun des joueurs de la partie.
    
    Paramètres :
        score - tableau avec le score du joueur 1 à l'indice 0 et du joueur 2 à l'indice 1.
    """
    return "Le score est : Joueur 1 (X) : " + str(score[0]) + " ; Joueur 2 (O) : " + str(score[1])
    