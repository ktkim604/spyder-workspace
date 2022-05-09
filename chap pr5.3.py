import random

solution = random.randint(0,99)#무작위 int형 숫자를 변수 x에 저장
x = int(input("복권번호를 입력하세요(0에서 99사이):")) #숫자를 입력 받음

print("당첨번호는",x,"입니다.") #당첨번호 출력
num1 = x // 10
num2 = x % 10
x1 = x // 10
x2 = x % 10
if (num1==x1 and num2==x2) or (num1==x2 and num2==x1): #숫자가 2개 전부 같을 때
    print("상금은 100만원 입니다.")
elif num1==x1 or num1==x2 or num2==x1 or num2==x2: #숫자가 1개만 같을 때
    print("상금은 50만원 입니다.")
else: #숫자 2개가 전부 다를 때
    print("상금은 없습니다.")