import turtle
import colorsys

# Setup screen and turtle
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Initialize color hue
hue = 0
n = 36  # number of petals per rotation
rotations = 10  # spiral arms

for i in range(360):
    t.color(colorsys.hsv_to_rgb(hue, 1, 1))
    t.forward(i * 0.5)
    t.left(360 / n + 1)
    hue += 0.005

t.hideturtle()
turtle.done()
