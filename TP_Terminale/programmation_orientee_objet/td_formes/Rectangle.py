class Rectangle :
    __largeur = 0.0
    __longueur = 0.0

    def __init__(self, lar, lon):
        self.__largeur = lar
        self.__longueur = lon
    
    def perimetre(self):
        return (self.__largeur + self.__longueur) * 2
    
    def surface(self):
        return self.__largeur * self.__longueur