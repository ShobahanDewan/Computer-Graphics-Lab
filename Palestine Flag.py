import turtle

# Set up screen
screen = turtle.Screen()
screen.title("Palestine Flag")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)

# Function to draw rectangle
def draw_rectangle(color, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

# Draw black stripe
draw_rectangle("black", -150, 100, 300, 33.33)

# Draw white stripe
draw_rectangle("white", -150, 66.67, 300, 33.33)

# Draw green stripe
draw_rectangle("green", -150, 33.33, 300, 33.33)

# Draw red triangle
pen.penup()
pen.goto(-150, 100)
pen.pendown()
pen.color("red")
pen.begin_fill()
pen.goto(-150, 0)
pen.goto(-50, 50)
pen.goto(-150, 100)
pen.end_fill()

# Hide turtle
pen.hideturtle()
turtle.done()
