str1 = str(input('请输入一个字符串：'))
str2 = str(input('请输入一个子字符串：'))
def substr(str1,str2):
    length = len(str1)
    count =0
    for i in range(length):
        print(i)
        if str1[i:i+len(str2)] == str2:
            count += 1
    return count

count = substr(str1,str2)
print(count)