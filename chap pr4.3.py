import turtle
t = turtle.Turtle()
t.shape("turtle")
 
x1 = int(input("x1: " ))
y1 = int(input("y1: " ))
x2 = int(input("x2: " ))
y2 = int(input("y2: " ))
x3 = int(input("x3: " ))
y3 = int(input("y3: " ))
 
a = [x1, y1]
b = [x2, y2]
c = [x3, y3]
 
t.goto(a)
t.goto(b)
t.goto(c)

turtle.done()