import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(5)  # Increased speed for faster drawing
turtle.bgcolor("lightblue") # Changed background to light blue for sky

# Function to draw a square
def draw_square(color, size):
    t.color("black", color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# Function to draw a triangle (for roof)
def draw_triangle(color, size):
    t.color("black", color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# --- Draw House ---

# Draw house base
t.penup()
t.goto(-100, -150)
t.pendown()
draw_square("lightgray", 200) # Changed house color to light gray

# Draw roof
t.penup()
t.goto(-100, 50)  # Top-left corner of the house
t.pendown()
t.setheading(0)
t.color("black", "firebrick")
t.begin_fill()
t.forward(200)         # Base of the roof
t.goto(0, 150)         # Top of the triangle
t.goto(-100, 50)       # Back to start
t.end_fill()

# Draw door
t.penup()
t.goto(-25, -150)
t.pendown()
t.setheading(0)
draw_square("saddlebrown", 50)

# Draw left window
t.penup()
t.goto(-85, -50)
t.pendown()
draw_square("white", 40)

# Draw right window
t.penup()
t.goto(45, -50)
t.pendown()
draw_square("white", 40)

# --- Draw Sun ---
t.penup()
t.goto(100, 150) # Moved sun to top right
t.pendown()
t.color("orange") # Changed sun color to orange
t.begin_fill()
t.circle(40)     # Slightly smaller sun
t.end_fill()

# --- Draw Flag ---

# Draw flag stand (pole)
t.penup()
t.goto(200, -150) # Positioned flag pole to the right of the house
t.pendown()
t.color("black", "saddlebrown") # Changed pole color to brown
t.begin_fill()
for _ in range(2):
    t.forward(10)  # Slightly thinner pole
    t.left(90)
    t.forward(300) # Shorter pole
    t.left(90)
t.end_fill()

# Draw flag (green rectangle)
t.penup()
t.goto(210, 150) # Positioned flag to the right of the pole
t.pendown()
t.color("black", "darkgreen") # Changed flag color to dark green
t.begin_fill()
for _ in range(2):
    t.forward(150)  # Width
    t.right(90)
    t.forward(90)   # Height
    t.right(90)
t.end_fill()

# Draw red circle on flag
t.penup()
circle_x = 210 + (150 / 2) # Center of the flag width
circle_y = 150 - (90 / 2) - 25 # Center of the flag height, adjust for circle radius
t.goto(circle_x, circle_y)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(25) # Smaller circle
t.end_fill()

# Finish
t.hideturtle()
turtle.done()
