def Palindrome_number(str1):
    str3 = ""
    str4 = ""
    length = (len(str1)//2)
    for i in range(length):
        str3 += str1[i]
    j = len(str1)-1
    while j > length:
        str4 += str1[j]
        j -= 1
    if str4 == str3:
        print("这是一个回文数")
    else:
        print("这不是回文数")
str1 = str(input('请输入一个字符串：'))
str2 = Palindrome_number(str1)
