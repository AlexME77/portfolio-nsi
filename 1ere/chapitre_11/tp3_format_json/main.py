import json

    # Intégrer le code des réponses aux questions à partir d'ici

def nb_cine_idf(fichier):
    nb=0
    for cine in fichier:
        if "fields" in cine:
            if cine["fields"]["region_administrative"]=="ILE-DE-FRANCE":
                nb+=1
    print(nb)

def descripteur_cine(fichier):
    for cine in fichier:
        print(cine["fields"].keys())

def cine_chelles(fichier):
    for cine in fichier:
        if "fields" in cine:
            if cine["fields"]["commune"]=="Chelles":
                print(cine["fields"]["nom"])

with open("cinemas.json") as fichier:
    donnees = json.load(fichier)
    print(cine_chelles(donnees))
    
    