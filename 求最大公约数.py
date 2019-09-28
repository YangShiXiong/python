def maxgreatest_common_diviso(x,y):

    if x>y:
        temp = y
        y = x
        x = temp

    while y:
        temp = x % y
        x = y
        y= temp
    return x
print(maxgreatest_common_diviso(4,6))


