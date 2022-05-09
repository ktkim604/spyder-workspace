import turtle # 터틀 그래픽 모듈을 불러온다.
import random # 난수 모듈을 불러온다.

screen = turtle.Screen() 
image1 = "C:\\Users\\kim kyu tae\\Desktop\\front.GIF"
image2 = "C:\\Users\\kim kyu tae\\Desktop\\back.GIF"
screen.addshape(image1) #이미지 추가
screen.addshape(image2)

t1 = turtle.Turtle() # 첫 번째 거북이를 생성한다.
coin = random.randint(0, 1)
if coin == 0 :
	t1.shape(image1) #이미지 설정
	t1.stamp() #이미지 찍기
else :
	t1.shape(image2)
	t1.stamp()
    
turtle.done()