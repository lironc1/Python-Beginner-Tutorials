import random
import turtle

turtle.speed(0)

################################################################## PART I

for i in range(15):
    turtle.write(i)
    turtle.right(90)
    turtle.forward(160)
    turtle.right(180)
    turtle.forward(160)
    turtle.right(90)
    turtle.forward(30)


################################################################## PART II

liron = turtle.Turtle()
liron.color('pink')
liron.shape('turtle')
liron.penup()
liron.goto(0, -50)
liron.pendown()

tomer = turtle.Turtle()
tomer.color('blue')
tomer.shape('turtle')
tomer.penup()
tomer.goto(0, -100)
tomer.pendown()

################################################################## PART III

for turn in range(100):
    lironRun = random.randint(1, 5)
    liron.forward(lironRun)
    tomerRun = random.randint(1, 5)
    tomer.forward(tomerRun)

