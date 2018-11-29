# password = "password"
# count = 3
# while count:
#     passwd = input('请输入密码：')
#     if passwd == password:
#         print("密码输入正确,账号登录中")
#         break
#     elif '*' in passwd:
#         print("密码中不可以有*，你还有", count, "次机会", end="")
#     else:
#         print("密码输入错误，你还有", count-1, "次机会", end="")
#     count -= 1
# else:
#     print("    锁定账号5分钟")


for i in range(100, 100000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp % 10) ** 3
        temp //= 10         # 注意这里要使用地板除哦~
    if sum == i:
        print(i)