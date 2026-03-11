import turtle
import formes
import random

def mur(x, y, hauteur):
    """
    Dessine le mur d'une maison de largeur 100px.
    
    x       -- position x du coin inférieur gauche du mur
    y       -- position y du coin inférieur gauche du mur
    hauteur -- hauteur du mur
    """

    formes.rectangle(x, y, hauteur, 100)

def toit_triangle(x, y):
    """
    Dessine le toit d'une maison de largeur 100px de forme triangulaire.
    
    x        -- position x du coin inférieur gauche d'un toit
    y        -- position y du coin inférieur gauche d'un toit
    """

    formes.triangle(x, y, 100, 50)

def toit_rond(x, y):
    """
    Dessine le toit d'une maison de largeur 100px de forme arrondi.
    
    x        -- position x du coin inférieur gauche d'un toit
    y        -- position y du coin inférieur gauche d'un toit
    """

    formes.demi_cercle(x + 100, y, 50)

def porte(x, y, hauteur, largeur):
    """
    Dessine la porte de la maison de couleur grise.

    x       -- position x du coin inférieur gauche de la porte
    y       -- position y du coin inférieur gauche de la porte
    hauteur -- hauteur de la porte de la maison
    largeur -- largeur de la porte de la maison
    """

    formes.rectangle(x, y, hauteur, largeur)

def fenetre(x, y, cote):
    """
    Dessine une fenêtre de la maison avec 4 carreaux de couleur bleu. 

    x    -- position x du coin inférieur gauche de la fenêtre
    y    -- position y du coin inférieur gauche de la fenêtre
    cote -- longeueur du côté d'un seul carreau de la fenêtre
    """
    
    # Dessine 4 carrés ce qui va créer les 4 carreaux de la fenêtre.

    for i in range(2):
        turtle.begin_fill()
        turtle.fillcolor('lightcyan')
        formes.rectangle(x + cote*i, y, cote, cote)
        turtle.end_fill()
        turtle.right(90)
        i+=1
    
    for i in range (2):
        turtle.begin_fill()
        turtle.fillcolor('lightcyan')
        formes.rectangle(x + cote*i, y + cote, cote, cote)
        turtle.end_fill()
        turtle.right(90)
        i+=1

def nb_fenetre(x, y, hauteur_mur, nb_fenetre):
    """
    Dessine le nombre de fenêtre choisi (1, 2 ou 3 max)

    x           -- position x du coin inférieur gauche de la fenêtre
    y           -- position y du coin inférieur gauche de la fenêtre
    hauteur_mur -- hauteur d'un mur de la maison
    nb_fenetre  -- nombre de fenêtre dans la maison par étage
    """
    
    if nb_fenetre == 2:
        fenetre(x + 100/3 - hauteur_mur/10, y + hauteur_mur/2, hauteur_mur/10)
        fenetre(x + 2*(100/3) - hauteur_mur/10, y + hauteur_mur/2, hauteur_mur/10)
    elif nb_fenetre == 3:
        fenetre(x + 100/4 - hauteur_mur/10, y + hauteur_mur/2, hauteur_mur/10)
        fenetre(x + 2*(100/4) - hauteur_mur/10, y + hauteur_mur/2, hauteur_mur/10)
        fenetre(x + 3*(100/4) - hauteur_mur/10, y + hauteur_mur/2, hauteur_mur/10)
    else:
        fenetre(x + 100/2 - hauteur_mur/10, y + hauteur_mur/2, hauteur_mur/10)

def arbre(x, y, hauteur, largeur):
    """
    Dessine un arbre

    x       -- position du coin en bas à gauche du tronc de l'arbre 
    y       -- position y du coin en bas à gauche du tronc de l'arbre
    hauteur -- hauteur du tronc de l'arbre
    largeur -- largeur du tronc de l'arbre
    """

    # Dessin du tronc de l'arbre
    turtle.begin_fill()
    turtle.fillcolor('brown')
    formes.rectangle(x, y, hauteur, largeur)
    turtle.end_fill()

    # Dessin des feuilles de l'arbre
    turtle.begin_fill()
    turtle.fillcolor('limegreen')
    formes.triangle(x-30, y+hauteur, largeur+60, 150)
    turtle.end_fill()

def sol(couleur, nb_arbre):
    """
    Dessine le sol du paysage

    couleur  -- choisi la couleur du sol
    nb_arbre -- nombre d'arbre dans le paysage situé sur le sol
    """

    # Déssine un rectangle pour prendre tout l'espace de l'écran.

    turtle.begin_fill()
    turtle.fillcolor(couleur)
    formes.rectangle(-1000,-1000,900, 3000)
    turtle.end_fill()
    
    # Dessin des arbres
    for i in range(nb_arbre):
        if couleur == 'green':
            arbre(random.randint(-700, 700), random.randint(-400, -150), random.randint(30, 60), random.randint(5, 20))

def arc_en_ciel(largeur):
    """
    Dessine un arc en ciel

    largeur -- largeur entière de l'arc en ciel
    """

    colors = ('red', 'orange', 'yellow', 'lightgreen', 'lightblue', 'violet')
    turtle.pensize(10)
    for color in colors:
         turtle.pencolor(color)
         formes.demi_cercle(largeur, -100, largeur)
         turtle.left(90)
         turtle.up()
         turtle.forward(2*largeur + 10)
         turtle.down()
         largeur += 10
    turtle.pensize(1)
    turtle.pencolor('black')

