class Book:                     # 클래스 정의
    def __init__(self,title):   # 생성자(매개변수 self와 title)
       # Book 클래스의 속성들
        self.title = title      
        self.price              
        self.publisher          
        self.year               
        
    def price(self,price):      # Book 클래스의 price 메소드(매개변수 self와 price)
        self.price = price      
        
    def publisher(self,publisher): # Book 클래스의 publisher 메소드(매개변수 self와 publisher)
        self.publisher = publisher 
        
    def year(self,year):       # Book 클래스의 year 메소드(매개변수 self와 year)
        self.year = year       
        
    def getBook(self):          # Book 클래스의 getBook 메소드(매개변수 self)
        bookinfo = "책제목 : " + self.title + ",출판사 : " + self.publisher +",출판년도: " + self.year + ", 가격: " + self.price
        return bookinfo # bookinfo 값 반환
        
a = Book("두근두근 파이썬") # Book 클래스로부터 객체를 생성함
b = Book("파이썬 Express") # Book 클래스로부터 객체를 생성함
        
a.publisher("생릉출판") # 객체 안의 publisher 메소드가 "생릉출판"을 인자로 받아 호출됨
a.year("2021")  # 객체 안의 year 메소드가 "2021"을 인자로 받아 호출됨
a.price("24000")   # 객체 안의 price 메소드가 "24000"을 인자로 받아 호출됨

ainfo = a.getBook()  # 객체 안의 getBook() 메소드가 호출되고 ainfo에 값이 저장됨

print(ainfo)  # ainfo 출력

b.publisher("생릉출판")  # 객체 안의 publisher 메소드가 "생릉출판"을 인자로 받아 호출됨
b.year("2020")      # 객체 안의 year 메소드가 "2021"을 인자로 받아 호출됨
b.price("30000")     # 객체 안의 price 메소드가 "24000"을 인자로 받아 호출됨

binfo = b.getBook()     # 객체 안의 getBook() 메소드가 호출되고 binfo에 값이 저장됨

print(binfo)     # binfo 출력