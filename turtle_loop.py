
import turtle

"""
turtle.tracer(1)
rounds = 10
size = 10
mike = turtle.clone()
steve = turtle.clone()
turtle.bgcolor("white")
turtle.hideturtle()
mike.color("gold")
steve.color("blue")
steve.goto(5,5)
while True:
    mike.forward(size)
    mike.left(90)
    steve.forward(-size)
    steve.left(-90)
    size += 10
"""

line1 = turtle.Turtle()
line1.color("Peach Puff")
size = 5
line1.left(45)
line1.forward(100)  
line1.right(45)
line1.forward(50)
line1.right(90)
line1.forward(200)
line1.right(90)
line1.forward(50)
line1.left(135)
line1.forward(100)  

turtle.mainloop()
