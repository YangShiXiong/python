list1 = [1,3,5,2,4,7,8,6,9]

def Sort(list1):
    length = len(list1)

    for i in range(length):
        for j in range(length-1):
            if list1[j] > list1[j+1]:
                temp = list1[j+1]
                list1[j+1] = list1[j]
                list1[j] = temp
    return list1

print(Sort(list1))