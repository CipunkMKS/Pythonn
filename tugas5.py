import turtle
star = turtle.Turtle()
star.right(75)
star.forward(100)
star.fillcolor("yellow")
star.begin_fill()

for i in range(4):
    star.right(144)
    star.forward(100)
     
star.end_fill()
turtle.done()