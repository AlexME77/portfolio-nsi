def rendu(montant):
    """
    Calcule le rendu de monnaie pour un montant donné en euros.
    Utilise les billets et pièces courants en euros.
    """
    billets_pieces = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    rendu_monnaie = {}
    for valeur in billets_pieces:
        if montant > 0:
            if montant >= valeur:
                quantite = int(montant // valeur)
                rendu_monnaie[valeur] = quantite
                montant -= quantite * valeur   
    return rendu_monnaie

print(rendu(786))