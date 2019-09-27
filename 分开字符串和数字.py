str1 = "i2s154ovvvb4e3bferi32s56h;$c43.sfc67o0cm99"
def Split_Dig_alp(str1):
    list = []
    str3 = []
    for each in str1:
        if each.isdigit():
            list.append(each)
        else:
            str3.append(each)
    return list,str3
list,str3 = Split_Dig_alp(str1)

print(list)

print(str3)