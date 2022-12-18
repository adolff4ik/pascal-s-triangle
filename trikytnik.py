print(' 0\n010')
list = [0,1,0]

for i in range(100):
    newlist = []
    for q in range(len(list)):
        if q < 101 and int(len(list) - 1) != q:
            newnum = int(list[q] + list[q+1])
            newlist.append(newnum)
        else:
            break
    list.clear()

    list.append(0)
    for l in newlist:
        list.append(l)
    list.append(0)
    
    print(list)
