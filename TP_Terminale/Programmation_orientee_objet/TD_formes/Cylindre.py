from Cercle import Cercle

class Cylindre :
    __cerc = Cercle((0,0), 0.0)
    __hauteur = 0.0

    def __init__(self, cerc, h):
        self.__cerc = cerc
        self.__hauteur = h
    
    def volume(self):
        return self.__cerc.surface() * self.__hauteur