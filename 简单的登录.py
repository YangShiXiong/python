str = '''
|--- 新建用户: N/n ---|
|--- 登录用户: E/e ---|
|--- 退出程序: Q/q ---|
'''

global Date
Date = {}
def create():
    username = input('请输入用户名：')
    if username in Date:
        username = input('用户名已经存在,请输入其他用户名：')
    password = input('请输入密码：')
    Date[username] = password
    print("注册成功，赶紧登录试试吧")
    return
def login():
    username = input('请输入用户名：')
    if username not in Date:
        username = input('用户名不存在,请再次输入用户名：')
    password = input('请输入密码：')
    if Date[username] == password:
        print("欢迎进入xxoo系统，点击右上角结束程序！")

if __name__ == '__main__':
    flag = True
    while flag:
        print(str)
        temp = input("请输入指令代码：")
        if temp == 'Q' or temp =='q':
            flag = False

        if temp == 'N'or temp == 'n':
            create()

        if temp == 'E' or temp == 'e':
            login()

