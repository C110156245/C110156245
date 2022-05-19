a=int(input('測試幾個:'))
listall=[]
for i in range(a):
    list1=list(map(int,input(":").split(" ")))
    listall.append(list1)
for h in range(len(listall)):
    if listall[h][3] / listall[h][2] == listall[h][2] / listall[h][1]:
        listall[h].append((listall[h][3])*(listall[h][3] / listall[h][2]))
        listall[h] = list(map(str,listall[h]))
        strA = " ".join(listall[h])
        print(strA)
        print("此為等比數列")
    elif listall[h][3] - listall[h][2] == listall[h][2] - listall[h][1]:
        listall[h].append((listall[h][3])+(listall[h][3] - listall[h][2]))
        listall[h] = list(map(str,listall[h]))
        strA = " ".join(listall[h])
        print(strA)
        print("此為等差數列")