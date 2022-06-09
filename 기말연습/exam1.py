def calculate_area ():
    result = 3.14 * r**2
    return result

r = float(input("원의 반지름: "))
area = calculate_area()
print(area)



# def calculate_area (radius):
#     global area   
#     area = 3.14 * radius**2 # 전역변수 area에 계산값을 저장하려고 했다!
#     return

# area = 0
# r = float(input("원의 반지름: "))
# calculate_area(r)
# print(area)
        
