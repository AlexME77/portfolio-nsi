nom = str(input("Comment tu t'appelles ?"))
annee = input("Quelle est ton année de naissance ?")
if annee.isdigit() == False:
    exit("Erreur : l'année doit être un nombre")
if int(annee) <= 1900:
    exit("Erreur : tu dois être mort !")
if int(annee) >= 2024:
    exit("Erreur : tu n'est pas né !")
from datetime import date
annee_courante = date.today().year
age = int(annee_courante) - int(annee)
simineur = str((18 - age) + annee_courante)
if age >= 18:
    texte = "majeur"
else:
    texte = "mineur. Tu deviendra majeur en " + simineur
print("Bonjour",nom,"tu as",age,"ans. Tu es" ,texte,)
