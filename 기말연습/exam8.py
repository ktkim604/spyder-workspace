import random

guesses = ''    #사용자로부터 지금까지 입력받은 모든 알파벳 보관
turns = 10

infile = open("word.txt", "r")   #메모장 가져오기
lines = infile.readlines()      #각각의 줄이 리스트 내부에 저장 
word = random.choice(lines)   # 랜덤 단어 뽑기 
word = word.strip('\n')

while turns > 0:     # turns 0보다 크면 계속 반복
    failed = 0             
    for char in word:      
        if char in guesses:    
            print(char, end="")    #맞으면 문자 넣음 end="" 은 줄바꿈하지 않음
        else:
            print("_", end="")     #틀리면 _ 그대로출력
            failed += 1    
    if failed == 0:          
        print("사용자 승리")  #다맞추면 사용자 승리 문구 출력
        break               #반복문 빠져나옴
    
    print("")
    guess = input("단어를 추측하시오: ")  #사용자 입력받기
    guesses += guess                    
    
    if guess not in word:       #10번의 기회에서 틀릴때마다 기회 1번씩 줄임
        turns -= 1        
        print ("틀렸음!")
        print (str(turns)+ '기회가 남았음!') 
        if turns == 0:           
            print("사용자 패배 정답은 "+word)
           

infile.close()

