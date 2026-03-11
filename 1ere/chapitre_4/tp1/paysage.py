import turtle
import aide

def positionnement(x, y):
    """
    Positionne la tortue aux coordonnées (x, y).
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def mur(x, y, largeur, hauteur):
    """
    Dessine le mur d'une maison.

    x       -- position x du coin inférieur gauche du mur
    y       -- position y du coin inférieur gauche du mur
    largeur -- largeur du mur
    hauteur -- hauteur du mur
    """
    positionnement(x, y)
    turtle.goto(x, y + hauteur)
    turtle.goto(x + largeur, y + hauteur )
    turtle.goto(x + largeur, y)
    turtle.goto(x, y)


def toit(x, y, base, hauteur):
    """
    Dessine le toit d'une maison.

    x       -- position x du coin inférieur gauche du toit
    y       -- position y du coin inférieur gauche du toit
    base    -- largeur de la base du toit
    hauteur -- hauteur du toit
    """
    positionnement(x, y)
    turtle.goto(x + base / 2, y + hauteur)
    turtle.goto(x + base, y)
    turtle.goto(x, y)


def maison(x, y, etages):
    """
    Dessine une maison de 200px de largeur. Le mur fait 100px de hauteur et le toit, 50px de hauteur.

    x -- position x du coin inférieur gauche de la maison
    y -- position y du coin inférieur gauche de la maison
    etages -- nombre d'étages de la maison
    """
    
    largeur = 200
    hauteur_mur = 100
    hauteur_toit = 50
    
    for i in range (etages):
        mur(x, y + hauteur_mur*i, largeur, hauteur_mur)
        

    toit(x, y + hauteur_mur * etages, largeur, hauteur_toit)
    
def porte(x, y, nb_portes):
    """
    Dessine une porte de 10px de largeur et 20px de hauteur.
    
    x -- position x du coin inférieur gauche de la porte
    y -- position y du coin inférieur gauche de la porte
    """
    positionnement(x, y)
    turtle.goto(x, y + 30)
    turtle.goto(x + 20, y + 30)
    turtle.goto(x + 20, y)
    turtle.goto(x, y)
    
    nb_portes = 5
    
    for i in range (nb_portes):
        porte(x, y, positionnnement(x + 20 * 1, y))
    
    
def dessiner_paysage():
    """Dessine un paysage de 3 maisons sous Turtle."""
    
    maison(300, 0, 3)
    maison(0, 0, 2)
    maison(-300, 0, 4)

# Tests
if __name__ == "__main__":
    aide.grille()
    mur(-300, 0, 200, 100)
    toit(-300, 150, 200, 50)
    maison(0, 0, 2)
    porte(10, 0, 3)
    turtle.mainloop()
