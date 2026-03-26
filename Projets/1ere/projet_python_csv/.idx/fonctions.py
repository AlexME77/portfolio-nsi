def tri_dictionnaire_croissant(tab, descripteur):
    """
    Tri un tableau de dictionnaire dans l'ordre croissant (tri sélection).

    tab         -- tableau de dictionnaires à trier
    descripteur -- descripteur du dictionnaire sur lequel on veut trier
    """
    n = len(tab)
    for i in range(n-1):
        indice_min=i
        for j in range(i+1, n):
                if tab[j][descripteur]<tab[indice_min][descripteur]:
                    indice_min=j
        temp=tab[i]
        tab[i]=tab[indice_min]
        tab[indice_min]=temp

def tri_dictionnaire_decroissant(tab, descripteur):
    """
    Tri un tableau de dictionnaire dans l'ordre décroissant (tri sélection).

    tab         -- tableau de dictionnaires à trier
    descripteur -- descripteur du dictionnaire sur lequel on veut trier
    """
    n = len(tab)
    for i in range(n-1):
        indice_max=i
        for j in range(i+1, n):
            if tab[j][descripteur]>tab[indice_max][descripteur]:
                indice_max = j
        temp=tab[i]
        tab[i]=tab[indice_max]
        tab[indice_max]=temp

