import turtle
import aide

# Tracé de la grille
aide.grille()

# Tracé de démonstration
turtle.goto(40, 40)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.penup()
turtle.backward(20)
turtle.pendown()
turtle.backward(20)

# Boucle des événements
turtle.mainloop()

