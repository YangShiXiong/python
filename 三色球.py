print("red  yellow  green")
count = 0
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(0,7):
            if (red + yellow + green) == 8:
                print("red=%d yellow=%d green=%d" % (red,yellow,green))
                count += 1

print("总的情况为：",count )