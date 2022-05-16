def draw_square(x,y,c): #사각형을 그리는 함수
    t.fillcolor(c) #무슨 색으로 채울지 설정하는 함수
    t.penup() #펜을 올려 이동할 때 선을 그리지 않게 함
    t.goto(x,y) #(x,y)로 이동
    t.pendown() #펜을 내려 선을 그리게 함
    t.begin_fill() #색을 채우기 시작함
    for i in range(4): #for문을 이용해 직선을 4번 그림
        t.forward(100)
        t.left(90)
    t.end_fill()
    
import turtle
t = turtle.Turtle()
t.shape("turtle")
for c in ["yellow","red","blue"]: #노랑,빨강,파랑순으로 색을 칠 함
    a = int(input("x좌표를 입력하세요: "))
    b = int(input("y좌표를 입력하세요: "))
    draw_square(a,b,c)
    
turtle.done()
turtle.onclickexit()

