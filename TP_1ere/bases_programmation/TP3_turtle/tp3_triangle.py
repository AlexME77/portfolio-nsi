import turtle
import aide
aide.grille()
import formes

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
formes.triangle(20)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
formes.triangle(100)

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
formes.triangle(200)

turtle.mainloop