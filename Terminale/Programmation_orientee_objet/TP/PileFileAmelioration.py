class PileFileAmelioration:
    __liste = []

    def __init__(self):
        self.__liste = []

    def estVide(self):
        if self.__liste == []:
            return True
        else:
            return False

    def empiler(self, element):
        self.__liste.append(element)
    
    def depiler(self):
        if self.estVide() == False:
            last = self.__liste[len(self.__liste)-1]
            self.__liste.pop(len(self.__liste)-1)
            return last
        else:
            print("La pile est vide")
    
    def afficher(self):
        for element in self.__liste:
            print(element)
    
    def enfiler(self, element):
        self.__liste.append(element)
    
    def defiler(self):
        if self.estVide() == False:
            first = self.__liste[0]
            self.__liste.pop(0)
            return first
        else:
            print("La pile est vide")
