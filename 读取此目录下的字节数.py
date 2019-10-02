import os
def listdir():
    all_file = os.listdir(os.curdir)
    for each_line in all_file:
        print("文件名为%s，字节数为%d"%(each_line,os.path.getsize(each_line)))

listdir()