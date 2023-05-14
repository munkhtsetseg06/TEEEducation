import turtle
def draw(x, y, t, r, R, color, f):
    turtle.penup()
    turtle.goto(x, y)
    turtle.right(t)
    turtle.pendown()
    turtle.pensize(0)
    turtle.fillcolor(color)  
    turtle.begin_fill()
    turtle.circle(r, R)
    turtle.left(90)
    turtle.forward(f)
    turtle.end_fill()  

# Main program
turtle.speed(10)  # Set the drawing speed
draw(-200, 0, -90, 50, -180, "#DB3237", 100)
draw(-250, 0, 90, 125, -180, "#FBBC04", 100)
draw(-250, 0, -90, 200, 180, "#FBBC04", 0)
draw(150, 0, 90, 75, 90, "#40A951", 75)
turtle.right(90)
turtle.forward(75)
draw(-150, 50, 90, 25, 360, "#FFF", 0)
draw(-155, 50, 90, 23, 360, "#000", 0)
draw(-170, 60, 90, 7, 360, "#FFF", 0)
draw(-162, 58, 90, 2, 360, "#FFF", 0)
draw(75, -25, 90, 75, -180, "#4284F4", 150)
turtle.done()
