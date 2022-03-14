"""A grey man in front of his beautiful house on a nice day with a lake in the background!"""

__author__ = "730476939"

from turtle import Turtle, colormode, done


def main() -> None:
    """Putting the pieces together."""
    builder: Turtle = Turtle()
    tree_leaves(builder, -650, 200, 100, 255, 165, 0)
    rectangle(builder, -700, -350, 1400, 400, 124, 252, 0)
    rectangle(builder, -700, 50, 1400, 400, 0, 191, 255)
    rectangle(builder, -700, -100, 300, 150, 30, 144, 255)
    rectangle(builder, -500, 75, 300, 100, 255, 255, 255)
    rectangle(builder, -200, 170, 200, 50, 255, 255, 255)
    rectangle(builder, 100, 112, 142, 50.25, 255, 255, 255)
    rectangle(builder, 400, 200, 93, 46, 255, 255, 255)
    rectangle(builder, 250, 250, 150, 80.32, 255, 255, 255)
    tree_leaves(builder, -650, 200, 100, 255, 165, 0)
    house(builder, -80, -140, 250)
    window(builder, 100, 0, 100)
    window_line(builder, 50, 50, 50)
    rectangle(builder, -80, -140, 100, 80, 165, 42, 42)
    rectangle(builder, -350, -200, 250, 80, 165, 42, 42)
    rectangle(builder, 355, -150, 200, 80, 165, 42, 42)
    tree_leaves(builder, 410, 105, 80, 50, 205, 50)
    rectangle(builder, 500, -200, 200, 80, 165, 42, 42)
    tree_leaves(builder, -275, 100, 100, 50, 205, 50)
    tree_leaves(builder, 560, 50, 80, 75, 205, 50)
    rectangle(builder, 0, -200, 60, 30, 255, 0, 0)
    head(builder, 10, -115)
    done()


def house(shape: Turtle, x: float, y: float, width: float) -> None:
    """Shape for the house."""
    i = 0
    shape.penup()
    shape.goto(x, y)
    shape.pendown()
    shape.begin_fill()
    shape.pencolor("pink")
    shape.fillcolor(32, 67, 93)
    shape.color("green", "yellow")
    while i < 6:
        shape.forward(width)
        shape.left(90)
        i += 1
        while i < 4:
            shape.forward(width)
            shape.left(60)
            i += 1
    shape.end_fill()
    shape.speed(0)


def window(square: Turtle, x: float, y: float, width: float) -> None:
    """Square for window."""
    i = 0
    square.penup()
    square.goto(x, y)
    square.pendown()
    square.begin_fill()
    colormode(255)
    square.color(0, 191, 255)
    while i < 4:
        square.forward(width)
        square.left(90)
        square.speed(0)
        i += 1
    square.end_fill()


def window_line(cross: Turtle, x: float, y: float, width: float) -> None:
    """Cross for window lining."""
    i = 0
    while i < 4:
        colormode(255)
        cross.color(0, 0, 0)
        cross.penup()
        cross.goto(x, y)
        cross.pendown()
        cross.forward(width)
        cross.left(90)
        cross.speed(0)
        i += 1
    

def rectangle(rec: Turtle, x: float, y: float, width: float, height: float, r: float, g: float, b: float) -> None:
    """Rectangle used for all rectangular objects."""
    rec.begin_fill()
    colormode(255)
    rec.color(r, g, b)
    rec.penup()
    rec.goto(x, y)
    rec.pendown()

    rec.forward(width) 
    rec.left(90)
    
    rec.forward(height)
    rec.left(90) 
    
    rec.forward(width)
    rec.left(90) 
    
    rec.forward(height) 
    rec.left(90) 
    rec.end_fill()
    

def tree_leaves(octa: Turtle, x: float, y: float, width: float, r: float, g: float, b: float) -> None:
    """Octagon for the amazing tree leaves."""
    octa.begin_fill()
    colormode(255)
    octa.color(r, g, b)
    octa.pencolor(0, 0, 0)
    octa.penup()
    octa.goto(x, y)
    octa.pendown()
    i = 0
    while i <= 7:
        octa.forward(width)
        octa.left(45)
        octa.speed(0)
        i += 1
    octa.end_fill()


def head(circle: Turtle, x: float, y: float) -> None:
    """Little grey mans head."""
    circle.begin_fill()
    colormode(255)
    circle.color(125, 125, 125)
    circle.penup()
    circle.goto(x, y)
    circle.pendown()
    circle.circle(25)
    circle.end_fill()


if __name__ == "__main__":
    main()