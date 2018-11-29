# member = ['admwork','david']
# member.append(['竹林小溪', 'Crazy迷恋'])
# print(member)
# member.extend(['竹林小溪', 'Crazy迷恋'])
# print(member)


member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member.insert(1, 88)
member.insert(3, 90)
member.insert(5, 85)
member.insert(7, 90)
member.append(88)
print(member)

member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
print(member)
for each in member:
    print(each)

for each in range(len(member)):
    if each % 2 == 0:
        print(member[each], member[each+1])


count = 0
length = len(member)
while count < length:
    print(member[count], member[count+1])
    count += 2