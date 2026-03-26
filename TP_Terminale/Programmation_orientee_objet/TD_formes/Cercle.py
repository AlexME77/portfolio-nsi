import math
class Cercle :
    __origine = (0, 0)
    __rayon = 0.0

    def __init__(self, O, r):
        self.__origine = O
        self.__rayon = r
    
    def perimetre(self):
        return 2 * math.pi * self.__rayon
    
    def surface(self):
        return math.pi * self.__rayon * self.__rayon
    
    def testAppartenance(self, a):
        if math.sqrt((a[0] - self.__origine[0])**2 + (a[1] - self.__origine[1])**2) == self.__rayon:
            return True
        else:
            return False