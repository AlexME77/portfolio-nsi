import sqlite3

#Connexion
connexion = sqlite3.connect('db_livres_auteur.db')

#Recuperation d'un curseur
c = connexion.cursor()

deletelivres = """
DELETE FROM LIVRES
WHERE ann_publi<2000
"""
deleteauteurs = """
DELETE FROM AUTEURS
WHERE ann_naissance<2000
"""

defaultauteurs = """
INSERT INTO AUTEURS
(id,nom,prenom,ann_naissance,langue_ecriture)
VALUES
(1,"Orwell","George",1903,"anglais"),
(2,"Herbert","Frank",1920,"anglais"),
(3,"Asimov","Isaac",1920,"anglais"),
(4,"Huxley","Aldous",1894,"anglais"),
(5,"Bradbury","Ray",1920,"anglais"),
(6,"K.Dick","Philip",1928,"anglais"),
(7,"Barjavel","René",1911,"français"),
(8,"Boulle","Pierre",1912,"français"),
(9,"Van Vogt","Alfred Elton",1912,"anglais"),
(10,"Verne","Jules",1828,"français");
"""
defaultlivres = """
INSERT INTO LIVRES
(id,titre,id_auteur,ann_publi,note)
VALUES
(1,"1984",1,1949,10),
(2,"Dune",2,1965,8),
(3,"Fondation",3,1951,9),
(4,"Le meilleur des mondes",4,1931,7),
(5,"Fahrenheit 451",5,1953,7),
(6,"Ubik",6,1969,9),
(7,"Chroniques martiennes",5,1950,8),
(8,"La nuit des temps",7,1968,7),
(9,"Blade Runner",6,1968,8),
(10,"Les Robots",3,1950,9),
(11,"La Planète des singes",8,1963,8),
(12,"Ravage",7,1943,8),
(13,"Le Maître du Haut Château",6,1962,8),
(14,"Le monde des Ā",9,1945,7),
(15,"La Fin de l'éternité",3,1955,8),
(16,"De la Terre à la Lune",10,1865,10);
"""

afficher = """
SELECT titre, nom, prenom, ann_publi, langue_ecriture, note
FROM LIVRES JOIN AUTEURS
ON LIVRES.id_auteur = AUTEURS.id
"""

data1 = """
DELETE FROM LIVRES
WHERE ann_publi<1945;
"""
data2 = """
SELECT titre
FROM LIVRES
WHERE note>=7;
"""
data3 = """
SELECT A.prenom, A.nom, AVG(L.note) as moyenne
FROM AUTEURS A
JOIN LIVRES L ON A.id = L.id_auteur
GROUP BY A.id
ORDER BY moyenne DESC
LIMIT 1;
"""
data4 = """
UPDATE LIVRES
SET note=10
WHERE id_auteur=3 and ann_publi>1950;
"""
data5 = """
DELETE FROM LIVRES
WHERE ann_publi>1945
AND id_auteur IN (SELECT id FROM AUTEURS WHERE langue_ecriture="français");
"""
data6 = """
SELECT titre
FROM LIVRES JOIN AUTEURS ON LIVRES.id_auteur = AUTEURS.id
WHERE LIVRES.note>=7 AND AUTEURS.langue_ecriture='anglais';
"""
data7 = """
SELECT A.prenom, A.nom, AVG(L.note) as moyenne
FROM AUTEURS A
JOIN LIVRES L ON A.id = L.id_auteur
WHERE A.langue_ecriture != 'anglais'
GROUP BY A.id
ORDER BY moyenne DESC
LIMIT 1;
"""
data8a = """
INSERT INTO AUTEURS (id, nom, prenom, ann_naissance, langue_ecriture)
VALUES
(11, 'King', 'Stephen', 1947, 'anglais'),
(12, 'Chizmar', 'Richard', 1965, 'anglais'),
(13, 'Hassan', 'Yaël', 1952, 'français'),
(14, 'Radenac', 'Matthieu', 1984, 'français'),
(15, 'Farenc', 'Jean-Claude', 1950, 'français'),
(16, 'Kiefer', 'Michel', 1950, 'français'),
(17, 'Ives', 'Laurent', 1950, 'français');
"""
data8b = """
INSERT INTO LIVRES (id, titre, id_auteur, ann_publi, note)
VALUES
(17, 'Gwendy et la boite à boutons', 11, 2017, 8),
(18, 'Gwendy et la boite à boutons', 12, 2017, 8),
(19, 'La fille qui n’aimait pas les fins', 13, 2015, 7),
(20, 'La fille qui n’aimait pas les fins', 14, 2015, 7),
(21, 'Il fallait retrouver Nadia', 15, 2010, 7),
(22, 'Il fallait retrouver Nadia', 16, 2010, 7),
(23, 'Il fallait retrouver Nadia', 17, 2010, 7);
"""
data9 = """
SELECT titre, COUNT(id_auteur) as nb_auteurs
FROM LIVRES
GROUP BY titre
HAVING COUNT(id_auteur) >= 2;
"""

c.execute(data9)
livres = c.fetchall()


for element in livres:
    print(element)


#Deconnexion
connexion.close()