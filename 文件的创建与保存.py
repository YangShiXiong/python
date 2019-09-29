def write(content,file_name):
    f = open(file_name,'w')
    f.write(content)
    f.close()

if __name__ == '__main__':
    q = True
    file_name = input('请输入文件名：')
    while q:
        content = input('请输入内容：w保存退出')
        if content != 'w':
            write(content,file_name)
        else:
            q = False