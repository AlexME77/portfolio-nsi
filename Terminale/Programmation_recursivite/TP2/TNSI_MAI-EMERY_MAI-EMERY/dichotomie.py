def dichotomie(L, x):
    n = len(L)-1
    debut = 0
    milieu = n//2
    fin = n
    nb_etapes=0
    
    while debut<=fin:
        milieu=(debut+fin)//2
        nb_etapes+=1
        if L[milieu]==x:
            return True, nb_etapes
        elif L[milieu]>x:
            fin = milieu-1
        else:
            debut = milieu + 1
    return False, nb_etapes

def dichotomie_recursif(L, x, g=0, d=-1, nb_etapes=0):
    if d==-1:
        d=len(L)-1
    if g > d:
        return False,nb_etapes+1 
    milieu = (g+d)//2
    nb_etapes+=1
    if L[milieu] == x :
        return True, nb_etapes
    elif L[milieu] > x :
        return dichotomie_recursif(L, x, g, milieu-1, nb_etapes)
    else :
        return dichotomie_recursif(L, x, milieu+1, d, nb_etapes)
    


if __name__ == "__main__":
    print(str(dichotomie([1,2,3,4,5,6,7,8,9,10], 7)))
    print(str(dichotomie_recursif([1,2,3,4,5,6,7,8,9,10], 7)))