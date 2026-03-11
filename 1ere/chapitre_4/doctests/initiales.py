def initiales(prenom, nom):
    """
    Renvoie les initiales du prénom et du nom donnés.
    
    prenom -- prénom de la personne donné
    nom    -- nom de la personne donnné
    
    >>> initiales('Bernard', 'Dupont')
    'BD'
    """
    lettre = prenom[0] + nom[0]
    return lettre.upper()

if __name__ == "__main__":
    import doctest
    doctest.testmod()