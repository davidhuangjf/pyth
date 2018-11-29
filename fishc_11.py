list1 = [1, 3, 2, 7, 9, 4, 8]
print(list1)
list1.insert(0,list1.pop())
print(list1)
print(list1[::2]) #步长