member = [' 小甲鱼 ', ' 黑夜', ' 迷途', ' 怡静', '秋舞斜阳 ']
member1 = [88, 95, 96, 97, 98]

def changlist(member,member1):
    return  zip(member,member1)

str = changlist(member,member1)

for i in str:
    print(i)