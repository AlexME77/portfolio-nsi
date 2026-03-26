import turtle
import aide
aide.grille()
import formes

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
formes.polygone(3, 50)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
formes.polygone(4, 50)

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
formes.polygone(100, 50)