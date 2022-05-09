import turtle
import random

image1 = "C:\\Users\kim kyu tae\Pictures\파이썬 사진자료\\rabbit.gif"
image2 = "C:\\Users\kim kyu tae\Pictures\파이썬 사진자료\\turtle.gif"
image3 = "C:\\Users\kim kyu tae\Pictures\파이썬 사진자료\\tiger.gif"

s = turtle.Screen()
s.addshape(image1)
s.addshape(image2)
s.addshape(image3)

t1 = turtle.Turtle()
t1.shape(image1)
t1.pensize(5)
t1.penup()
t1.goto(-300,0)


t2 = turtle.Turtle()
t2.shape(image2)
t2.pensize(5)
t2.penup()
t2.goto(-300,-200)

t3 = turtle.Turtle()
t3.shape(image3)
t3.pensize(5)
t3.penup()
t3.goto(-300,200)

t1.pendown()
t2.pendown()
t3.pendown()
t1.speed(1)
t2.speed(1)
t3.speed(1)

for i in range(50):
    d1 = random.randint(1,25)
    t1.forward(d1)
    d2 = random.randint(1,25)
    t2.forward(d2)
    d3 = random.randint(1,25)
    t3.forward(d3)


turtle.done()
turtle.exitonclick()