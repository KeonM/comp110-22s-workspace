from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.begin_fill()
leo.penup()
leo.goto(45, 60)
leo.pendown()
colormode(255)
leo.color(125, 125, 125)
leo.speed(50)
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")


i = 0
while i < 3:
    leo.forward(200)
    leo.left(120)
    i += 1
leo.end_fill()
leo.hideturtle()
print(leo)
done()