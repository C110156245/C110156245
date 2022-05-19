n=int(input("請輸入幾階:"))
for i in range(n//2+1):
    for h in range(4-i):
        print(" ",end="")
    for h in range(2*i+1):
        print("*",end="")
    print()
for i in range(n//2,0,-1):
    for h in range(5-i):
        print(" ",end="")
    for h in range(2*i-1):
        print("*",end="")
    print()



