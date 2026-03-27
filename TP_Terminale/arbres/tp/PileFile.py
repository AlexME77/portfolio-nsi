class PileFile :
	__liste=[]   #attributs privés de la classe Pile

	def __init__(self):
		pass

	def enfiler(self,element):
		self.__liste.append(element)
	
	def defiler(self) :
		if self.estVide() == False :
			return self.__liste.pop(0)
			
	def empiler(self,element):
		self.__liste.append(element)
			
	def depiler(self):
		if self.estVide()==False :
			return self.__liste.pop(-1)

	def estVide(self) :
		if (self.__liste == []) :
			return True
		else :
			return False

	def afficher(self) :
		print(self.__liste)
		return self.__liste
