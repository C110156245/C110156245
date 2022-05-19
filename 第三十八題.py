
n=int(input("小狗可能跑到的地方:"))
way=[]
if n == 0:
    print("")
else:
    for i in range(n):
        a=int(input("距離:"))
        way.append(a)
    for h in range(len(way)):
        if way[h] % 9 ==0 or way[h] % 11 == 0:
            print(f"第{h+1}個點:{way[h]}") 

    
