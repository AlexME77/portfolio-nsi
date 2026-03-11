# [NSI1RE06] TP1 - Exercice 2.1 - Parcours simples
# Heure début : 09h10
# Heure fin   : 09h16

t1 = ['(\\(\\','(-.-)','c(")(")']
t2 = ["'___'","(0,0)","/)_)",' ""']
t3 = ["  __", "<(o )___", " ( ._> /", "  `---'"]

# Tableau t1 : Afficher chaque valeur en utilisant un parcours par valeur.
print("Tableau T1")
for v in t1:
    print(v)


# Tableau t2 : Afficher chaque valeur en utilisant un parcours par indice via une boucle bornée.
print("\nTableau T2")
for i in range(len(t2)):
    print(t2[i])


# Tableau t3 : Afficher chaque valeur en utilisant un parcours par indice via une non boucle bornée.
print("\nTableau T3")
i=0
while i< len(t3):
    print(t3[i])
    i+=1
