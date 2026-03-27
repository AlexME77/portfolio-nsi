from arbre_eleve import arbre

if __name__ == "__main__":
    a = [5,[3,[4,[2,[],[]],[1,[],[]]],[6,[7,[10,[],[]],[11,[],[]]],[8,[],[]]]],[2,[],[]]]
    b = [1,[2,[4,[8,[],[]],[9,[],[]]],[5,[10,[],[]],[]]],[3,[6,[],[]],[7,[],[]]]]
    c = [2, [1, [0, [], []], []], [5, [4, [3, [], []], []], [12,[9, [8, [6, [], [7, [], []]], []], [10, [], [11, [], []]]], [13, [], [14, [], [18, [17, [15, [], [16, [], []]],[]], [19, [], []]]]]]]]
    d = [20,[5,[3,[],[]],[12,[8, [6, [],[]],[]],[13,[],[]]]],[25, [21, [],[]],[28,[],[]]]]
    e = ['moi', ['maman', ['papy',[], []], ['mamie', [], []]], ['papa', ['papy',[], []], ['mamie', [], []]]]

liste_arbre = [a, b, c, d, e]
nom_arbre = ["a", "b", "c", "d", "e"]
arbre1 = arbre()

for i in range(len(nom_arbre)):
    print('Arbre ' + nom_arbre[i] + ' :')
    print('Taille : ' + str(arbre1.taille(liste_arbre[i])))
    print('Hauteur : ' + str(arbre1.hauteur(liste_arbre[i])))
    print('estVide : ' + str(arbre1.estVide(liste_arbre[i])))
    print()
    print('Arbre ' + nom_arbre[i] + ' :')
    print('Parcours par largeur :' + str(arbre1.parcours_largeur(liste_arbre[i])))
    print('Parcours par profondeur :' + str(arbre1.parcours_profondeur(liste_arbre[i])))
    print('Parcours par profondeur récursif prefix :' + str(arbre1.parcours_profondeur_recursif_prefix(liste_arbre[i])))
    print('Parcours par profondeur récursif infixe :' + str(arbre1.parcours_profondeur_recursif_infixe(liste_arbre[i])))
    print('Parcours par profondeur récursif postfixe :' + str(arbre1.parcours_profondeur_recursif_postfixe(liste_arbre[i])))
    print()