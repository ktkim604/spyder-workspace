import turtle
t = turtle.Turtle()

a = int(input("몇각형을 그릴건가요? "))
b = int(input("몇번 그릴건가요?"))

# n-각형을 그리는 함수를 정의한다
def n_polygon(a,b):
    for i in range(a):
        t.forward(b)
        t.left(360//a)



for i in range(b):
    t.left(20)
    n_polygon(a,100)
    
turtle.done()
turtle.onclickexit()