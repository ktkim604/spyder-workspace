import turtle

def draw_shape(radius, color1):
    t.left(270)
    t.width(3)
    t.color()
    t.color("black", color1)
    t.begin_fill()
    t.circle(radius/2.0, -180)
    t.circle(radius,180)
    t.left(180)
    t.circle(-radius/2.0, -180)
    t.end_fill()
    
t = turtle.Turtle()
t.reset()
draw_shape(200,"red")   #호출하면 빨간색 채워짐
t.setheading(180)
draw_shape(200, "blue") #호출하면 파란색 채워짐

turtle.done()
turtle.exitonclick()