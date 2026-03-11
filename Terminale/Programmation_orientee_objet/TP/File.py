class PileFile:
    __liste = []
    __taille = 0

    def __init__(self, taille):
        self.__taille = taille
        self.__liste = [None] * taille

    def estPleine(self):
        for element in self.__liste:
            if element == None:
                return False
        return True

    def estVide(self):
        for element in self.__liste:
            if element != None:
                return False
        return True

    def empiler(self, element):
        if self.estPleine() == False:
            for i in range(self.__taille):
                if self.__liste[i] == None:
                    self.__liste[i] = element
                    break
        else:
            print("La pile est pleine")
    
    def depiler(self):
        if self.estVide() == False:
            for i in range(self.__taille):
                if self.__liste[i] == None:
                    last = self.__liste[i-1]
                    self.__liste[i-1] = None
                    break
            return last
        else:
            print("La pile est vide")
    
    def afficher(self):
        for element in self.__liste:
            print(element)
    
    def enfiler(self, element):
        if self.estPleine() == False:
            for i in range(self.__taille):
                if self.__liste[i] == None:
                    self.__liste[i] = element
                    break
        else:
            print("La pile est pleine")
    
    def defiler(self):
        if self.estVide() == False:
            first = self.__liste[0]
            self.__liste[0] = None
            for i in range(self.__taille-1):
                self.__liste[i] = self.__liste[i+1]
            self.__liste[self.__taille-1] = None
            return first
        else:
            print("La file est vide")
