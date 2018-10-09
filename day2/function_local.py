
# __author : david
# date:  2018/10/8

x=50

def function_c(x):
    print('x is ',x)
    x=2
    print('change local x to',x)

function_c(x)
print('x is still',x)