import os
all_file = os.listdir(os.curdir)
type_dict = dict()
def lisdir():
    for eachline in all_file:
        if os.path.isdir(eachline):
            type_dict.setdefault('文件夹',0)
            type_dict['文件夹'] += 1
        else:
            ext = os.path.splitext(eachline)[1]
            type_dict.setdefault(ext,0)
            type_dict[ext] += 1
    return type_dict

Dir  = lisdir()

for key in Dir.keys():
    print("共有%d个文件名为%s"%(Dir[key],key))
