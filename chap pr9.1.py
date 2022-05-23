from tkinter import* #tkinter의 모든 정의를 임포트한다

#사각형 출력
def displayRect():
    canvas.create_rectangle(10,10,190,90,tags = "rect")  
    
#타원 출력
def displayOval():
    canvas.create_oval(10,10,190,90,fill = "red", tags = "oval") #그려진 타원 내부에 빨간색으로 색채움, 타원이 내접하는 사각형의 좌상단, 우하단 좌표

#호 출력
def displayArc():
    canvas.create_arc(10,10,190,90,start = 0, extent = 90, width = 8, fill = "red", tag = "arc")  #원이 내접하는 사각형의 좌상단, 우하단 좌표, extent는 호의각도
    
#다각형 출력
def displayPolygon():
    canvas.create_polygon(10,10,190,90,30,50, tags = "polygon") #(10,10) 좌표, (190,90)좌표, (30,50)좌표를 꼭지점으로 하는 다각형
    
#선분 출력
def displayLine():
    canvas.create_line(10,10,190,90,fill = "red", tags = "line")
    canvas.create_line(10,10,190,90, width = 9, arrow = "last", activefill = "blue", tags = "line")

#문자열 출력
def displayString():
    canvas.create_text(60,40, text = "Hi, i am a string", font = "Times 10 bold underline", tags = "string") #문자열을 그리는데 사용되는 함수.
    
#그림 제거
def clearCanvas():
    canvas.delete("rect", "oval", "arc", "polygon", "line", "string")  #tag 명령문을 이용해 그림을 식별하고 delete 메소드에서 이용
    
window = Tk() #창을 생성함
window.title("Canvas 그리기") #창 제목 설정

#윈도우 창에 캔버스 배치한다.
canvas = Canvas(window, width = 200, height = 100, bg = "white")
canvas.pack()
#프레임에 버튼을 배치한다
frame = Frame(window)
frame.pack()

btRectangle = Button(frame, text = "Rectangle", command = displayRect)  #Rectangle 버튼 생성
btOval = Button(frame, text = "Oval", command = displayOval)            #Oval 버튼 생성
btArc = Button(frame, text = "Arc", command = displayArc)               #Arc 버튼 생성
btPolygon = Button(frame, text = "Polygon", command = displayPolygon)   #Polygon 버튼 생성
btLine = Button(frame, text = "Line", command = displayLine)            #Line 버튼 생성
btString = Button(frame, text = "String", command = displayString)      #String 버튼 생성
btClear = Button(frame, text = "Clear", command = clearCanvas)          #Clear 버튼 생성


#같은 행에 각각의 열 번호 설정
btRectangle.grid(row = 1, column = 1)    
btOval.grid(row = 1, column = 2)
btArc.grid(row = 1, column = 3)
btPolygon.grid(row = 1, column = 4)
btLine.grid(row = 1, column = 5)
btString.grid(row = 1, column = 6)
btClear.grid(row = 1, column = 7)

window.mainloop()  #이벤트 루프를 생성한다.    