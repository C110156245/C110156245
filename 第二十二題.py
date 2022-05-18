a=[["123","456","9000"],["456","789","5000"],["789","888","3000"],["336","558","19000"],["775","666","10000"],["566","221","12000"]]
n=int(input("輸入查詢組數N為:"))
for i in range(n):
    a1,a2=map(str,input().split(" "))
    if a[0][0] == a1 and a[0][1] == a2:
        print(a[0][2])
    elif a[1][0] == a1 and a[1][1] == a2:
        print(a[1][2])
    elif a[2][0] == a1 and a[2][1] == a2:
        print(a[2][2])
    elif a[3][0] == a1 and a[3][1] == a2:
        print(a[3][2])
    elif a[4][0] == a1 and a[4][1] == a2:
        print(a[4][2])
    elif a[5][0] == a1 and a[5][1] == a2:
        print(a[5][2])
    else:
        print("error")
            
       
        
            