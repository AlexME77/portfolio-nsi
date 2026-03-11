# [NSI1RE06] TP1 - Problème météo
# Heure début : 09h25
# Heure fin   : 00h00 (le tp suivant)


def rapport(temperatures):
    mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    for i in range(len(mois)):
        print(mois[i] + ' : ' + str(temperatures[i]))
    print("Température moyenne annuelle : ", moyenne(temperatures))
    print("Température moyenne maximale : ", maximum(temperatures))
        
def moyenne(temperatures):
    total=0
    for v in temperatures:
        total+=v
    return total/len(temperatures)

def maximum(liste):
    """
    Calcule la plus grande valeur d'un tableau non vide d'entiers ou de flottants

    liste -- tableau qui va servir pour la fonction à calculer la plus grande valeur
    """
    max=0
    for v in liste:
        if v>max:
            max=v
    return max

if __name__ == '__main__':
    # Températures mensuelles moyennes de l'année 2021
    temperatures_2021 = [4.6, 6.5, 5.6, 10.0, 11.3, 14.4, 15.7, 17.6, 14.5, 10.3, 7.3, 5.2]
    # Affichage du rapport
    rapport(temperatures_2021)
    