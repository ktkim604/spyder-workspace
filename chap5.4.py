id = "ilovepython"
ps = "123456"
s = input("아이디를 입력하시오: ")
i = input("패스워드를 입력하시오: ")

if s == id:
    if i == ps:
        print("환영합니다.")
    else:
        print("아이디를 찾을 수 없습니다.")
    
else:
	print("아이디를 찾을 수 없습니다.")
