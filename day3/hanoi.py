# __author : david
# date:  2018/10/31

def hanoi(n,a,b,c):
    # global number
    if n==1:
        print(a,' --> ',c)
        # global number

    else:
        hanoi(n-1,a,c,b)

        print(a, ' --> ',c)

        hanoi(n-1,b,a,c)


n=int(input("请输入层数："))
print(hanoi(n,"红","黄","绿"))
# print(hanoi(n,1,2,3))
