# number=int(input("请输入一个整数："))
# i = 1
# while number:
#     print(i)
#     i+=1
#     number= number - 1

number = int(input("请输入一个整数："))
while number:
    i = number - 1
    while i:
        print(" ",end="")
        i -= 1
    j=number
    while j:
        print("*",end="")
        j-=1
    print()
    number = number - 1