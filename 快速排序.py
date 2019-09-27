list1 = [1,3,5,2,4,7,8,6,9]

def Quick_Sort(list1,low,high):
    if low >= high:
        return
    base_num = list1[low]
    left = low
    right = high
    while low < high:
        while (low < high) and (base_num <= list1[high]):
            high -= 1
        list1[low] = list1[high]

        while(low<high) and (base_num >= list1[low]):
            low +=1
        list1[high] = list1[low]

        list1[low] = base_num
        Quick_Sort(list1,left,low-1)
        Quick_Sort(list1,low+1,right)
    return list1
high = len(list1)-1
low = 0

print(Quick_Sort(list1,low,high))