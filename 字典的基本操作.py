def Fun(dict):
    for each in dict.keys():
        if each == 'C':
            print("C对应的值为'C' -> ",dict[each])

def FunA(dict):
    for each in dict.values():
        print(each,end=' ')
        print("\n")

def FunB(dict):
    for each in dict.items():
        print(each,end=' ')

dict = {'F':70,'C':60,'h':104,'i':105,'s':115}

Fun(dict)
FunA(dict)
FunB(dict)