import random

guesses = ''
turns = 10

infile = open("words.txt", "r")   #메모장 가져오기
lines = infile.readlines()       
word = random.choice(lines)
word = word.strip('\n')

while turns > 0:     # turns 0보다 크면 계속 반복
    failed = 0             
    for char in word:      
        if char in guesses:    
            print(char, end="")    #맞으면 문자 넣음
        else:
            print("_", end="")     #틀리면 _ 그대로출력
            failed += 1    
    if failed == 0:          
        print("사용자 승리")  #다맞추면 사용자 승리 문구 출력
        break               #반복문 빠져나옴
    
    print("")
    guess = input("단어를 추측하시오: ") 
    guesses += guess                    
    
    if guess not in word:       #10번의 기회에서 틀릴때마다 기회 1번씩 줄임
        turns -= 1        
        print ("틀렸음!")
        print (str(turns)+ '기회가 남았음!') 
        if turns == 0:           
            print("사용자 패배 정답은 "+word)
           

infile.close()