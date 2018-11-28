import random

times = 3
secret = random.randint(1, 10)
print("===============-- Start --============")

guess = 0
print("猜猜随机数，请输入一个整数：", end='')
while guess != secret and times > 0:
    temp = input()
    if temp.isdigit():
        guess = int(temp)
        if guess == secret:
            print("恭喜你，猜中了！")
            print("猜中了也没有奖励！")
        else:
            if guess > secret:
                print("你猜大了")
            else:
                print("你猜小了")
            if times > 1:
                print("再试一次吧: ", end='')
            else:
                print("机会用光了！")
    else:
        print("抱歉，您的输入有误，请输入一个整数：")
    times = times - 1
print("Game Over")