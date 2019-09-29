def How_old(num):
    if num == 1:
        return 10
    else:
        return How_old(num-1)+2

print(How_old(5))