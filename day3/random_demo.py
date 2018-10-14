# __author : david
# date:  2018/10/14


import random
secret= random.randint(1,10)

print("==========********==========")
temp = input("请输入数字：")
guess=int(temp)
while True:
# while guess != secret:
    temp=input("请重新输入数字：")
    guess=int(temp)
    if guess == secret:
        print("卧槽，猜中了！！！！！")
        print("猜中了也没有奖励！")
        break
    else:
        if guess > secret:
            print("大了！")
        else:
            print("小了！！")

print("Game OVER")