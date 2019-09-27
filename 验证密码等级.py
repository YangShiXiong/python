import re
str1 = str(input('请输入密码：'))

# 1. 密码必须由数字、字母及特殊字符（仅限：）三种组合
# 2. 密码只能由字母开头
# 3. 密码长度不能低于 16 位
if re.search(r'^[a-zA-Z]+\d+:+|:+\d+',str1) and (len(str1) >= 16) :
    print("等级为高")

# 1. 密码必须由数字、字母或特殊字符（仅限：）任意两种组合
# 2. 密码长度不能低于 8 位
elif (re.search(r'([a-zA-Z0-9])*',str1) or (re.search(r'([0-9:])*',str1)) or re.search(r'([a-zA-Z:])*',str1)) and  (len(str1) > 8):
    print("密码等级为中")

# 1. 密码由单纯的数字或字母组成
# 2. 密码长度小于等于 8 位
elif str1.isdigit() or str1.isalpha() or (len(str1) <= 8):
    print("密码等级为低级")

else:
    print("密码为空")