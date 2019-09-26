num = str(input('请输入一个整数：'))
sum = 0
for i in num:
    print(i)
    sum = sum + int(i)*int(i)*int(i)

print(sum)

if str(num) == num:
    print('输入是一个水仙花数')
else:
    print('输入不是一个水仙花数')