import turtle


t = turtle.Turtle()
t.speed(3)
turtle.bgcolor("light blue")

# 🌼 ফুলের কেন্দ্র
t.penup()
t.goto(0, 0)
t.color("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

# 🌸 প্রতিটা পাপড়ি (no loop)
t.color("Purple")

# পাপড়ি ১+++++
t.penup()
t.goto(35, -35)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# পাপড়ি 2+++
t.penup()
t.goto(50, 0)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# পাপড়ি 3+++
t.penup()
t.goto(35, 35)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()


# পাপড়ি 4+++
t.penup()
t.goto(0, 50)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()


# পাপড়ি 5++++
t.penup()
t.goto(-35, 35)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# পাপড়ি 6
t.penup()
t.goto(-50, 0)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()


# পাপড়ি 7
t.penup()
t.goto(-35, -35)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()



# 🌱 ডাঁটা (লাঠি) - এখন ঠিক পাপড়ির নিচে
t.penup()
t.goto(0, 0)
t.setheading(-90)
t.pendown()
t.color("green")
t.pensize(6)
t.forward(160)

# 🌿 বড় পাতা (ডাঁটার সাথে লাগানো)
t.penup()
t.goto(0, -100)
t.setheading(-45)
t.pendown()
t.color("forest green")
t.begin_fill()
t.circle(65, 90)
t.left(90)
t.circle(65, 90)
t.end_fill()

# 🟫 মাটি
t.penup()
t.goto(-120, -162)
t.setheading(0)
t.pendown()
t.color("sienna")
t.pensize(3)
t.forward(240)

t.hideturtle()
turtle.done()
