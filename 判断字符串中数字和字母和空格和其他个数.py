str1 = str(input('请输入一个字符串：'))
def type_count(str1):
    alpha_count = 0
    digit_count = 0
    kongge_count = 0
    other_count = 0
    for each_1 in str1:
        if each_1.isalpha():
            alpha_count += 1
        elif  each_1.isdigit():
            digit_count += 1
        elif each_1 == ' ':
            kongge_count +=1
        else:
            other_count += 1

    print(alpha_count,digit_count,kongge_count,other_count)


type_count(str1)