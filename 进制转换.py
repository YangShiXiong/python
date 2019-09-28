def Hex():
    q = True
    num = input('请输入一个整数，输入Q结束：')
    while q:
        if num == 'Q':
            q = False
        else:
            num = int(num)
            print('十进制转为十六进制：%d -> Ox%x' % (num, num))
            print('十进制转为八进制：%d -> Oo%o' % (num, num))
            print(' 十进制 转为二进制 : %d -> ' % num, bin(num))
            num = input('请输入一个整数，输入Q结束：')
Hex()