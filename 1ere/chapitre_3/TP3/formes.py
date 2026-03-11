import turtle

def carre(longueur):
    i=0
    while i<4:
        turtle.forward(longueur)
        turtle.right(90)
        i+=1
        
def triangle(longueur):
    i=0
    while i<3:
        turtle.forward(longueur)
        turtle.left(120)
        i+=1

def polygone(n, longueur):
    i=0
    while i < n:
        turtle.forward(longueur)
        turtle.right(360/n)
        i = i + 1
        
def dessin_1(n, longueur):
    '''Dessine une combinaison de "n" carrés de taille "longueur"'''
    while n > 0:
        carre(longueur)
        turtle.right(10)
        n = n - 1


def dessin_2(n, longueur):
    '''Dessine une série de "n" carrés de taille "longueur"'''
    while n > 0:
        carre(longueur)
        turtle.penup()
        turtle.forward(2 * longueur)
        turtle.pendown()
        turtle.right(10)
        n = n - 1