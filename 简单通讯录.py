str = '''
---  欢迎进入通讯录程序   --
---  1：查询联系人资料    --
---  2：插入新的联系人    --
---  3：删除已有的联系人  --
---  4：退出通讯录程序    --
'''
print(str)

def Conect():
    date = {'ysx':18810589117}
    q = True
    while q:
        interge = int(input('请输入相关指令：'))

        if interge == 1:
            str1 = input('请输入查询人的名字：')
            for each in date.keys():
                if each == str1:
                    print(date[each])
        if interge == 2:
            str2 = input('请输入插入人的名字：')
            str3 = input('请输入插入人的电话号码：')
            date[str2] = str3

        if interge == 3:
            del date
        if interge == 4:
            q = False
    print("|---感谢使用通讯录 ---|")

Conect()