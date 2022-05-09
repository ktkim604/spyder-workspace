import random

x = random.randint(1, 10)
y = random.randint(1, 10)

correct = x*y
while True:
    user = int(input("%s * %s 는" %(x, y)))
    if(user == correct):
        print("맞았습니다!")
        break