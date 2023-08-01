#random.randint(多少到多少)
import random
answer = random.randint(1,10)
count =  3
while count >0:
    temp = input("1-10猜数字: \n")
    guess = int(temp)

    if guess == answer :
        print("正确")
        break
    else:
        if guess < answer:
            print("小了")
        else:
            print("大了")
    count = count - 1
print("游戏结束")
