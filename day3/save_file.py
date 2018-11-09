# __author : david
# date:  2018/11/9

# def open_file(file_name ):

def save_file(boy,girl,count):
    file_name_boy = 'boy' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    girl_file.writelines(girl)
    boy_file.writelines(boy)

    boy_file.close()
    girl_file.close()


f = open('log.txt')

boy = []
girl = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        # each_line.s
        ( role, line_spoken) = each_line.split(':',1)
        if role == '小黄':
            boy.append(line_spoken)
        if role == '小王':
            girl.append(line_spoken)
    else:
        save_file(boy,girl,count)
        # file_name_boy = 'boy' + str(count) + '.txt'
        # file_name_girl =  'girl' + str(count) + '.txt'
        #
        # boy_file = open(file_name_boy,'w')
        # girl_file = open(file_name_girl,'w')
        #
        # girl_file.writelines(girl)
        # boy_file.writelines(boy)
        #
        # boy_file.close()
        # girl_file.close()

        boy = []
        girl = []
        count += 1

    save_file(boy, girl, count)
    # file_name_boy = 'boy' + str(count) + '.txt'
    # file_name_girl = 'girl' + str(count) + '.txt'
    #
    # boy_file = open(file_name_boy, 'w')
    # girl_file = open(file_name_girl, 'w')
    #
    # girl_file.writelines(girl)
    # boy_file.writelines(boy)
    #
    # boy_file.close()
    # girl_file.close()

f.close()