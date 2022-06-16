a=list(map(str,input("請輸入英文句子").split(" ")))
a1=[]
for i in range(len(a)-1,-1,-1):
    a1.append(a[i])

print(a1)