filename = input("파일 이름을 입력하세오: ") #파일 경로 입력
infile = open(filename,"r")
count = 0
for line in infile:#여러 줄이 있을 경우 각 줄을 line이라는 변수에 저장함
    words = line.split()
    for word in words:
        count += len(word) #글자 수를 더함
print("파일 안에는 총",count,"개의 글자가 있습니다.")

