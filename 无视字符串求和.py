def sum(num):
    result = 0
    for i in num:
        if (type(i) == int) or (type(i) == float):
            result += i
        else:
            continue
    return result


num = [1,2,3,'str']
result =  sum(num)
print(result)