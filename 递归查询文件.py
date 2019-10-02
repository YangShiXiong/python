import os
dir = input('请输入一个路径：')
file = input('请输入一个要查找的文件：')
def find_file(dir,file):
    os.chdir(dir)
    for each in os.listdir(os.curdir):
        print(each)
        if each == file:
            print(os.getcwd()+os.sep+each)
        if os.path.isdir(each):
            find_file(each,file)
            os.chdir(os.pardir)

find_file(dir,file)
