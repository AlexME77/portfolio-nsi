def salutation(langue):
    """
    Renvoie le formule de salutation propre une langue donnée.

    langue -- Chaîne au format ISO 639-1
    
    >>> salutation('fr')
    'Salut'
    >>> salutation('es')
    'Hola'
    >>> salutation('en')
    'Hello'
    >>> salutation('??')
    'Hello'
    """
    
    if langue == 'fr':
        return 'Salut'
    elif langue == 'es':
        return 'Hola'
    else:
         return 'Hello'
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()