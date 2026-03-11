import turtle

def position(x, y):
    """
    Positionne la tortue aux coordonnées (x, y)

    x -- position x de la tortue
    y -- position y de la tortue
    """

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def triangle(x, y, base, hauteur):
    """
    Dessine un triangle.

    x       -- position x du coin inférieur gauche du triangle
    y       -- position y du coin inférieur gauche du triangle
    base    -- base du triangle
    hauteur -- hauteur du triangle
    """

    position(x, y)
    turtle.goto(x + base / 2, y + hauteur)
    turtle.goto(x + base, y)
    turtle.goto(x, y)

def rectangle(x, y, hauteur, largeur):
    """
    Dessine un rectangle
    x       -- position x du coin inférieur gauche du rectangle
    y       -- position y du coin inférieur gauche du rectangle
    hauteur -- hauteur du rectangle
    largeur -- largeur du rectangle
    """

    position(x, y)
    turtle.goto(x, y + hauteur)
    turtle.goto(x + largeur, y + hauteur )
    turtle.goto(x + largeur, y)
    turtle.goto(x, y)

def cercle(x, y, diametre):
    """
    Dessine un cercle
    x        -- position x du bas du cercle
    y        -- position y du bas du cercle
    diametre -- diametre du cercle
    """

    position(x, y)
    turtle.circle(diametre)

def demi_cercle(x, y, diametre):
    """
    Dessine un demi cercle avec le coté plat vers le bas
    x        -- position x de la droite du demi cercle
    y        -- position y de la droite du demi cercle
    diametre -- diametre du demi cercle
    """

    position(x, y)
    turtle.left(90)
    turtle.circle(diametre,180)

def etoile(x, y, longueur):
    """
    Dessine une étoile
    x        -- position x du coin en haut à gauche de l'étoile
    y        -- position y du coin en haut à gauche de l'étoile
    longueur -- longueur de l'étoile
    """
    position(x, y)
    turtle.right(36)
    for i in range(5):
        turtle.forward(longueur)
        turtle.left(144)

# Tests
if __name__ == "__main__":
    position(0, 0)
    triangle (0, 0, 50, 50)
    rectangle(100, 0, 50, 20)
    cercle(-100, 0, 50)
    demi_cercle(-200, 0, 40)
    etoile(200, 0, 30)
    turtle.mainloop()