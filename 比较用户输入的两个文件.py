def compare(file_name1,file_name2):
    file1 = open(file_name1,'r')
    list1 = []
    list2 = []
    for eachline1 in file1:
        list1.append(list(eachline1))
    print(list1)
    file1.close()

    file2 = open(file_name2,'r')

    for eachline2 in file2:
        list2.append(list(eachline2))
    print(list2)
    file1.close()
    length1 = len(list1)
    print(length1)
    for i in range(length1):
        if list1[i] == list2[i]:
            continue
        else:
            for j in range(len(list1[i])):
                if list1[i][j] != list2[i][j]:
                    print("第%d行，第%d个"%(i,j))
                    break

file_name1 = input('请输入第一个文件名：')
file_name2 = input('请输入第二个文件名：')

compare(file_name1,file_name2)