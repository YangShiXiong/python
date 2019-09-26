name = ['F','i','h','c']
print(name[0])
def Insert(name):
    length = len(name)-1
    while length > 0:
        print(name[length])
        if (name[length] == 'i') and (name[length-1]):
            return length
        else:
            length -= 1

index = Insert(name)

name.insert(index+1,'s')

print(name)