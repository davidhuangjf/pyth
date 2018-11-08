# __author : david
# date:  2018/11/9

def open_file(file_name ):
    f = open(file_name)

    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            (role,line_spoken) = each_line.split(":",1)
            if role == '':