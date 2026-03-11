# [NSI1RE06] TP1 - Exercice 2.2 - Écriture de la fonction somme
# Heure début : 09h17
# Heure fin   : 09h25

def somme(tableau):
    """
    Renvoie la somme de toutes les valeurs du tableau
    
    tableau -- tableau dont la somme va être calculé
    
    >>> somme([1, 2, 3, 4])
    10
    """
    
    total=0
    for v in tableau:
        total+=v
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()