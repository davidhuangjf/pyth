temp = input("请输入年份： ")
while not temp.isdigit():
    print("抱歉，您的输入有误，请输入一个整数：")
year = int(temp)
if year/400 == int(year/400):
    print(temp + "是闰年！")
else:
    if year/4 == int(year/4) or year/100 == int(year/100):
        print(temp + "是闰年！")
    else:
        print(temp + "不是闰年！")

print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)