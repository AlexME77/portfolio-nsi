class PileFile :
	__liste=[]
	tailleListe=0	#attributs de la classe PileFile

	def __init__(self):
 		self.__liste =[]

	def enfiler(self,element):
		self.__liste.append(element)
		self.__tailleListe=len(self.__liste)

	def defiler(self) :
		val= self.__liste.pop(0)
		self.__tailleListe=len(self.__liste)
		return val

	def estVide(self) :
		if self.__liste == [] :
			return True
		else :
			return False


