def Fun(file_name,start,end):
    file = open(file_name,'r')
    count = 0
    if start == '':
        end = int(end)
        while end:
            f = file.readline()
            print(f)
            end -= 1
    elif end == '':
        start = int(start)
        f = True
        while f :
            f = file.readline()
            count += 1
            if count >= start:
                print(f)
    else:
        start = int(start)
        end = int(end)
        f = True
        while f:
            f = file.readline()
            count += 1
            if (count >= start) and (count<=end):
                print(f)


if __name__ == '__main__':
    file_name = input('请输入要打开的文件：')
    temp = str(input('请输入行数,列如 1:3 '))
    (start,end) = temp.split(':')
    Fun(file_name,start,end)