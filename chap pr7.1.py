import turtle 
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def draw_hexa():
    for i in range(6):
        t.forward(100)
        t.left(360/6)
        
for i in range (6):
    draw_hexa()
    turtle.forward(100)
    turtle.right(60)

turtle.done()
turtle.exitonclick()