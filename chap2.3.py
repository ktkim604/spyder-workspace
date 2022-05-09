import turtle
t = turtle.Turtle()
t.shape("turtle")

radius = 50
t.circle(radius)
radius = radius + 20
t.circle(radius)
radius = radius + 20
t.circle(radius)

turtle.done()
turtle.exitoneclick()