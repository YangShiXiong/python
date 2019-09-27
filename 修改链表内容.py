list1 = [1, [1, 2, [' 小甲鱼 ']], 3, 5, 8, 13, 18]
list1[1][2] = '小鱿鱼'
def changelist1(list1):
    for each in list1:
        print(each)

changelist1(list1)