import pickle
def save_file(boy,girl,count):
    file_name_boy = 'boy_'+str(count)+'.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'
    boy_file = open(file_name_boy,'wb')
    girl_file = open(file_name_girl, 'wb')
    pickle.dump(boy,boy_file)
    pickle.dump(girl,girl_file)
    boy_file.close()
    girl_file.close()
def Split(file):
    f = open(file,encoding='utf-8')
    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:6] != '======':
            (name,content) = each_line.split(':',1)
            if name == '小甲鱼':
                boy.append(content)
            if name == '客服':
                girl.append(content)
        else:
            save_file(boy,girl,count)
            count += 1
            boy = []
            girl = []
    save_file(boy, girl, count)
    f.close()
if __name__ == '__main__':
    Split('m.txt')