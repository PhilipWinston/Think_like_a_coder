from turtle import *
bgcolor('red')
color('white')

begin_fill()
pensize(10)
circle(150)
end_fill()

penup()
goto(0,150)
pendown()
left(90)

color('black')
pensize(25)
for i in range(5):
    right(30)
    forward(50)
    right(90)
    forward(50)
    penup()
    goto(0,150)
    left(30)
    pendown()

exitonclick()