def nuage(x, y):
    """
    Dessine les nuages dans le ciel

    x -- position x du haut du nuage
    y -- position y du haut du nuage
    """

    formes.position(x, y)
    turtle.pencolor('white')
    turtle.begin_fill()
    turtle.fillcolor('white')
    formes.cercle(x, y, 20)
    turtle.forward(20)
    for i in range(4):
        formes.cercle(x + 20, y, 20)
        turtle.right(90)
    turtle.end_fill()
    turtle.pencolor('black')   

def ciel(journuit):
    """
    Dessine le ciel du paysage

    journuit -- choisi la couleur du ciel selon si il fait jour (bleu clair) ou nuit (bleu foncé) et dessine la lune (grise) ou le soleil (jaune) en fonction du jour ou de la nuit
    """

    # Déssine un grand rectangle pour prendre tout l'espace de l'écran et un cercle pour le soleil ou la lune

    if journuit == 'jour':
        # Dessin du ciel de jour
        turtle.begin_fill()
        turtle.fillcolor('lightskyblue')
        formes.rectangle(-1000,-100,1000,3000)
        turtle.end_fill()

        # Dessin du soleil
        turtle.begin_fill()
        turtle.fillcolor('gold')
        formes.cercle(-550, 200, 50)
        turtle.end_fill()

        # Dessin d'un arc en ciel ou de nuages
        arc = random.choice(['oui', 'non'])

        if arc == 'oui':
            arc_en_ciel(500)
        else:
            for i in range(5):
                nuage(random.randint(-550, 500), random.randint(200, 300))
                turtle.penup()

       
    else:
        # Dessin du ciel de nuit
        turtle.begin_fill()
        turtle.fillcolor('midnightblue')
        formes.rectangle(-1000,-100,1000,3000)
        turtle.end_fill()

        # Dessin de la lune
        turtle.begin_fill()
        turtle.fillcolor('lightgray')
        formes.cercle(550, 200, 50)
        turtle.end_fill()

        # Dessin des étoiles
        for i in range(50):
            turtle.begin_fill()
            turtle.fillcolor('lightyellow')
            formes.etoile(random.randint(-1000, 1000), random.randint(-50, 400), 20)
            turtle.end_fill()   

def maison(x, y, hauteur_mur, forme_toit, nb_etages, fenetre, couleur_mur, couleur_toit):
    """
    Dessine une maison de 100px de largeur.

    x            -- position x du coin inférieur gauche de la maison
    y            -- position y du coin inférieur gauche de la maison
    hauteur_mur  -- hauteur d'un seul mur de la maison
    forme_toit   -- forme du toit : triangulaire ou arrondi
    nb_etages    -- nombre d'étages de la maison, donc le  nombre de mur
    fenetre      -- nombre de fenêtres de la maison
    couleur_mur  -- couleur des murs de la maison
    couleur_toit -- couleur du toit de la maison
    """
    
    # Dessine les murs de la maison
    formes.position(x, y)
    turtle.begin_fill()
    turtle.fillcolor(couleur_mur)
    for i in range (nb_etages):
        mur(x, y + hauteur_mur*i, hauteur_mur)
        i+=1
    turtle.end_fill()
        
    # Dessine le toit de la maison
    formes.position(x, y + hauteur_mur * nb_etages)
    if forme_toit == 'triangulaire':
        turtle.begin_fill()
        turtle.fillcolor(couleur_toit)
        toit_triangle(x, y + hauteur_mur * nb_etages)
    else:
        turtle.begin_fill()
        turtle.fillcolor(couleur_toit)
        toit_rond(x, y + hauteur_mur * nb_etages)
        turtle.left(90)  
    turtle.end_fill()
    
    # Dessine la porte de la maison
    turtle.begin_fill()
    turtle.fillcolor('gainsboro')
    porte(x + 100/2 - 20/2, y, hauteur_mur/3, 100/5)
    turtle.end_fill()

    # Dessine les fenêtres de la maison
    for i in range (nb_etages):
        nb_fenetre(x, y + hauteur_mur*i, hauteur_mur, fenetre)



def dessiner_paysage():
    """
    Dessine un paysage de 1, 2, ou 3 maisons sous Turtle avec le sol et le ciel.
    """
    # Dessine le ciel du paysage de nuit ou de jour
    ciel(random.choice(['jour', 'nuit']))

    # Dessine 1, 2, ou 3 maisons de couleurs de murs et de toit aléatoires
    for i in range (random.randint(1, 3)):
        maison(-200 + i*200, -100, random.randint(50, 125), random.choice(['triangulaire', 'circulaire']), random.randint(1, 3), random.randint(1, 3), random.choice(['beige', 'darkgrey', 'sandybrown']), random.choice(['indianred', 'dimgray']))

    # Dessine le sol du paysage avec une couleur aléatoire verte (herbe) ou grise (béton)
    sol(random.choice(['green', 'silver']), 10)

# Tests
if __name__ == "__main__":
    turtle.hideturtle()
    turtle.speed('fastest')
    ciel(random.choice(['jour', 'nuit']))
    sol(random.choice(['green', 'silver']), 10)
    for i in range (random.randint(1, 3)):
        maison(-200 + i*200, -100, random.randint(50, 125), random.randint(25, 75), random.randint(1, 3), random.randint(1, 3), random.choice(['beige', 'darkgrey', 'sandybrown']), random.choice(['indianred', 'dimgray']))
    turtle.tracer(True)
    turtle.mainloop()
