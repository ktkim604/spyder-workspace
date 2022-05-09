import turtle 
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

def draw_line():
    t.forward(100)
    t.forward(-100)
    t.right(30)
    
    
for i in range(12):
    draw_line()

turtle.done()
turtle.exitonclick()