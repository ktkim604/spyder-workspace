import turtle
t = turtle.Turtle()
t.shape("turtle")
 

t.fillcolor("red")
t.begin_fill() 
t.circle(50)   
t.end_fill()   
t.penup()      
t.goto(100,0)
t.pendown()    
 
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(200,0)
t.pendown()
 
t.fillcolor("blue")
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.done()

