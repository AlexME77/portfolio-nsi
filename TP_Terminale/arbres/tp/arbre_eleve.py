from PileFile import PileFile
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20, 6)

class arbre:

# à compléter
	def __init__(self):
		pass

	def taille(self, t):
		if self.estVide(t):
			return 0
		else:
			taille_gauche=self.taille(t[1])
			taille_droite=self.taille(t[2])
			return 1+taille_gauche+taille_droite

	def hauteur(self, t):
		if self.estVide(t):
			return -1
		else:
			hauteur_gauche=self.hauteur(t[1])
			hauteur_droite=self.hauteur(t[2])
			return 1+max(hauteur_gauche, hauteur_droite)

	def estVide(self, t):
		if t==[] or t==None:
			return True
		else:
			return False

	def dessiner_aux(self,t, rect, dy, labels, avl=False):
		if (self.estVide(t)):
			return
		x1, x2, y1, y2=rect
		xm= (x1+x2) //2
		x, t1, t2 = t
		self.dessiner_aux(t1, (x1, xm, y1, y2-dy), dy, labels, avl)
		self.dessiner_aux(t2, (xm, x2, y1, y2-dy), dy, labels, avl)
		if labels:
			if avl:
				plt.text(xm, y2, str(x[0]), fontsize=12, horizontalalignment='center')
			else:
				plt.text(xm, y2, str(x), fontsize=12, horizontalalignment='center')
		if not self.estVide(t1):
			a, b= ((xm, (x1+xm) //2), (y2, y2-dy))
			plt.plot(a, b, 'k', marker='o', markerfacecolor='c', markersize=25)
		if not self.estVide(t2):
			c, d= ((xm, (x2+xm) //2), (y2, y2-dy))
			plt.plot(c, d, 'k', marker='o', markerfacecolor='c', markersize=25)

	def dessiner(self,t, labels=True, avl=False):
		d=512
		pad=20
		dy= (d-2*pad) / (self.hauteur(t))
		self.dessiner_aux(t, (pad, d-pad, pad, d-pad), dy, labels, avl)
		plt.axis([0, d, 0, d])
		plt.axis('off')
		plt.show()

	def parcours_largeur(self,t):
		visite = PileFile()
		lst = []
		visite.enfiler(t)
		while visite.estVide() == False:
			visite.afficher()
			noeud = visite.defiler()
			if type(noeud) == list and noeud != []:
				lst.append(noeud[0])
				if noeud[1] != []:
					visite.enfiler(noeud[1])
				if noeud[2] != []:
					visite.enfiler(noeud[2])
			else:
				lst.append(noeud)
		return lst
	
	def parcours_profondeur(self,t):
		visite = PileFile()
		lst = []
		visite.empiler(t)
		while visite.estVide() == False:
			visite.afficher()
			noeud = visite.depiler()
			if type(noeud) == list and noeud != []:
				lst.append(noeud[0])
				if noeud[2] != []:
					visite.empiler(noeud[2])
				if noeud[1] != []:
					visite.empiler(noeud[1])
			else:
				lst.append(noeud)
		return lst
	
	def parcours_profondeur_recursif_prefix(self, t):
		lst = []
		if type(t) == list and t != []:
			lst.append(t[0])
			print(lst)
			if t[1] != []:
				res1 = self.parcours_profondeur_recursif_prefix(t[1])
				lst.append(res1)
				print(lst)
			if t[2] != []:
				res2 = self.parcours_profondeur_recursif_prefix(t[2])
				lst.append(res2)
				print(lst)
		else:
			lst.append(t)
			print(lst)
		return lst
	
	def parcours_profondeur_recursif_infixe(self, t):
		lst = []
		if type(t) == list and t != []:
			if t[1] != []:
				res1 = self.parcours_profondeur_recursif_infixe(t[1])
				lst.append(res1)
				print(lst)
			lst.append(t[0])
			print(lst)
			if t[2] != []:
				res2 = self.parcours_profondeur_recursif_infixe(t[2])
				lst.append(res2)
				print(lst)
		else:
			lst.append(t)
			print(lst)
		return lst
	
	def parcours_profondeur_recursif_postfixe(self, t):
		lst = []
		if type(t) == list and t != []:
			if t[1] != []:
				res1 = self.parcours_profondeur_recursif_postfixe(t[1])
				lst.append(res1)
				print(lst)
			if t[2] != []:
				res2 = self.parcours_profondeur_recursif_postfixe(t[2])
				lst.append(res2)
				print(lst)
			lst.append(t[0])
		else:
			lst.append(t)
			print(lst)
		return lst