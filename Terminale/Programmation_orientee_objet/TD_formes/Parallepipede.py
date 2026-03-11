from Rectangle import Rectangle

class Parallepipede:
    __rect = Rectangle(0.0, 0.0)
    __hauteur = 0.0

    def __init__(self, rect, hau):
        self.__rect = rect
        self.__hauteur = hau

    def volume(self):
        return self.__rect.surface() * self.__hauteur

    
    