member = [' 小甲鱼 ', ' 黑夜', ' 迷途', ' 怡静', '秋舞斜阳 ']
member1 = [88, 95, 96, 97, 98]

def Insert(member,member1):
    for name in member1:
        member.insert(1,name)


def Append(member, member1):
    for name in member1:
        member.append(1, name)


print(Insert(member,member1),end = ' ')

print(Append(member,member1),end = '')