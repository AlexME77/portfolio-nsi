class CompteBancaire :
    __numeroCompte = ""
    __nom = ""
    __solde = 0.0
    __taux = 3.0
    
    def __init__(self, numeroCompte, nom, solde):
        self.__numeroCompte = numeroCompte
        self.__nom = nom
        self.__solde = solde

    def versement(self, montant):
        if montant>0:
            self.__solde += montant
        else:
            print("Vous ne pouvez pas verser un montant négatif ou nul d'argent sur votre compte")
    
    def retrait(self, montant):
        if -500<=self.__solde-montant:
            self.__solde-=montant
        else:
            print("Vous ne pouvez pas dépasser un découvert de plus de 500€.")
    
    def agios(self):
        if self.__solde<0:
            self.__solde-=-(self.__solde*0.05)

        
    def changeTaux(self, taux):
        self.__taux = taux

    def capitalisation(self, nb_mois):
        if self.__solde>=0:
            interet = self.__taux/100*self.__solde
            self.__solde+=interet*nb_mois
    
    def afficher(self):
        print("Numéro de compte : " + self.__numeroCompte)
        print("Nom du propriétaire du compte : " + self.__nom)
        print("Solde : " + str(self.__solde) + "€")
        print("Taux d'intérêt : " + str(self.__taux) + "%")