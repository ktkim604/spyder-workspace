import turtle
t = turtle.Turtle()
t.shape("turtle")
 

x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
 
t.goto(x1,y1)
t.goto(x2,y2)
 
dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print("두점 사이의 거리= ",dist)
 
t.up()
t.write("점의 길이 = ", dist)
t.write(dist)
t.goto(x2,y2)