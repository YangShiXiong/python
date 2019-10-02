file_name = input('请输入文件名：')
str1 = input('请输入要替换的字符：')
str2 = input('请输入替换的字符：')
def replace(file_name,str1,str2):
    file = open(file_name,'r')
    content = []
    count = 0
    for eachline in file:
        count += eachline.count(str1)
        eachline = eachline.replace(str1,str2)
        content.append(eachline)

    decide = input('文件%s中共有%d个%s,你要把所有的%s换成%s吗？\n[no/yes]:'%(file_name,count,str2,str2,str1))

    if decide == decide:
        file1 = open(file_name,'w')

        file1.writelines(content)
        file1.close()
    file.close()

replace(file_name,str1,str2)