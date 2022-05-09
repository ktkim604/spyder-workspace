sum = 0
while True:
    a = int(input("정수를 입력하시오: "))
    if(a == 0):
        print("합은", sum, "입니다.")
        break
    
    sum += a