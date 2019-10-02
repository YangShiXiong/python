import os

def findfile(dir,f):
    os.chdir(dir)
    for each in os.listdir(os.curdir):
        ext = os.path.splitext(each)[1]
        if (ext == '.mp4') or (ext == '.rmvb') or (ext == '.avi') :
            file = os.getcwd()+os.sep+each
            f.write(file)
        if os.path.isdir(each):
            findfile(each,f)
            os.chdir(os.pardir)
dir = input('请输入一个待查路径：')
f = open('vediolist.txt','w')
findfile(dir,f)
f.close()