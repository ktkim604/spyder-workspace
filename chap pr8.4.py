problems = {"파이썬": "최근에 가장 떠오르는 프로그래밍 언어",
            "변수": "데이터를 저장하는 메모리 공간",
            "함수": "작업을 수행하는 문장들의 집합에 이름을 붙인 것",
            "리스트": "서로 관련이 없는 항목들의 모임"}

def show_words(problems):   # 문자만 입력하는 함수 호출
    display_message = ""
    i=1                     # i 초기값 설정   
    for word in problems.keys():   # 문자 반복문
        display_message += "("+str(i)+")"
        display_message += word + " "
        i += 1
    print(display_message)
    
for meaning in problems.values():  # 문장 반복문
    print("다음은 어떤 단어에 대한 설명일까요? ")
    print("\""+meaning+"\"")  #문자 설명하는 문장 출력
    
    correct = False
    while not correct:               #조건식이 True 일 경우 계속해서 반복
        show_words(problems)
        guessed_word = input("")     # 문장에 맞는 문자 입력
        if problems[guessed_word] == meaning:  # 문장에 맞는 문자 입력시 정답입니다 출력
            print("정답입니다. !")
            correct = True                  # 문장에 맞는 문자를 입력했을 경우 다음 문장 설명 
        else:                                   #문장에 맞지 않는 문자 입력시 정답이 아닙니다 출력
            print("정답이 아닙니다.")