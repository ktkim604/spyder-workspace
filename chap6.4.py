import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")

for i in range(10):
    for j in range(5):
        t.left(144)
        t.forward(100)
    t.left(10)
    
turtle.done()