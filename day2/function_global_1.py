# __author : david
# date:  2018/10/8

x=50

def funciton_global1():
    global x
    print('x is ',x)
    x=2
    print('change global x to',x)

funciton_global1()
print('Value of x is ',x)