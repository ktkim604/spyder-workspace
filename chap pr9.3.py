from tkinter import *
 
window = Tk()                   #일종의 GUI 툴킷
window.title("My Calculator")   #계산기 이름 설정
display = Entry(window, width=33, bg="yellow")  #텍스트를 입력받거나 출력하기 위한 기입창을 생성
display.grid(row=0, column=0, columnspan=5)     #grid를 이용하여 위젯을 배치
 
button_list = [                 # 버튼에 표식될 텍스트를 리스트로 값 설정
'7', '8', '9', '/', 'C',
'4', '5', '6', '*', ' ',
'1', '2', '3', '-', ' ',
'0', '.', '=', '+', ' ' ]
 
row_index = 1
col_index = 0
 
# 버튼을 생성해서 리스트에 있는 값을 표식
# 17개의 버튼에 전부 이벤트 처리

for button_text in button_list:
    Button(window, text=button_text, width=5).grid(row=row_index, column=col_index) #버튼 생성해서 리스트에 있는 값을 표시
    col_index += 1              #col_index 값을 1씩 증가
    if col_index > 4:           #col_index 값이 1씩 증가하다가 4가 넘어갈 경우 행 인덱스를 1증가시키고 열 인덱스를 0으로 초기화
        row_index += 1
        col_index = 0
        
        
window.mainloop()
