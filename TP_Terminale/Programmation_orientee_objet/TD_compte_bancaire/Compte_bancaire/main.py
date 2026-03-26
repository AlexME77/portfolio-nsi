from CompteBancaire import CompteBancaire

if __name__ == "__main__":
    cb1 = CompteBancaire("0000", "Alexandre Mai--Emery", 0)

    cb1.versement(200)
    cb1.changeTaux(5)
    cb1.capitalisation(2)
    cb1.agios()
    cb1.afficher()