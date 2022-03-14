from turtle import Turtle, colormode, done
bob: Turtle = Turtle()
side_length: int = 300

bob.penup()
bob.goto(-12, 35)
bob.pendown()

bob.begin_fill()
colormode(255)
bob.color(124, 123, 154)
bob.speed(50)


i = 0
while i < 3:
    bob.forward(side_length)
    bob.left(120)
    i+=1
bob.end_fill()
print(bob)

bob.penup()
bob.goto(-12, 35)
bob.pendown()

colormode(255)
bob.color(255, 0, 154)
bob.speed(50)


i = 0
while i < 3:
    side_length = side_length * 1
    bob.forward(side_length)
    bob.left(120)
    i+=1
print(bob)
done()