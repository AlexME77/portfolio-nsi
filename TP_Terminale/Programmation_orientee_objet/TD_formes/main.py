from Rectangle import Rectangle
from Parallepipede import Parallepipede
from Cercle import Cercle
from Cylindre import Cylindre

if __name__ == "__main__":
    r = Rectangle(4.5, 5.3)
    p = Parallepipede(r, 3.2)
    ce = Cercle((0,0),5)
    cy = Cylindre(ce, 5)

    print(str(r.perimetre()) + " m")
    print(str(r.surface()) + " m2")
    print(str(p.volume()) + " m3")
    print(str(ce.surface()) + " m2")
    print(str(ce.perimetre()) + " m")
    if ce.testAppartenance((0,5)):
        print("Le point appartient au cercle")
    else:
        print("Le point n'appartient pas au cercle")
    print(str(cy.volume()) + " m3")