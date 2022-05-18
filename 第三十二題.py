M=int(input("小明身上有多少錢:"))
N=int(input("有幾種飲料:"))
sum = 0
buy = 0
for i in range(N):
    sum+=10
    print(sum)
    if M >= sum:
        buy +=1
print(buy)

