# __author : david
# date:  2018/11/9
# _*_ coding: utf-8 _*_
f = open('log_un.txt')

boy = []
girl = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        (role,line_spoken) = each_line.split(":",1)
        if role == '我':
            boy.append(line_spoken)
        if role == '黄':
            girl.append(line_spoken)
    else:
        # pass
        file_name_boy = "boy"+ count +".txt"
        file_name_girl = "girl" + count + ".txt"

        boyflie = open(file_name_boy,'w')
        girlflie = open(file_name_girl,'w')

        boyflie.writelines(boy)
        girlflie.writelines(girl)

        boyflie.close()
        girlflie.close()

        boy = []
        girl = []
        count += 1


# open_file('log.txt')