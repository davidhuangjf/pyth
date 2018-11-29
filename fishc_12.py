# list1 = []
# for x in range(10):
#     for y in range(10):
#         if x % 2 == 0:
#             if y % 2 != 0:
#                 list1.append((x, y))


list2 = []
list2.clear()

for x in range(10):
    for y in range(10):
        if x % 2 == 0:
            if y % 2 != 0:
                list2.append((x, y))
print(list2)


list1 = ['1.Just do it', '2.一切皆有可能', '3.让编程改变世界', '4.Impossible is Nothing']
list2 = ['4.阿迪达斯', '2.李宁', '3.鱼C工作室', '1.耐克']
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
print(list3)
list3.reverse()
print(list3)