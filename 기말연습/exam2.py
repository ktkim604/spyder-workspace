import random
import turtle

def draw_maze(x, y):   #경로 만들어주는 함수
	for i in range(2):
		t.penup()
		if i==1 :
			t.goto(x+100, y+100)
		else:
			t.goto(x, y)
		t.pendown()
		t.forward(300)
		t.right(90)
		t.forward(300)
		t.left(90)
		t.forward(300)

#키보드에서 화살표키가 눌리면 이벤키가 발생하고 이 이벤트 처리 함수 등록
def turn_left():
	t.left(10)
	t.forward(10)

def turn_right():
	t.right(10)
	t.forward(10)

t = turtle.Turtle()     #터틀 생성
screen = turtle.Screen()
t.shape("turtle")
t.speed(0)

draw_maze(-300, 200)  #경로만들어주고
t.penup(); 
t.goto(-300, 250)    #터틀 시작점으로 이동시킴
t.speed(1)
t.pendown();

screen.onkey(turn_left, "Left")   #onkeypress(함수명, 키보드버튼명)
screen.onkey(turn_right, "Right") #버튼을 눌렀을때 이 함수가 동작하도록 함

screen.listen()   # onclick()을 사용할때는 필수적으로 작성해야 함.
screen.mainloop() # 프로그램이 종료되지않고 화면을 유지하기위해 필요
