alist = []
sum = 0

for i in range(5): #5개의 정수를 리스트에 넣음
    i = int(input("정수를 입력해주세요 : "))
    alist.append(i)
    sum += i

avg = sum/len(alist) #평균을 구함
print("평균 =",avg) #평균을 출력