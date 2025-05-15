import turtle
import colorsys

# Setup
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.width(2)

# Colors
hue = 0

# Draw pattern
for i in range(120):
    t.color(colorsys.hsv_to_rgb(hue, 1, 1))  # Rainbow effect
    t.circle(100)
    t.left(30)
    t.circle(100)
    t.left(30)
    t.circle(100)
    t.left(30)
    t.circle(100)
    t.left(30)
    t.circle(100)
    t.left(30)
    t.circle(100)
    
    t.left(5)  # Rotate slightly for full circular pattern
    hue += 0.0083  # Gradually change color

t.hideturtle()
turtle.done()
